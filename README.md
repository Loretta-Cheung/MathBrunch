# Mathematics Roadmap

This repository is a public, anonymized learning roadmap. It tracks how course mathematics grows into research-facing mathematics, with a special focus on the bridge:

```mermaid
flowchart LR
  DM[Discrete Mathematics] --> GT[Graph Theory]
  LA[MAT1002 Linear Algebra] --> SGT[Spectral Graph Theory]
  GT --> SRG[Strongly Regular Graphs]
  SGT --> SRG
  SRG --> SE[Spectral Embeddings]
  SE --> SC[Spherical Codes]
  SC --> TA[T-avoiding Codes]
  TA --> LP[Linear Programming Bounds]
  LP --> UO[Universal Optimality]

  C[MAT1001 Calculus] --> PF[Potential Functions]
  PF --> EM[Energy Minimization]
  EM --> UO
```

## Current semester

- `MAT1001`: Calculus foundation, analysis habits, Taylor approximation, and one-variable optimization. This course is currently part of the plan, but may be withdrawn if a prerequisite waiver is granted for `MAT2LAL`.

- `MAT1002`: Linear algebra foundation, including inner products, eigenvalues, eigenspaces, orthogonality, and Gram matrices.

- `MAT2LAL`: Advanced linear algebra pathway. If enrolled, this course will become the main bridge toward spectral graph theory, graph embeddings, and research-facing mathematical structures.

- Discrete mathematics background: Graph theory, paths, connectivity, combinatorial reasoning, and proof style.

- Programming support: Computational experiments with matrices, graph spectra, spectral embeddings, and visualization.

## Repository purpose

This is not only a study log. It is a trace of how mathematical interests become research directions.

The repository has two layers:

1. **Knowledge Map** — mathematical dependencies and conceptual structure.
2. **Footprint Trace** — when and why a concept became personally meaningful.

## Privacy rule

This public version intentionally avoids real names, private emails, private institutions, mentor identities, and personal identifiers. Research-facing content is described by topic, not by person.

Use labels such as:

- `target research area`
- `research mentor`
- `recent reading`
- `spherical codes project`
- `spectral graph theory bridge`

Do not use real names, emails, screenshots, private messages, or identifiable personal stories.

## Quick navigation

- [Roadmap](roadmap.md)
- [Footprint Trace](trace.md)
- [Glossary](notes/glossary.md)
- [Questions](notes/questions.md)
- [Reading Log](notes/reading-log.md)
- [Mini-project: SRG spectral embeddings](projects/srg-spectral-embeddings.md)

## Weekly workflow

1. Add short notes under `progress/`.
2. Add new questions to `notes/questions.md` or as GitHub Issues.
3. When a concept becomes meaningful, create a new file in `footprints/`.
4. If a topic becomes stable, summarize it under `topics/`.
5. Run the privacy checker before publishing:

```bash
python scripts/privacy_check.py
```

## Minimal update ritual

```text
Learned → Understood well → Still unclear → Connection to research bridge → Next action
```

Keep the system alive, not perfect.
