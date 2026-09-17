# Product validation, 0.2.0

Verified on 2026-09-16. This release combines the earlier Apple connector with resumable connection onboarding, scoped context retrieval, a `$steward` entry, and versioned distribution. Historical checks are in [Apple validation](apple-validation.md) and [guided-session validation](guided-sessions-validation.md); they do not automatically certify new changes.

## Automated checks

- **24 Python tests passed:** Apple request validation, preview boundaries, memory setup and preservation, connection choices and denied access, scope changes and disconnect, installation conflicts, managed update backups, and distribution contents.
- **Native Notes mock passed:** preview and unknown-operation gates made no Apple app calls.
- **16 skills and 147 portable references passed** the structural validator. The archive checks the shipped tree as well as source.
- The distribution test built a self-contained package, checked its hash and manifest, excluded synthetic private state, and installed directly from the extracted folder.
- The packaged plugin manifest and the new Steward entry’s skill metadata passed their dedicated validators. A valid local bundle is not proof of marketplace availability or installation through every host.

## Independent forward trials

Two independent agent trials used copied runtime files and synthetic adapters. They could not access live apps or the personal vault. Their prompts supplied ordinary first-use and returning-user requests, without a scripted sequence of skill operations.

| Trial | Observed result | Boundary verified |
|---|---|---|
| New Markdown user, Calendar + Reminders selected | Created memory and a trusted workspace pointer; saved choices; Calendar read succeeded; Reminders denial remained blocked; produced two proposed walks with exact after-work timing pending | Four skipped apps stayed skipped. Three synthetic read calls, zero external writes. Optional denial did not prevent useful work. |
| Returning user with a saved walking goal | Recovered goal, constraints, and onboarding state; refreshed only the selected calendar; saved a dated plan and next step | One synthetic read, zero external writes. No onboarding restart, skipped-app reads, or invented participation. |

These trials establish the observed paths, not population-level usability or a guarantee of future agent behavior. First setup still requires a verified workspace-to-memory pointer in addition to creating files. Instruction reading carries overhead; the brief product entry shares existing routing rather than duplicating it. Synthetic adapter observations are identified as synthetic in the trial records and are not live connection evidence.

## Live access and limits

On the development Mac, current Calendar, Reminders, and Notes container discovery succeeded. Contacts, Mail, and Messages exposed readable account content through host app control. Only observation status and scopes were saved to the private connection registry; private content is excluded from this repository and release.

Those checks establish reading through the observed routes at that time. They do not certify Mail/Messages sending, every Contacts mutation, all accounts, delivery of notifications, or every Apple UI feature. Earlier explicitly authorized disposable Calendar/Reminders/Notes write tests are described in [Apple validation](apple-validation.md). No test message or email was sent during this onboarding validation.

The suite requires a capable host and user-selected access. A connection can later fail or become stale; current facts and consequential actions require fresh verification. Private/shared restrictions, host approval rules, and the user's specific action authorization remain separate from connection status. No background service is installed.

## 0.2.1 naming migration

The repository and runtime now use Steward consistently. All 25 Python tests passed, including a migration trial that preserves local edits, backs up legacy folders, and verifies that only 16 current skill entries remain. Native Notes mock gates and 147 portable runtime references passed. The prior behavioral trials remain historical evidence; they were not repeated for this naming-only runtime change. Raw trial artifacts retain their original command names.

## 0.2.2 guides and conversational onboarding

All 25 Python tests, native Notes mock gates, 147 runtime references, and the edited session skill’s metadata passed. The guide check resolved 31 relative links and found all 16 skills in the optional map. An independent agent read the revised runtime and responded to two isolated synthetic requests: uncertain first use with no storage/apps, and an already-set-up user asking for a simple message draft. The first stopped at one focused unanswered question; the second returned the draft without onboarding or sending. Neither required the user to select a supporting skill. These are bounded response checks, not a test of a full multi-turn onboarding or live app execution.

The root installation procedure makes repository-link installation explicit, separates installed files from host discovery, and preserves manual permission/account boundaries. Distribution tests install directly from the extracted release folder.

For 0.2.2, a release candidate also passed checksum verification, archive-path inspection, extraction, installer preview, and installation of all 16 skills into a fresh temporary host directory. The packaged INSTALL.md was present. This checks the distribution mechanics; it does not certify every host’s automatic discovery or permissions flow.
