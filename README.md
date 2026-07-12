flowchart LR

  %% Course roots
  DM[Discrete Mathematics] --> GT[Graph Theory]
  C[MAT1001 Calculus] --> CAL[Calculus and Analysis Habits]
  LA[MAT1002 / MAT2LAL Linear Algebra] --> LALG[Linear Algebra Core]
  CS[Programming Support] --> COMP[Computational Experiments]

  %% Graph theory branch
  GT --> HAND[Handshaking Lemma]
  GT --> SEVEN[Seven Bridges Problem]
  GT --> PATH[Paths and Connectivity]
  GT --> EULER[Euler Circuit]
  GT --> HAMP[Hamilton Path]
  GT --> HAMC[Hamilton Cycle]
  GT --> CUT[Cut-edge and Connectivity]
  GT --> CLIQUE[Clique and Complement]
  GT --> CART[Cartesian Product of Graphs]
  GT --> AM[Adjacency Matrix]

  %% Trigger node
  AM --> GTRIGGER[Graph Trigger: structure becomes matrix]

  %% Linear algebra bridge
  LALG --> IP[Inner Products]
  LALG --> ORTH[Orthogonality]
  LALG --> EIG[Eigenvalues and Eigenvectors]
  LALG --> ESP[Eigenspaces]
  LALG --> GRAM[Gram Matrices]
  LALG --> PSD[Positive Semidefinite Matrices]

  AM --> EIG
  EIG --> SGT[Spectral Graph Theory]
  ESP --> SGT
  GRAM --> GEOM[Geometric Configurations]

  %% Spectral graph route
  SGT --> SRG[Strongly Regular Graphs]
  SRG --> SE[Spectral Embeddings]
  SE --> SC[Spherical Codes]
  SC --> IPSET[Inner Product Sets]
  IPSET --> TA[T-avoiding Codes]
  TA --> LP[Linear Programming Bounds]
  LP --> UO[Universal Optimality]

  %% Calculus branch
  CAL --> LIMIT[Limits and Continuity]
  CAL --> DER[Derivatives]
  CAL --> ROLLE[Rolle's Theorem]
  ROLLE --> MVT[Lagrange Mean Value Theorem]
  MVT --> CMVT[Cauchy Mean Value Theorem]
  MVT --> TAYLOR[Taylor's Theorem]
  TAYLOR --> TAP[Taylor Approximation]
  CAL --> OPT1[One-variable Optimization]

  %% Calculus trigger
  ROLLE --> CTRGL[Calculus Trigger: local flatness implies global structure]

  %% Analysis to energy route
  TAP --> APPROX[Approximation]
  OPT1 --> OPT[Optimization Language]
  CAL --> PF[Potential Functions]
  PF --> EM[Energy Minimization]
  APPROX --> LP
  OPT --> LP
  EM --> UO

  %% Computation support
  COMP --> MATRIX[Matrix Computation]
  COMP --> GSPEC[Graph Spectra]
  COMP --> VIS[Visualization]
  MATRIX --> AM
  GSPEC --> SGT
  VIS --> SE

  %% Styling
  classDef course fill:#f7f7f7,stroke:#555,stroke-width:1px;
  classDef trigger fill:#fff3cd,stroke:#b58900,stroke-width:2px;
  classDef research fill:#e8f0fe,stroke:#3367d6,stroke-width:1.5px;
  classDef theorem fill:#fce8e6,stroke:#c5221f,stroke-width:1.5px;
  classDef graph fill:#e6f4ea,stroke:#137333,stroke-width:1.5px;

  class DM,C,LA,CS course;
  class GTRIGGER,CTRGL trigger;
  class SRG,SE,SC,TA,LP,UO research;
  class ROLLE,MVT,CMVT,TAYLOR theorem;
  class HAND,SEVEN,PATH,EULER,HAMP,HAMC,CUT,CLIQUE,CART,AM graph;
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

## 平行世界&谢谢

中国的同学我羡慕你们wwwwww 
在大陆高校每个工科生都能在大一自动获得数学大礼包，高数线代数分一应俱全，而不是像我一样学线性代数都要求免先修审批（哭）
想把我分身去大陆的大学接受高压的数学训练。感谢华中师范大学和上海交通大学，以及中国科学技术大学的几位学姐学妹学长让我看到了中国大陆工科生与数学交互的路径。
身为在澳大利亚高校探索数学的计算机工科生，她们对我的选课，建筑数学修读计划起到了极大的作用。
