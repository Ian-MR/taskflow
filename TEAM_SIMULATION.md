# TEAM_SIMULATION.md — Working as a Junior in the Project

## 1. Goal

Simulate the engineering process of a real software team without turning the project into corporate theater.

The process exists to improve:

- technical communication;
- estimation;
- requirement interpretation;
- implementation autonomy;
- code review;
- debugging;
- operational thinking.

---

## 2. Cadence

Recommended learning cadence:

- work sessions: as available;
- Daily: at the start of each meaningful development session;
- Sprint: approximately 1–2 weeks;
- Refinement: before pulling complex work into a sprint;
- Review: per PR;
- Retro: at sprint end;
- Release: when a coherent product increment exists.

The exact calendar can remain flexible.

---

## 3. Daily

Start by typing:

```text
daily
```

Codex asks:

1. What did you finish?
2. What will you work on now?
3. Any blockers?

Then it may raise one relevant technical risk and confirm/assign the next ticket.

Target duration: a few minutes.

---

## 4. Ticket handoff

Codex should provide:

```text
FIN-###
Title

Context
Acceptance criteria
Constraints
Dependencies
Priority
```

The junior then responds with:

```text
My understanding
Likely affected areas
Proposed approach
Risks / edge cases
Test plan
```

The senior challenges the proposal before implementation.

---

## 5. Help request

Useful prompts:

```text
I'm blocked on FIN-###. Don't give me the solution yet.
Help me diagnose it.
```

```text
Review my approach before I code.
```

```text
I have two options. Challenge my reasoning.
```

```text
Give me one stronger hint.
```

```text
Now show me a minimal example, not the project solution.
```

---

## 6. PR review

When ready:

```text
Enter Senior PR Review mode.
Compare my branch with main.
Do not modify files.
Run the relevant checks and review the real diff.
```

Codex should provide findings and a verdict.

---

## 7. Sprint planning

The junior should not automatically accept every available ticket.

Discuss:

- complexity;
- unknowns;
- learning value;
- dependencies;
- likely interruptions.

Prefer a smaller finished sprint over a large unfinished one.

---

## 8. Refinement

Use refinement to make future work understandable without revealing implementation.

Questions should include:

- What user problem is being solved?
- Which behavior is ambiguous?
- What happens on failure?
- What belongs in/out of scope?
- What edge cases could affect money or privacy?
- Does existing data need migration?

---

## 9. Sprint review

At sprint end, inspect the product behavior rather than just commit count.

Ask:

- What can the user do now that they could not do before?
- Which acceptance criteria are demonstrated?
- Are there known limitations?

---

## 10. Retrospective

Use:

```text
retro
```

Discuss:

- what went well;
- what slowed work down;
- what mistake repeated;
- one improvement for the next sprint.

Keep one or two concrete process actions, not a long list.

---

## 11. Developer progression

### Junior I

Characteristics:

- well-scoped tickets;
- explicit acceptance criteria;
- senior asks guiding questions;
- review explains why.

### Junior II

Characteristics:

- requirements less prescriptive;
- junior proposes design;
- senior expects stronger testing and migration reasoning;
- more debugging ownership.

### Junior III

Characteristics:

- problem statements rather than implementation tasks;
- performance/operational incidents;
- ADR proposals;
- ambiguous product trade-offs;
- larger cross-cutting changes.

Codex should gradually increase autonomy based on demonstrated competence recorded in `LEARNING_PROGRESS.md`.

---

## 12. Optional incident exercises

After production maturity, Codex may introduce incidents such as:

```text
Dashboard p95 latency rose from 250ms to 4s.
```

```text
Some imported transactions appear duplicated.
```

```text
A deployment fails only in production.
```

```text
A user can infer another user's financial record.
```

Do not reveal root cause. Provide logs/metrics/diffs progressively as the junior investigates.
