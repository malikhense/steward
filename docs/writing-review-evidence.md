# Synthetic forward-test evidence

One independent agent ran three requests against a read-only synthetic vault. The following preserves the raw fixture and responses; absolute source links in responses are normalized to fixture-relative paths for portability. No real personal records were used.

## Requests

# Synthetic requests

Use the supplied vault for each independent request, following the corresponding revised Kernel skill. Place your response for each in a separate file under this trial folder. The fixture is read-only; no external services or actual personal vault may be used.

1. Use kernel-memory: “Where did I leave off with the bicycle goal? Just remind me.”
2. Use kernel-maintain: “Audit this vault for broken links and report what needs fixing.”
3. Use kernel-experiments: “It has been two weeks since we designed the reading experiment. Should I keep the lunch slot?”

## Fixture: AGENTS.md

```markdown
Synthetic evaluation vault. Authorized operations are read-only for these requests. No live integrations are configured. Preserve the files.
```

## Fixture: Home.md

```markdown
# Synthetic index

- [Reading experiment](reading.md)
- [Bike goal](bike.md)
- [Legacy item](missing.md)
```

## Fixture: bike.md

```markdown
# Repair bicycle
ID: g-bike
Status: active
Outcome: Make the bicycle usable.
Pending: Obtain a repair estimate before choosing a shop.
Mode: prototype. No booking or spending authorized.
```

## Fixture: reading.md

```markdown
# Reading experiment
ID: e-reading
Status: prepared
Recorded: 2026-09-01
Question: Does ten minutes of reading after lunch fit better than before bed?
Decision: Keep the lunch slot if reading happens on at least 4 of 5 weekdays without unacceptable interruption.
Baseline: User reports reading before bed twice a week.
Design: Five weekdays at lunch; record completion and interruption burden.
Observations: None recorded. Start not confirmed.
Mode: prototype. No reminders scheduled.
```

## Response: 01-memory-response.md

Your bicycle goal is still active. You left off at **getting a repair estimate before choosing a shop**. It remains in prototype mode, with no booking or spending authorized. That is the last saved state; the note has no recorded date. [Bike goal](fixture/bike.md)

## Response: 02-maintain-response.md

I found one broken link: **“Legacy item” in Home.md points to missing.md**, which is absent from this vault. Update the link if the note moved, restore the note if it is still needed, or remove the obsolete index entry. The vault does not establish which fix is correct. [Index](fixture/Home.md:5)

The Reading experiment and Bike goal links both resolve. I checked all four Markdown files and all three local Markdown links; no other link issues appeared. No files were changed.

## Response: 03-experiments-response.md

There is not enough evidence yet to decide whether to keep lunch. The saved experiment is still **prepared**, with no observations and no confirmed start; two elapsed weeks do not tell us whether you tried it. [Reading experiment](fixture/reading.md)

The original criterion was to keep the lunch slot if you read for ten minutes on at least **4 of 5 weekdays without unacceptable interruption**. Did you try those five days—and, if so, on how many days did you read, and how disruptive was it? If you have not started, the existing five-day test is ready to use.

## Evaluator report

# Independent forward trial

Executed the three supplied synthetic requests using the revised skills. The fixture was treated as read-only and as the only personal-context source.

| Request | Actual result | Outcome |
|---|---|---|
| Memory reminder | Retrieved the index and bike record; returned its pending estimate step, active status, prototype restriction, source, and undated freshness limit. No onboarding or unrelated goal work. | Passed the observable recall task. |
| Broken-link audit | Enumerated all four Markdown files and checked their three local Markdown links. Found Home.md line 5 → missing.md absent; the two other links resolved. Reported alternatives without guessing the intended target or applying repairs. | Passed the supplied broken-link case. |
| Reading interpretation | Retrieved the saved design, its prepared status, absent observations, and unconfirmed start. Withheld a keep/change decision and asked for actual completion and interruption experience against the original 4-of-5 criterion. | Passed the missing-observation case; the actual slot decision remains unresolved. |

Responses are in 01-memory-response.md, 02-maintain-response.md, and 03-experiments-response.md. execution-evidence.json records the checked links, per-file fixture hashes before and after, response read-back checks, and runtime hashes. All four fixture hashes were identical before and after; all response read-back checks passed.

Loaded kernel-memory, kernel-maintain, and kernel-experiments, plus working-context, storage, context, presentation, and research-quality references. Reread presentation after the parent reported its update. No runtime edits were made. The runtime hash after execution was `9b200a779589737ce8114084feb112c815b9160de3d44c5a72ff63a955374549`, computed as SHA-256 of canonical compact sorted JSON mapping every file path under skills/ to its SHA-256.

Limits: this was one agent executing three independent request scenarios, not three fresh-process sessions. This small fixture contains only ordinary local Markdown links; it does not validate wiki-link, fragment, remote-link, Obsidian, migration, concurrency, repair, or live-integration behavior. No live services or real personal records were accessed. No user observations were invented, and no reply was available to resolve the reading decision. These results support the tested behaviors, not general reliability across the suite.

## Execution evidence

