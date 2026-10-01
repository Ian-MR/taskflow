# ARCHITECTURE.md — Phase 2 Baseline

## 1. Architectural goal

Keep the system simple enough for a junior developer to understand end-to-end while maintaining professional boundaries that allow the product to evolve.

Current default architecture:

> **Django modular monolith + PostgreSQL + server-rendered UI**

Docker, CI and the existing production/deployment learning setup remain part of the engineering baseline.

Do not add infrastructure without a concrete requirement.

---

## 2. Current system shape

```text
Browser
   |
   v
Django URLs
   |
   v
Views
   |
   +--> Forms / validation
   |
   +--> domain/application logic where needed
   |
   +--> QuerySets / Models
             |
             v
         PostgreSQL
```

The exact module structure should evolve with real needs.

---

## 3. Suggested initial domain boundary

A dedicated finance-oriented Django app or cohesive set of apps should replace the old TaskFlow business domain over time.

Do not preserve Project/Task abstractions simply because they already exist.

The final app split for V1 should be chosen deliberately.

Possible simple starting point:

```text
finance/
    models.py
    forms.py
    views.py
    urls.py
    querysets.py     # only if useful
    services.py      # only if useful
    tests/
```

Another split may be chosen if justified.

The architecture document deliberately does not mandate a large app hierarchy yet.

---

## 4. Layer responsibilities

### Models

Use models for:

- persisted domain state;
- model-level invariants where appropriate;
- small domain behavior closely tied to an entity;
- relationships;
- database constraints.

Avoid making models a dumping ground for every operation.

### QuerySets / Managers

Use when query semantics repeat or when ownership/filtering should be made explicit.

Examples of useful semantics:

- records owned by a user;
- active transactions;
- transactions within a period;
- aggregate data for a dashboard.

Avoid trivial wrappers that hide a single obvious `.filter()` with no reuse or semantic value.

### Forms

Use for:

- input validation;
- normalization of user-provided data;
- form-specific rules;
- rendering integration for Django server-rendered UI.

Do not trust browser validation alone.

### Views

Views coordinate HTTP.

They should:

- read request data;
- call forms/querysets/domain logic;
- enforce access rules;
- choose response/redirect/template.

Avoid long business workflows inside views.

### Services

Introduce only when there is a real application operation that:

- coordinates multiple models;
- has non-trivial business steps;
- benefits from a transaction boundary;
- is reused;
- becomes difficult to understand inside a view/model.

A service module is not mandatory.

### Templates

Templates present data.

Do not place non-trivial business rules or data-access logic in templates.

---

## 5. Ownership and authorization

Financial records are private.

All object access must be scoped to the current owner whenever data is user-owned.

Correct pattern conceptually:

```text
request.user
    |
    v
owned queryset
    |
    v
object lookup
```

Do not:

1. fetch object globally by numeric id;
2. check ownership only after exposing related data;
3. rely on hiding links in the UI.

Authorization must be enforced server-side.

---

## 6. Money

Never use binary floating point for stored money.

Use decimal semantics.

Decisions that must eventually be explicit:

- maximum amount precision;
- currency support;
- sign convention;
- whether `amount` is always positive with a separate type or signed;
- rounding behavior.

V1 may support only BRL if that keeps the domain simpler.

If a money decision has long-term consequences, document it in an ADR.

---

## 7. Time and dates

Finance is date-sensitive.

V1 transaction date should mean the date the financial event belongs to for reporting.

Do not casually substitute `created_at` for financial date.

The project should make a deliberate timezone decision before card billing cycles, recurring rules or forecasts are introduced.

For Brazilian personal-finance use, timezone behavior must be explicit rather than inherited accidentally from defaults.

---

## 8. Transaction status / deletion

Financial history should not be deleted casually once the product begins storing real information.

V1 must decide one of:

- allow destructive deletion while the product is still a basic private tracker;
- use a status such as active/canceled;
- introduce a simple audit/reversal rule.

Do not implement an elaborate accounting ledger merely to future-proof V1.

Document the chosen trade-off.

---

## 9. Database rules

Use database constraints for invariants that must remain true regardless of input path.

Examples that may become appropriate:

- owner is required;
- amount rules;
- allowed type/status values;
- uniqueness rules;
- foreign-key behavior.

Indexes should be added because a query pattern justifies them, not preemptively on every column.

---

## 10. Testing architecture

Prefer behavior-oriented tests.

Initial test areas should eventually include:

```text
tests/
    test_models.py
    test_forms.py
    test_views.py
    test_permissions.py
    test_queries.py
```

Exact files depend on the chosen app layout.

High-value financial tests include:

- owner isolation;
- totals;
- decimal behavior;
- boundary dates;
- canceled/ignored transaction exclusion;
- category ownership;
- invalid values;
- dashboard query behavior.

Keep a small number of end-to-end flows; rely more heavily on targeted integration tests around Django + PostgreSQL.

---

## 11. Infrastructure baseline

Keep the existing principles:

```text
GitHub
   |
   v
CI
   |
   +--> lint
   +--> format
   +--> Django checks
   +--> migrations check
   +--> tests
   +--> production image build
   |
   v
GHCR / deployment artifact
```

Early cloud deployment may use synthetic data only.

Real financial data should move to a hardened environment only after a production-readiness review.

---

## 12. Docker

Docker remains part of the project.

Local development may use:

- Django container;
- PostgreSQL container;
- persistent database volume;
- bind mount for source where appropriate.

Production should not assume that local bind mounts or development conveniences exist.

Do not introduce Redis/Celery until the product has asynchronous/background work that justifies them.

---

## 13. Future API and React boundary

Later:

```text
React + TypeScript
       |
       v
Django REST API
       |
       v
Finance domain
       |
       v
PostgreSQL
```

The REST API should expose product semantics, not leak arbitrary model internals.

Do not design every V1 model around hypothetical frontend API requirements.

---

## 14. Future import boundary

Desired conceptual flow:

```text
Manual   CSV   OFX   Open Finance
   \      |     |       /
    \     |     |      /
       Normalization
            |
            v
      Finance domain
```

Provider-specific payloads must not become the core domain model.

This abstraction should be introduced when the first real import source appears.

---

## 15. Architecture decision records

Use ADRs for decisions with meaningful long-term trade-offs.

Location:

`docs/adr/`

Candidates over the life of the product:

- transaction amount/sign convention;
- delete vs cancel/reverse;
- timezone policy;
- account/transfer source of truth;
- invoice semantics;
- background-job mechanism;
- self-hosting exposure model;
- Open Finance provider boundary;
- React migration strategy.
