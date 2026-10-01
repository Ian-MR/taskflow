# CONTRIBUTING.md — Junior Simulation Workflow

## 1. Roles

### Junior Backend Developer
The human developer:

- owns implementation;
- creates branches;
- writes code;
- writes tests;
- investigates bugs;
- explains technical decisions;
- performs self-review;
- responds to code-review findings.

### Codex
Codex acts as senior support according to `AGENTS.md`.

It should not become the primary implementer.

---

## 2. Branch workflow

Start from updated `main`.

Suggested format:

```bash
git checkout main
git pull
git checkout -b feat/FIN-001-short-description
```

Branch prefixes:

- `feat/`
- `fix/`
- `refactor/`
- `chore/`
- `docs/`
- `test/`

Keep branches scoped to one ticket when practical.

---

## 3. Commit style

Use meaningful semantic commits.

Examples:

```text
feat: add transaction creation flow
fix: scope category lookup to current user
test: cover cross-user transaction access
refactor: extract monthly totals queryset
docs: record transaction deletion decision
chore: configure phase 2 project files
```

Avoid:

```text
update
fix
changes
final
more changes
```

---

## 4. Before coding

For non-trivial tickets, provide a short implementation proposal to the senior:

- understanding;
- likely files/layers affected;
- data-model impact;
- edge cases;
- test plan.

Do not produce a formal design document for trivial CRUD unless the decision has real architectural consequences.

---

## 5. Local Definition of Ready

A ticket is ready when:

- business objective is understandable;
- acceptance criteria are testable;
- major dependencies are known;
- open product questions are resolved or explicitly listed.

---

## 6. Before opening a PR

Run the repository checks.

Typical baseline:

```bash
ruff check .
ruff format --check .
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Use the project-specific commands if they differ.

Also perform self-review:

- Did I satisfy every acceptance criterion?
- Did I add unnecessary abstractions?
- Is ownership enforced?
- Are money/date rules correct?
- Could a failure leave inconsistent data?
- Did I accidentally commit secrets or real financial data?
- Are migrations intentional?
- Is the diff focused?

---

## 7. Pull request expectations

The PR description should explain:

- what changed;
- why;
- how to test;
- design decisions;
- risks;
- migration/deploy impact;
- screenshots only when UI changes benefit from them.

Do not write "works" as the test plan.

---

## 8. Review response

For each blocking finding:

1. understand the concern;
2. ask if unclear;
3. change the code yourself;
4. add or adjust a regression test where appropriate;
5. reply with what changed and why.

Do not blindly apply reviewer suggestions without understanding them.

A reviewer suggestion is not automatically correct.

---

## 9. Merge policy

Prefer merge only when:

- CI is green;
- P0/P1 findings are resolved;
- acceptance criteria are satisfied;
- migration/deployment concerns are understood.

Squash merge is preferred when intermediate branch commits are noisy.

---

## 10. Release policy

Use tags for meaningful product milestones.

Do not tag every merged ticket.

Examples:

```text
v0.2.0 — Finance phase foundation
v0.3.0 — First transaction management release
v0.4.0 — Categories and filtering
v0.5.0 — Monthly dashboard
```

Exact versions may change during planning.

---

## 11. Data safety

Never commit:

- `.env`;
- database credentials;
- bank exports;
- real transaction CSV/OFX files;
- production database dumps;
- access/refresh tokens;
- Open Finance credentials;
- encryption keys.

Fixtures and screenshots used in development must use synthetic data unless explicitly sanitized.

---

## 12. Documentation

Update documentation when a change affects:

- how to run the project;
- environment variables;
- deployment;
- architecture;
- significant domain semantics;
- operational recovery.

Use ADRs for significant choices, not for routine code changes.
