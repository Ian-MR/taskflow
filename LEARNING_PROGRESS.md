# LEARNING_PROGRESS.md — Phase 2

This is not a checklist of technologies.

Use it to record demonstrated engineering growth.

---

## Starting point

Phase 1 completed:

- Django fundamentals;
- ORM / QuerySets;
- ownership-based authorization;
- database constraints;
- PostgreSQL;
- migrations;
- tests;
- Docker;
- production settings;
- CI;
- release artifact flow;
- Git/PR workflow.

Phase 2 focus:

- domain modeling;
- financial correctness;
- broader testing;
- atomic operations;
- dates/timezones;
- migration safety;
- idempotency;
- operational maturity;
- product-driven architecture.

---

## Sprint log

### Sprint 0

**Goal:** Product pivot and finance foundation.

#### What I implemented
-

#### Decisions I made
-

#### Bugs I investigated
-

#### Review findings I received
-

#### Concepts I had to learn
-

#### What I can now explain without help
-

#### Recurring mistake to watch
-

#### Senior assessment
-

---

### Sprint 1

**Goal:** Transactions and categories.

#### What I implemented
-

#### Decisions I made
-

#### Bugs I investigated
-

#### Review findings I received
-

#### Concepts I had to learn
-

#### What I can now explain without help
-

#### Recurring mistake to watch
-

#### Senior assessment
-

---

## Competency matrix

Use:
- `N` — not yet demonstrated
- `A` — assisted
- `I` — independent
- `R` — reliable / repeatable

| Competency | Level | Evidence |
|---|---:|---|
| Django request/response | R | Phase 1 |
| Basic ORM | R | Phase 1 |
| Ownership authorization | I/R | Phase 1; continue validating |
| Database constraints | I | Phase 1 |
| Query performance | I | Phase 1 query-count work |
| Test design | I | Needs broader financial coverage |
| Docker | I | Phase 1 |
| CI/release | I | Needs more release-safety practice |
| Financial domain modeling | N | Phase 2 |
| Decimal/money semantics | N | Phase 2 |
| Timezone/date modeling | A | Phase 2 target |
| Atomic business operations | N | Future accounts/transfers |
| Idempotency | N | Future import |
| Observability | A | Future production maturity |
| Incident debugging | A | Future simulations |
| ADR/design communication | A | Phase 2 |
| API design | N/A | Later |
| React | N/A | Later learning phase |
| Open Finance | N/A | Future R&D |

---

## Bug journal

For meaningful bugs, record:

```text
Bug:
Symptom:
Root cause:
Why I initially missed it:
How I proved the cause:
Regression test:
Lesson:
```

Do not log every typo.

---

## Review-pattern journal

When the same code-review issue appears more than once:

```text
Pattern:
Examples:
Why it happens:
New personal checklist item:
```

The goal is to stop repeating the same class of mistake.

---

## Promotion criteria

### Junior I → Junior II

Evidence should show:

- can implement a ticket without step-by-step guidance;
- proposes reasonable tests before coding;
- consistently enforces ownership;
- explains model/query decisions;
- responds well to review findings;
- can diagnose ordinary bugs.

### Junior II → Junior III

Evidence should show:

- handles ambiguous requirements;
- proposes safe migrations;
- reasons about transaction boundaries;
- notices performance/data-integrity risks;
- can write small ADRs;
- investigates production-like incidents;
- anticipates rollback/operational consequences.

Promotion is based on evidence, not elapsed time.
