import Foundation
import EventKit

struct Failure: Error, CustomStringConvertible { let description: String; init(_ s: String) { description = s } }
let store = EKEventStore()
let iso = ISO8601DateFormatter()
func emit(_ value: Any) { let data = try! JSONSerialization.data(withJSONObject: value, options: [.sortedKeys]); print(String(data: data, encoding: .utf8)!) }
func str(_ r: [String: Any], _ key: String) throws -> String {
    guard let s = r[key] as? String, !s.isEmpty else { throw Failure("Missing string: \(key)") }; return s
}
func date(_ s: String) throws -> Date {
    guard let d = iso.date(from: s) else { throw Failure("Use ISO8601 timestamp with explicit UTC offset: \(s)") }; return d
}
func waitFor(_ done: () -> Bool) throws {
    let deadline = Date().addingTimeInterval(90)
    while !done() && Date() < deadline { RunLoop.current.run(until: Date().addingTimeInterval(0.05)) }
    if !done() { throw Failure("Timed out; inspect permission or operation state before retrying") }
}
func access(_ type: EKEntityType, request: Bool) throws {
    if EKEventStore.authorizationStatus(for: type) == .fullAccess { return }
    guard request else { throw Failure("Access missing. Run connect for this app and approve the macOS prompt.") }
    var done = false; var granted = false; var problem: Error?
    let cb: (Bool, Error?) -> Void = { ok, e in granted = ok; problem = e; done = true }
    if type == .event { store.requestFullAccessToEvents(completion: cb) }
    else { store.requestFullAccessToReminders(completion: cb) }
    try waitFor { done }
    guard granted else { throw Failure("Access not granted: \(problem?.localizedDescription ?? "Check System Settings > Privacy & Security")") }
}
// Fail closed: macOS full access is broader than the user's write policy.
func checkWritePolicy(_ app: String, _ id: String) throws {
    let url = FileManager.default.homeDirectoryForCurrentUser.appendingPathComponent("Library/Application Support/Steward/apple-policy.json")
    guard let data = try? Data(contentsOf: url),
          let policy = try JSONSerialization.jsonObject(with: data) as? [String: Any],
          let apps = policy[app] as? [String: Any],
          let entry = apps[id] as? [String: Any], entry["write"] as? Bool == true else {
        throw Failure("Write blocked by Steward's private-container policy. Shared and unknown containers are read-only.")
    }
    guard let stamp = entry["privateVerifiedAt"] as? String, let verified = iso.date(from: stamp),
          Date().timeIntervalSince(verified) >= -60, Date().timeIntervalSince(verified) <= 900 else {
        throw Failure("Private status needs a fresh Calendar/Reminders UI check; refresh privateVerifiedAt only after verifying this container is not shared.")
    }
}
func calendar(_ id: String, _ type: EKEntityType, write: Bool = false) throws -> EKCalendar {
    guard let c = store.calendars(for: type).first(where: { $0.calendarIdentifier == id }) else { throw Failure("Calendar/list ID not found; rediscover containers") }
    if write && !c.allowsContentModifications { throw Failure("Container is read-only") }; return c
}
func eventJSON(_ e: EKEvent) -> [String: Any] {
    return ["id": e.eventIdentifier ?? "", "calendar": e.calendar.calendarIdentifier,
            "title": e.title ?? "", "start": iso.string(from: e.startDate), "end": iso.string(from: e.endDate),
            "allDay": e.isAllDay, "notes": e.notes ?? "", "location": e.location ?? "",
            "recurring": e.hasRecurrenceRules || e.isDetached, "attendees": e.attendees?.count ?? 0,
            "alarms": (e.alarms ?? []).map { ["relativeSeconds": $0.relativeOffset, "absolute": $0.absoluteDate.map { iso.string(from: $0) } ?? ""] as [String: Any] },
            "availability": e.availability.rawValue, "status": e.status.rawValue]
}
func reminderJSON(_ r: EKReminder) -> [String: Any] {
    var result: [String: Any] = ["id": r.calendarItemIdentifier, "calendar": r.calendar.calendarIdentifier,
      "title": r.title ?? "", "notes": r.notes ?? "", "completed": r.isCompleted, "priority": r.priority, "recurring": r.hasRecurrenceRules, "alarms": (r.alarms ?? []).map { ["relativeSeconds": $0.relativeOffset, "absolute": $0.absoluteDate.map { iso.string(from: $0) } ?? ""] as [String: Any] }]
    if let dc = r.dueDateComponents {
        result["dueComponents"] = ["year": dc.year ?? 0, "month": dc.month ?? 0, "day": dc.day ?? 0,
                                    "hour": dc.hour ?? -1, "minute": dc.minute ?? -1]
        if let d = Calendar.current.date(from: dc) { result["due"] = iso.string(from: d) }
    }
    return result
}
func reminders(_ c: EKCalendar) throws -> [EKReminder] {
    var result: [EKReminder]?; var done = false
    store.fetchReminders(matching: store.predicateForReminders(in: [c])) { result = $0; done = true }
    try waitFor { done }; guard let result else { throw Failure("Reminders fetch failed") }; return result
}
func event(_ r: [String: Any], _ c: EKCalendar) throws -> EKEvent {
    guard let e = store.event(withIdentifier: try str(r, "id")), e.calendar.calendarIdentifier == c.calendarIdentifier else { throw Failure("Event not found in selected calendar") }
    return e
}
func reminder(_ r: [String: Any], _ c: EKCalendar) throws -> EKReminder {
    guard let item = store.calendarItem(withIdentifier: try str(r, "id")) as? EKReminder,
        item.calendar.calendarIdentifier == c.calendarIdentifier else { throw Failure("Reminder not found in selected list") }; return item
}
func run(_ r: [String: Any]) throws -> [String: Any] {
    let op = try str(r, "op")
    if op == "status" {
        return ["calendarAuthorization": EKEventStore.authorizationStatus(for: .event).rawValue,
                "remindersAuthorization": EKEventStore.authorizationStatus(for: .reminder).rawValue,
                "timezone": TimeZone.current.identifier]
    }
    let app = try str(r, "app")
    guard ["calendar", "reminders"].contains(app) else { throw Failure("app must be calendar or reminders") }
    let type: EKEntityType = app == "calendar" ? .event : .reminder
    try access(type, request: op == "connect")
    if ["connect", "containers"].contains(op) {
        return ["containers": store.calendars(for: type).map { ["id": $0.calendarIdentifier, "name": $0.title,
            "source": $0.source.title, "sourceID": $0.source.sourceIdentifier, "writable": $0.allowsContentModifications] as [String: Any] }]
    }
    if op == "create-container" {
        guard r["apply"] as? Bool == true else { return ["state": "preview", "request": r] }
        let policyURL = FileManager.default.homeDirectoryForCurrentUser.appendingPathComponent("Library/Application Support/Steward/apple-policy.json")
        let data = try Data(contentsOf: policyURL)
        var policy = try JSONSerialization.jsonObject(with: data) as! [String: Any]
        guard policy["allowContainerCreation"] as? Bool == true else { throw Failure("Container creation is disabled by local policy") }
        guard let source = store.sources.first(where: { $0.sourceIdentifier == r["source"] as? String }) else { throw Failure("Choose a discovered source ID") }
        let title = try str(r, "name")
        guard !store.calendars(for: type).contains(where: { $0.title == title && $0.source.sourceIdentifier == source.sourceIdentifier }) else { throw Failure("Container name already exists; inspect it instead of duplicating") }
        let c = EKCalendar(for: type, eventStore: store); c.title = title; c.source = source
        try store.saveCalendar(c, commit: true)
        var appPolicy = policy[app] as? [String: Any] ?? [:]
        appPolicy[c.calendarIdentifier] = ["name": title, "write": true, "privateVerifiedAt": iso.string(from: Date()), "provenance": "created-private-by-Steward"]
        policy[app] = appPolicy
        try JSONSerialization.data(withJSONObject: policy, options: [.prettyPrinted, .sortedKeys]).write(to: policyURL, options: .atomic)
        return ["state": "created", "container": ["id": c.calendarIdentifier, "name": c.title, "source": c.source.title]]
    }
    let mutating = ["create", "update", "delete", "rename-container", "delete-container"].contains(op)
    if mutating && r["apply"] as? Bool == true { try checkWritePolicy(app, str(r, "calendar")) }
    let c = try calendar(str(r, "calendar"), type, write: mutating)
    if op == "delete-container" {
        guard r["apply"] as? Bool == true else { return ["state": "preview", "request": r] }
        if type == .event {
            guard store.calendars(for: .event).filter({ $0.title == c.title }).count == 1 else { throw Failure("Ambiguous calendar name; exact empty check unavailable") }
            let task = Process(); let output = Pipe(); let errors = Pipe()
            task.executableURL = URL(fileURLWithPath: "/usr/bin/osascript")
            task.arguments = ["-l", "JavaScript", "-e", "function run(argv) { var a=Application('Calendar'); var cs=a.calendars.whose({name:argv[0]})(); if(cs.length!==1) throw new Error('Ambiguous calendar'); return cs[0].events().length; }", c.title]
            task.standardOutput = output; task.standardError = errors
            try task.run(); task.waitUntilExit()
            let count = String(data: output.fileHandleForReading.readDataToEndOfFile(), encoding: .utf8)?.trimmingCharacters(in: .whitespacesAndNewlines)
            guard task.terminationStatus == 0, count == "0" else { throw Failure("Calendar nonempty or empty-check unavailable; deletion blocked") }
        } else {
            guard try reminders(c).isEmpty else { throw Failure("List is not empty; bulk deletion requires a separate reviewed workflow") }
        }
        try store.removeCalendar(c, commit: true)
        guard store.calendar(withIdentifier: try str(r, "calendar")) == nil else { throw Failure("Container deletion read-back unverified") }
        return ["state": "deleted", "id": try str(r, "calendar")]
    }
    if op == "rename-container" {
        guard r["apply"] as? Bool == true else { return ["state": "preview", "request": r] }
        c.title = try str(r, "name"); try store.saveCalendar(c, commit: true)
        return ["state": "renamed", "container": ["id": c.calendarIdentifier, "name": c.title]]
    }
    if op == "list" {
        if type == .event {
            let start = try date(str(r, "start")), end = try date(str(r, "end"))
            guard end > start, end.timeIntervalSince(start) <= 93 * 86400 else { throw Failure("Query window must be positive and at most 93 days") }
            let events = store.events(matching: store.predicateForEvents(withStart: start, end: end, calendars: [c]))
            return ["items": events.sorted { $0.startDate < $1.startDate }.map(eventJSON)]
        }
        let include = r["includeCompleted"] as? Bool ?? false
        return ["items": try reminders(c).filter { include || !$0.isCompleted }.map(reminderJSON)]
    }
    if op == "get" { return ["item": try type == .event ? eventJSON(event(r, c)) : reminderJSON(reminder(r, c))] }
    guard mutating else { throw Failure("Unknown operation") }
    guard r["apply"] as? Bool == true else { return ["state": "preview", "request": r] }
    let fields = r["fields"] as? [String: Any] ?? [:]
    let token = r["token"] as? String ?? ""
    let marker = "[steward:\(token)]"
    if op == "create", token.isEmpty { throw Failure("Create needs a stable token; reuse it when recovering an uncertain result") }
    if type == .event {
        let e: EKEvent
        if op == "create" {
            let start = try date(str(fields, "start")), end = try date(str(fields, "end"))
            guard end > start else { throw Failure("end must follow start") }
            let matches = store.events(matching: store.predicateForEvents(withStart: start, end: end, calendars: [c])).filter { ($0.notes ?? "").contains(marker) }
            if let existing = matches.first { return ["state": "existing", "item": eventJSON(existing)] }
            e = EKEvent(eventStore: store); e.calendar = c; e.startDate = start; e.endDate = end
            e.title = try str(fields, "title"); e.notes = marker; e.alarms = []
        } else { e = try event(r, c) }
        // Series edits and invitations need a dedicated UI-aware workflow.
        guard !e.hasRecurrenceRules, !e.isDetached, (e.attendees?.isEmpty ?? true), e.organizer == nil else { throw Failure("Recurring or invited event: use Calendar UI to choose occurrence/series and notification scope") }
        if op == "delete" {
            try store.remove(e, span: .thisEvent, commit: true)
            guard store.event(withIdentifier: try str(r, "id")) == nil else { throw Failure("Deletion read-back did not confirm removal") }
            return ["state": "deleted", "id": try str(r, "id")]
        }
        if let v = fields["title"] as? String { e.title = v }
        if let v = fields["start"] as? String { e.startDate = try date(v) }
        if let v = fields["end"] as? String { e.endDate = try date(v) }
        guard e.endDate > e.startDate else { throw Failure("end must follow start") }
        if let v = fields["notes"] as? String { e.notes = op == "create" ? v + "\n" + marker : v }
        if let v = fields["location"] as? String { e.location = v }
        if let v = fields["allDay"] as? Bool { e.isAllDay = v }
        if e.isAllDay {
            guard Calendar.current.startOfDay(for: e.startDate) == e.startDate,
                  Calendar.current.startOfDay(for: e.endDate) == e.endDate else {
                throw Failure("All-day boundaries must be midnight in the Mac's local timezone, with exclusive end")
            }
        }
        if let minutes = fields["alertMinutesBefore"] as? Int { e.alarms = [EKAlarm(relativeOffset: -Double(minutes * 60))] }
        else if fields["alertMinutesBefore"] is NSNull { e.alarms = [] }
        try store.save(e, span: .thisEvent, commit: true)
        guard let saved = store.event(withIdentifier: e.eventIdentifier) else { throw Failure("Saved but read-back failed; inspect before retry") }
        return ["state": "saved", "item": eventJSON(saved)]
    }
    let item: EKReminder
    if op == "create" {
        if let existing = try reminders(c).first(where: { ($0.notes ?? "").contains(marker) }) { return ["state": "existing", "item": reminderJSON(existing)] }
        item = EKReminder(eventStore: store); item.calendar = c; item.title = try str(fields, "title"); item.notes = marker
    } else { item = try reminder(r, c) }
    guard !item.hasRecurrenceRules else { throw Failure("Recurring reminder: use Reminders UI for series-aware edits") }
    if op == "delete" {
        try store.remove(item, commit: true)
        guard store.calendarItem(withIdentifier: try str(r, "id")) == nil else { throw Failure("Deletion read-back did not confirm removal") }
        return ["state": "deleted", "id": try str(r, "id")]
    }
    if let v = fields["title"] as? String { item.title = v }
    if let v = fields["notes"] as? String { item.notes = op == "create" ? v + "\n" + marker : v }
    if let v = fields["completed"] as? Bool { item.isCompleted = v }
    if let v = fields["priority"] as? Int { guard (0...9).contains(v) else { throw Failure("priority must be 0...9") }; item.priority = v }
    if let v = fields["due"] as? String {
        let d = try date(v)
        var dc = Calendar.current.dateComponents(in: TimeZone.current, from: d)
        dc.second = nil; dc.nanosecond = nil
        item.dueDateComponents = dc
    } else if fields["due"] is NSNull { item.dueDateComponents = nil }
    if let when = fields["remindAt"] as? String { item.alarms = [EKAlarm(absoluteDate: try date(when))] }
    else if fields["remindAt"] is NSNull { item.alarms = [] }
    try store.save(item, commit: true)
    guard let saved = store.calendarItem(withIdentifier: item.calendarItemIdentifier) as? EKReminder else { throw Failure("Saved but read-back failed; inspect before retry") }
    return ["state": "saved", "item": reminderJSON(saved)]
}
do {
    let data = FileHandle.standardInput.readDataToEndOfFile()
    guard let request = try JSONSerialization.jsonObject(with: data) as? [String: Any] else { throw Failure("Expected JSON object") }
    emit(try run(request))
} catch { emit(["error": String(describing: error), "state": "failed-or-uncertain"]); exit(1) }
