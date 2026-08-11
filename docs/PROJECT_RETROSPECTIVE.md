# CTAPS Project Retrospective

## Outcome

CTAPS reached a functional prototype stage but was not adopted as the department's operational contract-ranking system. Stakeholder review established that the immediate business requirement was considerably simpler than the architecture that had been developed.

That outcome is the most important part of this project.

CTAPS demonstrates a distinction that is easy to lose during rapid development: **a technically successful implementation can still be the wrong product.**

## The original design

CTAPS was conceived as a multi-stage contract-prioritization and monitoring framework:

```text
OpenGov data
    ↓
Lite Ranking
    ↓
Advanced Assessment
    ↓
Final CTAPS Index
    ↓
Management Review
    ↓
Monitoring Level / Time Allocation
```

The architecture attempted to combine objective database fields with structured human judgment. It included automated Excel generation, controlled assessment inputs, weighted scoring, review flags, management overrides, monitoring levels, and cadence recommendations.

Each element was defensible on its own. Together, however, they created a system substantially more elaborate than the stakeholder's immediate operational requirement.

## The central failure: concept continuation

One of the most important lessons from CTAPS was not a Python or Excel problem. It was a requirements and context-management problem.

During development, a simplified **Lite** concept emerged. The intended simplification should have triggered a clean architectural decision: determine whether Lite was still a component of CTAPS or whether it had become an independent solution with a new specification.

That separation did not happen clearly enough.

Instead, the new Lite concept continued to inherit assumptions from the larger CTAPS architecture. Simplification occurred *inside the existing conceptual framework* rather than beginning from a clean requirements model. Lite remained an input into the Advanced Assessment and Final CTAPS Index, and the surrounding system continued to grow around it.

This is an example of what I call **concept continuation**.

## Concept continuation in vibe coding

AI-assisted or "vibe" coding makes it possible to move from an idea to functioning software remarkably quickly. The same conversational continuity that makes this productive can also become a source of architectural inertia.

A conversational development system has context. Earlier requirements, terminology, formulas, and architectural decisions remain available and can influence subsequent generations. When a requirement changes, merely asking the AI to "make this simpler" does not necessarily invalidate the assumptions that produced the previous design.

The result can be dangerous precisely because it remains coherent: the AI may continue generating technically consistent code for a conceptual model that no longer represents the business problem.

In CTAPS, the Lite concept changed, but its relationship to the rest of the system was not explicitly reset. The old architecture therefore continued exerting influence on later prompts and implementation decisions.

## The practical rule

When requirements materially change:

> **Do not merely modify the prompt. Reset the specification.**

A specification reset should explicitly identify:

1. What requirement changed?
2. Which previous assumptions remain valid?
3. Which assumptions are now deprecated?
4. Which existing components must no longer influence the new design?
5. Is the new concept a revision of the existing system or a new system that should begin from first principles?

This creates a conceptual boundary that ordinary conversational continuation does not provide automatically.

## Why this matters more with AI-assisted development

Traditional software development can also suffer from scope creep and obsolete assumptions. AI-assisted development changes the velocity.

When implementation takes minutes instead of days, there is less natural friction forcing the developer to stop and reconsider the architecture. A plausible idea can become code before the underlying requirement has been sufficiently challenged.

That changes the developer's job. The bottleneck moves away from syntax and toward:

- requirement definition,
- model selection,
- assumption management,
- validation,
- and knowing when to discard an elegant solution.

CTAPS taught me that faster implementation requires more deliberate conceptual governance.

## What worked

Despite the scope mismatch, several design choices remain useful:

- **Explainability:** CTAPS exposed scores and factors rather than producing an unexplained ranking.
- **Human review:** uncertain classifications and incomplete assessments could be flagged rather than silently resolved.
- **Separation of objective and subjective inputs:** database-derived information and employee judgment were treated differently.
- **Management override:** the proposed operating model preserved human authority over final prioritization.
- **Prototype velocity:** Python, Flask, pandas, openpyxl, and AI-assisted development made it possible to explore a fairly sophisticated workflow rapidly.

## What I would do differently

I would begin with the smallest stakeholder-approved decision model and require explicit approval before adding another layer.

The revised sequence would be:

```text
Business question
    ↓
Minimum required data
    ↓
Simplest defensible scoring rule
    ↓
Stakeholder validation
    ↓
Working prototype
    ↓
Only then: additional sophistication
```

I would also create a short versioned requirements document at every major conceptual pivot. If a new requirement invalidated an earlier architecture, the new version would explicitly state that the previous architecture was no longer authoritative.

## Final assessment

CTAPS was not deployed, but I do not consider the project wasted work.

It produced a functioning prototype, forced difficult questions about explainable prioritization, and revealed a development failure that would have been easy to hide. Preserving that failure is useful because it documents something a polished success story cannot: **how requirements drift interacts with conversational AI and rapid implementation.**

The lasting lesson from CTAPS is therefore not "avoid complexity." Complexity can be appropriate.

The lesson is:

> **Earn complexity from validated requirements. Do not inherit it from conversational momentum.**