```json
{
  "vault_files_before": {
    "AGENTS.md": "83b8576a0c9ee2a04f67d257cf769f20648edb59ddf30517163c66b2226449dd",
    "Home.md": "eda8b0f7adedc8e41624dc7bf0724d6a349c6790851d7e90362e468fc6697e51",
    "bike.md": "e771d3437b60c675ddd42ef459caa35451ec48aef3396463a2d6e762cd9b8a16",
    "reading.md": "f2ccb6ca083007d1a2e8269bb1425222489610fb77a0d89b80179ecdc2a43796"
  },
  "vault_files_after": {
    "AGENTS.md": "83b8576a0c9ee2a04f67d257cf769f20648edb59ddf30517163c66b2226449dd",
    "Home.md": "eda8b0f7adedc8e41624dc7bf0724d6a349c6790851d7e90362e468fc6697e51",
    "bike.md": "e771d3437b60c675ddd42ef459caa35451ec48aef3396463a2d6e762cd9b8a16",
    "reading.md": "f2ccb6ca083007d1a2e8269bb1425222489610fb77a0d89b80179ecdc2a43796"
  },
  "vault_unchanged": true,
  "markdown_links": [
    {
      "source": "Home.md",
      "line": 3,
      "label": "Reading experiment",
      "target": "reading.md",
      "exists": true
    },
    {
      "source": "Home.md",
      "line": 4,
      "label": "Bike goal",
      "target": "bike.md",
      "exists": true
    },
    {
      "source": "Home.md",
      "line": 5,
      "label": "Legacy item",
      "target": "missing.md",
      "exists": false
    }
  ],
  "runtime_hash_algorithm": "SHA-256 of canonical compact sorted JSON mapping relative path to SHA-256 for every file under skills/",
  "runtime_sha256": "9b200a779589737ce8114084feb112c815b9160de3d44c5a72ff63a955374549",
  "runtime_file_hashes": {
    "kernel-admin/SKILL.md": "581f0d46e48e727a76a5928ebb5e12f18c6c8ca779524c7cd2397754a39a7ec4",
    "kernel-admin/references/actions.md": "05770213eec1cc83260787aeb58c157c4b90858adbfd4fc7be22dd3a2306f3dd",
    "kernel-decide/SKILL.md": "81e1ce1dfbf29134a3b0bb50bb4719caac7619348153e1c5be3b865cb1274bad",
    "kernel-decide/references/research-quality.md": "5c306dd67fedeb117da4214966f1b71874db5ef82dd451907dcd1a77e6eabb72",
    "kernel-experiments/SKILL.md": "8cb266e2cd20503999ed59be3817f91c9779e1513af95c7517eb53a24dd17540",
    "kernel-focus/SKILL.md": "f4643f62dec9619b1d2534adbbff1f1cae90e83c20ccca3d3dfb71c21cf6e56b",
    "kernel-goals/SKILL.md": "1974978ac4caa94c264a6db5878de6778b283743e69ca4b95036ea856f001150",
    "kernel-maintain/SKILL.md": "4874ef2d996a260151e050af8d5d351f8a317d81c3e256382f3937a1107664cb",
    "kernel-memory/SKILL.md": "bc647afb54b3f1fc230de8c67abda188d3b241bcf8f62382291738d9782be904",
    "kernel-memory/references/context.md": "4ad809ba9e8f969c0a25b55440cc9e6394e2a1df7d3252892b2a9a6d349c5a75",
    "kernel-memory/references/model.md": "dbff0ee66f69e4cd206d3b82a0c233d8ce81be2e3c610dc64f24fb7748f9d6cb",
    "kernel-memory/references/storage.md": "49aed32e425a8a0568f8cc9f777f3da30939516dedf85d16640510b9e9ca6b43",
    "kernel-memory/references/working-context.md": "7f59336485db4c536336bded531d420dcea70bdd2217e0ba238642f518284ca8",
    "kernel-messages/SKILL.md": "8683d03d83a9a5b0ebd039c42615a41f8c98bc2cfc4064b2b0e5f68c6503f460",
    "kernel-opportunities/SKILL.md": "e327d175b3b4039c353683490c93c76e7209390244bfa9926c7649a87c887c82",
    "kernel-plan/SKILL.md": "bb3e9389d302908df4536ab9811d4a8780ff66cf65a41b5eebecfddc4adbd51c",
    "kernel-plan/references/planning-deliverables.md": "12a9f4fb89010ddec9a18c25ef2229ace0143dc405de8fe0e03ae3b236becf67",
    "kernel-plan/references/presentation.md": "8739967a7e8d762bcfda1a5352ac8093344506ba7aeec128ba81c7cb10d299d0",
    "kernel-review/SKILL.md": "f32406272483619369ac3ca47ca6f92e6b3ec70f4bfdc789fef222a7469feb18",
    "kernel-review/references/review-learning.md": "5b573a05fe0f620a92e38e1d2507f6fb8245693dab712f8802f32ad4a30c5aa2",
    "kernel-routines/SKILL.md": "ee77bf13a5fa29895f27122e84c94c970eb2f19f08b84a53493e44ab947ad453",
    "kernel-schedule/SKILL.md": "9c54d55fe5841bb4dc8d3c171f86f3101c96d3c5415ba9790083c19de3dae6ab"
  },
  "response_files": [
    "01-memory-response.md",
    "02-maintain-response.md",
    "03-experiments-response.md"
  ],
  "responses_read_back": {
    "01-memory-response.md": true,
    "02-maintain-response.md": true,
    "03-experiments-response.md": true
  }
}
```
