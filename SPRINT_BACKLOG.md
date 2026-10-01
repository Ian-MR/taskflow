# SPRINT_BACKLOG.md — Initial Phase 2 Backlog

This file intentionally contains only the first two sprints.

Do not pre-generate the entire multi-month roadmap. Future tickets should be created as the product and developer evolve.

---

# Sprint 0 — Product Pivot and Engineering Foundation

## Sprint goal

Convert the repository from a completed Django learning project into the foundation of a personal Expense Manager without implementing the full finance feature set.

Focus on product/domain decisions, project hygiene and a safe transition from the TaskFlow domain.

---

## FIN-001 — Establish the Phase 2 product baseline

**Type:** Chore / Product

**Priority:** High

### Context

The repository is pivoting from TaskFlow into a personal Expense Manager while preserving the Phase 1 history/tag.

### Acceptance criteria

- Phase 2 project documents are committed.
- Existing Phase 1 release/tag remains preserved.
- README clearly explains the new product direction.
- The developer can explain what belongs in V1 and what is deliberately excluded.
- No finance feature implementation is required by this ticket.

### Learning focus

Product scope, repository history and incremental evolution.

---

## FIN-002 — Decide how the legacy TaskFlow domain will be retired

**Type:** Architecture / Refactor planning

**Priority:** High

### Context

The existing Project/Task business domain is unrelated to personal finance.

### Acceptance criteria

- The developer proposes how legacy models/apps/routes/templates will be removed or isolated.
- Migration/data consequences are considered.
- The decision preserves the Phase 1 release in Git history.
- A short ADR is created only if the decision has meaningful lasting consequences.
- No unrelated redesign is introduced.

### Learning focus

Product pivots, migration safety, codebase cleanup.

---

## FIN-003 — Define V1 transaction semantics

**Type:** Domain design

**Priority:** High

### Context

V1 requires income and expense records, but money, signs, cancellation/deletion and reporting semantics must be unambiguous.

### Questions to resolve

- Is `amount` stored as positive with a separate type, or signed?
- Which decimal precision is supported?
- Is currency fixed to BRL in V1?
- Can a transaction be deleted, canceled, or both?
- Which date defines the reporting period?
- Does category remain optional?

### Acceptance criteria

- Decisions are documented.
- Invalid states can be described clearly.
- The model design does not attempt to solve credit cards/accounts/Open Finance yet.
- The developer can explain trade-offs.

### Learning focus

Domain modeling and financial correctness.

---

## FIN-004 — Define V1 category semantics

**Type:** Domain design

**Priority:** Medium

### Context

Categories are user-defined and private.

### Questions to resolve

- Can one category be used for both income and expenses?
- Is category name unique per user?
- What happens to transactions when a category is removed?
- Is uncategorized allowed?

### Acceptance criteria

- Category ownership is explicit.
- Deletion behavior is explicit.
- Naming/uniqueness behavior is explicit.
- Decision remains simple enough for V1.

---

## FIN-005 — Phase 2 security and data-handling baseline

**Type:** Security / Operations

**Priority:** High

### Acceptance criteria

- Development/test/staging use synthetic financial data.
- `.gitignore` covers likely financial exports and local secrets.
- Production secrets remain environment-based.
- The developer documents when real financial data is allowed to enter the system.
- A backup/security review is explicitly required before real financial data is used.

### Learning focus

Privacy and threat awareness.

---

## FIN-006 — Confirm engineering baseline after pivot

**Type:** Engineering

**Priority:** Medium

### Acceptance criteria

- Test suite passes after Sprint 0 changes.
- Lint/format checks pass.
- Migration check passes.
- Production image still builds.
- CI remains green.
- Obsolete TaskFlow-only docs/settings are removed or updated.

---

# Sprint 1 — Transactions and Categories

## Sprint goal

Deliver the first core financial workflow:

> A user can maintain private categories and record income/expense transactions safely.

Dashboard and advanced filtering are not the sprint goal unless planning explicitly brings a small part forward.

---

## FIN-101 — Create private user categories

**Type:** Feature

**Priority:** High

### Business context

Users need personalized categories to organize financial activity.

### Acceptance criteria

- Authenticated user can create a category.
- User can list their own categories.
- Category ownership is enforced server-side.
- Invalid category data is rejected.
- Cross-user access is covered by tests.
- Category semantics follow FIN-004 decisions.

### Out of scope

- automatic categorization;
- color/icon systems unless trivial;
- shared/global categories.

---

## FIN-102 — Manage existing categories

**Type:** Feature

**Priority:** Medium

### Acceptance criteria

- User can rename/manage their own category.
- User cannot mutate another user's category.
- Remove/delete behavior follows FIN-004 decision.
- Existing transaction consistency is preserved.
- Tests cover affected behavior.

---

## FIN-103 — Record an expense

**Type:** Feature

**Priority:** High

### Acceptance criteria

- Authenticated user can record an expense.
- Amount/date/description rules follow FIN-003.
- Category selection cannot reference another user's private category.
- Invalid monetary values are rejected.
- Expense is visible only to owner.
- Tests include money validation and authorization.

### Out of scope

- account balance;
- credit card;
- recurrence;
- import.

---

## FIN-104 — Record income

**Type:** Feature

**Priority:** High

### Acceptance criteria

- Authenticated user can record income.
- Domain rules match FIN-003.
- Income is distinguished unambiguously from expense.
- Ownership rules are enforced.
- Relevant tests exist.

---

## FIN-105 — List user transactions

**Type:** Feature

**Priority:** High

### Acceptance criteria

- User sees only their own transactions.
- List contains enough information to understand each record.
- Default ordering is intentional and documented in code/tests where appropriate.
- Canceled/removed records behave according to FIN-003.
- Query count is reasonable.

---

## FIN-106 — View and edit a transaction

**Type:** Feature

**Priority:** Medium

### Acceptance criteria

- User can inspect a transaction.
- User can edit permitted fields.
- Cross-user access is impossible.
- Editing cannot attach another user's category.
- Validation remains consistent with creation.
- Tests cover ownership and invalid edits.

---

## FIN-107 — Cancel/delete a transaction

**Type:** Feature

**Priority:** Medium

### Acceptance criteria

- Behavior follows FIN-003 decision.
- Financial records do not silently remain in totals when they should be excluded.
- Authorization is enforced.
- Tests cover reporting-relevant behavior.

---

## FIN-108 — Sprint 1 quality pass

**Type:** Quality

**Priority:** High

### Acceptance criteria

- CI green.
- No unresolved P0/P1 review findings.
- Key ownership tests exist.
- Monetary behavior is tested.
- Migration history is reviewed.
- Developer performs a full self-review.
- Senior PR review returns APPROVE or only non-blocking comments before release.

---

# Not yet scheduled

These are intentionally NOT Sprint 1 tickets:

- dashboard;
- monthly totals;
- filters;
- recurring transactions;
- accounts;
- cards;
- imports;
- React;
- DRF;
- Open Finance.

They will be refined after Sprint 1 based on what the codebase actually needs.
