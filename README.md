# CTAPS — Contract Time Allocation and Priority System

> **The point is not to automate judgment. The point is to focus judgment where it matters most.**

CTAPS was an AI-assisted prototype designed to help a municipal contract-compliance team prioritize a large contract portfolio using transparent scoring, structured employee assessment, and management review.

The project began with a legitimate operational problem: not every contract can receive the same level of attention. Contracts differ in financial exposure, service criticality, public visibility, safety consequences, compliance risk, and vendor performance. CTAPS attempted to convert those differences into a defensible monitoring plan.

## What CTAPS did

The proposed workflow had four stages:

1. **Lite Ranking** — rapid triage using contract-title indicators and budget exposure.
2. **Advanced Assessment** — structured employee input on operational risk and impact.
3. **Final Ranking** — a weighted 0–100 CTAPS index, subject to management review.
4. **Time Allocation** — monitoring cadence and workload guidance derived from the final level.

The working Flask application supports three core workflows:

- Process an uploaded workbook through the Lite Ranking engine.
- Generate an Advanced Assessment workbook with controlled employee-response fields.
- Process a completed Advanced Assessment and calculate the final CTAPS ranking.

## Scoring architecture

### Lite Ranking

The Lite model used visible database information already available to the organization:

```text
Lite Score = (Service Importance Points × 2) + Budget Points
```

Service importance was inferred from contract-title keywords and intentionally weighted more heavily than budget so that a lower-dollar essential service would not automatically be treated as low priority.

### Advanced Assessment

The original proposal expanded the model with operational factors including service criticality, safety impact, legal/contractual risk, health impact, vendor performance, public visibility, strategic alignment, schedule criticality, renewal status, insurance/compliance concerns, service type, funding source, and departmental accountability.

The implemented prototype later consolidated the Advanced Assessment into five weighted judgment factors:

- Service Criticality — 25%
- Health or Safety Impact — 25%
- Legal or Compliance Risk — 20%
- Schedule or Renewal Urgency — 15%
- Strategic or Public Impact — 15%

The final implemented formula was:

```text
Final CTAPS Index = (Normalized Lite Score × 25%) + (Assessment Index × 75%)
```

The result was converted into one of four monitoring levels with a corresponding review cadence.

## Why CTAPS was not deployed

CTAPS was technically viable, but stakeholder review showed that the proposed architecture substantially exceeded the complexity of the department's immediate need. Management ultimately wanted a much simpler High / Medium / Low contract-risk classification based primarily on readily available contract data.

That mismatch was useful. It exposed a requirements-management failure that is especially important in AI-assisted development: **concept continuation**.

During development, a simplified "Lite" concept emerged. However, the new Lite requirement was never explicitly severed from the assumptions of the larger CTAPS architecture. Instead of being redesigned as an independent solution, Lite continued to behave as the first stage of CTAPS. Earlier assumptions therefore persisted into later prompts, scoring logic, and implementation decisions even after the operational requirement had changed.

See **[Project Retrospective](docs/PROJECT_RETROSPECTIVE.md)** for the full discussion of this failure mode and its implications for vibe coding.

## What I learned

CTAPS became more valuable as an engineering case study than as a deployed product. The project demonstrated several lessons:

- Technical sophistication is not the same as requirement fit.
- Rapid AI-assisted development makes specification discipline more—not less—important.
- When requirements materially change, the specification should be explicitly reset rather than incrementally patched.
- Human-review flags and transparent scoring are valuable controls for explainable decision-support systems.
- A prototype can succeed technically while still being the wrong operational product.

## Technology

- Python
- Flask
- pandas
- openpyxl
- HTML / CSS
- Excel workbook generation

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── app.py
│   ├── ctaps_engine.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
└── docs/
    ├── PROJECT_RETROSPECTIVE.md
    ├── CTAPS_PROPOSAL.md
    └── CTAPS_PRESENTATION_OUTLINE.md
```

## Status

**Portfolio archive / prototype. Not deployed.**

CTAPS is preserved here because the design, code, presentation, and retrospective document an important part of the development process: how a strong technical solution can overshoot a simpler business requirement, and how conversational AI can reinforce obsolete architectural assumptions unless the developer deliberately resets the specification.
