# PRODUCT.md — Personal Finance Manager

## 1. Product vision

Build a private personal-finance platform that begins as a simple expense manager and evolves gradually into a complete financial-management system.

Long-term vision:

> A self-hostable personal financial platform capable of consolidating financial operations, accounts and cards; handling installments and invoices; classifying spending; managing budgets and goals; forecasting cash flow; tracking net worth; importing data; and eventually integrating with Open Finance through an appropriate provider or compliant integration boundary.

The product must grow in capability as the developer grows in engineering maturity.

---

## 2. Product strategy

Do not build the final platform immediately.

Evolution:

1. Expense Manager
2. Monthly Financial Control
3. Accounts and Transfers
4. Credit Cards and Invoices
5. Budgets, Goals and Forecasting
6. File Import and Reconciliation
7. Net Worth / Assets / Liabilities
8. Mature Self-Hosting and Operations
9. Open Finance R&D
10. Real Open Finance integration if feasible

Each stage should create real technical pressure that motivates the next architectural concept.

---

## 3. Current stage — V1 Expense Manager

### Product goal

Allow a user to answer:

1. How much money came in during a period?
2. How much money went out during a period?
3. Where did the money go?
4. What was the financial result for that period?

### Primary user

Initially a single personal user, but all data ownership rules must remain correct for multi-user behavior.

---

## 4. V1 scope

### Authentication

- Login.
- Logout.
- Protected financial views.
- Each user can access only their own financial records.

### Transactions

A user can:

- register income;
- register an expense;
- view a transaction;
- edit a transaction;
- cancel or otherwise remove a transaction according to the domain decision made in Sprint 0;
- list transactions.

A transaction needs enough information to support:

- owner;
- type (`income` / `expense`);
- description;
- monetary amount;
- transaction date;
- optional category;
- optional notes;
- status if the Sprint 0 domain decision adopts cancellation rather than destructive delete;
- creation/update timestamps where useful.

Do not use floating-point numbers for money.

### Categories

- User-defined categories.
- Categories are private to the owner.
- User can create, rename and manage categories.
- Category behavior regarding income vs expense should be deliberately decided during implementation rather than assumed prematurely.

Examples:

- Food
- Housing
- Transport
- Leisure
- Subscriptions
- Salary
- Freelance

### Filters

Transaction history should support useful combinations of:

- date or period;
- type;
- category;
- simple text search if it remains within reasonable V1 scope.

### Monthly/history view

The user can navigate historical periods and see:

- income total;
- expense total;
- result;
- spending by category;
- transactions belonging to that period.

### Dashboard

V1 dashboard should remain simple:

- income for selected/current month;
- expenses for selected/current month;
- result;
- transaction count;
- spending by category;
- recent transactions if useful.

Do NOT add forecasts, assets, cards or advanced analytics to V1.

---

## 5. V1 non-goals

Explicitly out of V1:

- bank accounts;
- transfers;
- credit cards;
- invoices;
- installments;
- recurring transactions;
- budgets;
- goals;
- forecasting;
- net worth;
- investments;
- loans;
- CSV imports;
- OFX imports;
- Open Finance;
- automatic categorization;
- alerts;
- Celery;
- Redis;
- React as a requirement;
- microservices.

A non-goal may be revisited only through planning/product refinement.

---

## 6. UX principles

The UI can initially use Django templates.

Priorities:

- quick data entry;
- clear money formatting;
- clear income vs expense distinction;
- obvious selected period;
- easy correction of mistakes;
- clear empty states;
- useful validation messages;
- responsive enough for basic mobile use if achievable without derailing backend learning.

Visual polish is secondary to correctness and usability in early releases.

---

## 7. Financial semantics

V1 intentionally has a simple domain:

- `income` increases the period result;
- `expense` decreases the period result;
- only active/valid transactions count toward totals;
- categories organize transactions;
- V1 does not model bank balances.

The system must not pretend that V1 transaction totals equal real account balances.

This distinction becomes important when accounts and cards are added later.

---

## 8. Future product stages

### Stage 2 — Monthly control

Possible features:

- recurring income;
- recurring expenses;
- monthly budgets;
- planned transactions;
- basic alerts.

New engineering themes:

- recurrence;
- planned vs actual;
- date generation;
- periodic jobs only if genuinely needed.

### Stage 3 — Accounts

Possible features:

- checking;
- savings;
- cash;
- account balances;
- account-scoped transaction history;
- transfers.

New engineering themes:

- multi-movement operations;
- atomicity;
- consistency;
- account balance semantics.

### Stage 4 — Credit cards

Possible features:

- cards;
- purchase date;
- closing date;
- due date;
- installments;
- invoices;
- invoice payments;
- refunds;
- card limit.

New engineering themes:

- debt vs expense;
- billing cycles;
- double-count prevention;
- date boundaries;
- installment generation;
- reversals.

### Stage 5 — Planning

Possible features:

- budgets by category;
- savings goals;
- cash-flow projections;
- alerts;
- "available to spend" concepts.

New engineering themes:

- forecasting rules;
- scheduled commitments;
- explainable calculations.

### Stage 6 — Import

Possible features:

- CSV;
- OFX;
- import preview;
- reconciliation;
- deduplication;
- categorization rules.

New engineering themes:

- parsers;
- idempotency;
- normalization;
- import batches;
- rollback;
- failure reporting.

### Stage 7 — Net worth

Possible features:

- assets;
- liabilities;
- investments;
- historical net worth.

### Stage 8 — Operations

Possible features:

- hardened home server;
- encrypted backups;
- restore drills;
- monitoring;
- audit history;
- stronger authentication;
- dependency/update policy.

### Stage 9 — Open Finance R&D

Study:

- OAuth 2.0;
- OIDC;
- FAPI;
- PKCE where applicable;
- mTLS;
- consent;
- tokens/scopes;
- provider architecture;
- sandbox/mock specs.

### Stage 10 — Real integration

Only after security and architecture are mature.

The core finance domain must not be coupled to a single bank or provider.

---

## 9. Success criteria for the first usable release

The V1 is useful when the user can use it for a full month and reliably answer:

- total income;
- total expenses;
- spending by category;
- month result;
- what individual transactions produced those totals.

Correctness is more important than feature count.
