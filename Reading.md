# Reading Log: Graph Theory and Spherical Codes

> This file records my reading progress, conceptual milestones, and motivation trace while studying graph theory and its bridge into spherical codes, spectral graph theory, and optimization-style mathematics.  
> The purpose is not only to track what has been read, but also to record how graph theory becomes connected to linear algebra, spectral embeddings, spherical codes, T-avoiding configurations, and future research preparation.

---

## Reading status

| Item | Status |
|---|---|
| Main book | *Graph Theory*, Second Edition |
| Book author | Douglas B. West |
| Research-facing paper | *Universal Optimality of T-avoiding Spherical Codes and Designs* |
| Main areas | Graph theory, spectral graph theory, spherical codes, linear programming bounds |
| Current purpose | Build a rigorous graph theory foundation and connect it to spectral embeddings, spherical configurations, and optimization-style proof methods |
| Started | 2026 |
| Current status | Active reading |

> Public-note rule: this file tracks learning content only. It intentionally avoids private names, personal identifiers, and unnecessary biographical details.

---

## Why this book matters

This book is being used as the main graph theory backbone for my mathematics roadmap.

The current learning path is:

```mermaid
flowchart LR
  DM[Discrete Mathematics] --> GT[Graph Theory]
  GT --> P[Paths and cycles]
  GT --> C[Connectivity]
  GT --> M[Matchings and colorings]
  GT --> E[Extremal graph theory]
  GT --> LA[Linear algebra connection]
  LA --> AM[Adjacency matrices]
  AM --> SGT[Spectral graph theory]
  SGT --> SRG[Strongly regular graphs]
  SRG --> SE[Spectral embeddings]
  SE --> SC[Spherical codes]
  SC --> TA[T-avoiding configurations]
  TA --> UO[Universal optimality]
```

The central idea is that graph theory is not being studied as an isolated subject. It is the discrete-structure side of a broader route:

```text
Graph structure → Matrix representation → Spectral embedding → Spherical configuration → Optimization / energy / universal bounds
```


---

## Research-facing paper

### *Universal Optimality of T-avoiding Spherical Codes and Designs*

This paper is included as a research-facing reading object. It is not being read as a fully mastered paper yet. Its current role is to show where the graph theory and linear algebra route can eventually lead.

The paper introduces and studies spherical codes whose inner products avoid a forbidden set `T`. It connects several themes:

- spherical codes
- spherical designs
- forbidden inner products
- potential energy minimization
- linear programming bounds
- universally optimal configurations
- strongly regular graphs
- spectral embeddings

The most important bridge for the current roadmap is:

```mermaid
flowchart LR
  GT[Graph theory] --> RG[Regular graphs]
  RG --> SRG[Strongly regular graphs]
  SRG --> A[Adjacency matrix]
  A --> EV[Eigenvalues and eigenspaces]
  EV --> SE[Spectral embedding]
  SE --> SC[Spherical code]
  SC --> IP[Inner product set]
  IP --> T[T-avoiding condition]
  T --> LP[Linear programming bound]
  LP --> UO[Universal optimality]
```

### Why this paper matters

This paper gives a concrete destination for the current learning path.

Graph theory supplies the discrete objects.  
Linear algebra supplies matrices, eigenspaces, projections, and inner products.  
Spectral graph theory turns graphs into geometric point configurations.  
Spherical code theory studies those point configurations on spheres.  
Linear programming bounds provide certificates of optimality.  

The paper therefore helps turn course-level study into research-facing vocabulary.

### Current reading goal

The first pass is not about understanding every theorem.

The goal is to understand the following questions:

- What is a spherical code?
- What is an inner product set?
- What does `T-avoiding` mean?
- Why do forbidden inner products behave like forbidden distances?
- What does universal optimality mean?
- How do strongly regular graphs produce spherical codes?
- Why do linear programming bounds prove maximality or energy optimality?
- Which parts require linear algebra, graph theory, calculus, or orthogonal polynomials?

### Priority sections for first pass

| Section type | Priority | Purpose |
|---|---:|---|
| Abstract and introduction | High | Understand the main problem and vocabulary |
| Definitions of spherical codes and T-avoiding codes | High | Build the object language |
| General linear programming theorems | Medium | Understand the proof engine at a high level |
| Strongly regular graph section | Very high | Direct bridge from graph theory to spherical codes |
| Universal optimality results for graph-derived codes | Very high | Research-facing target |
| Technical appendices | Low for now | Return later only when needed |

### Concept bridge

| Paper concept | Current prerequisite |
|---|---|
| Spherical code | Inner products, vectors, geometry |
| T-avoiding condition | Sets, intervals, inner products |
| Spherical design | Polynomials, averages, moments |
| Energy minimization | Calculus and potential functions |
| Linear programming bound | Polynomial certificates and inequalities |
| Gegenbauer polynomials | Orthogonal polynomial background |
| Strongly regular graphs | Graph theory and adjacency matrices |
| Spectral embedding | Linear algebra and eigenspaces |

### Paper-reading footprint

**Footprint:** graph theory begins to connect to spherical geometry.

The motivating realization is that graph theory does not have to remain purely combinatorial. Through adjacency matrices and eigenspaces, a graph can become a geometric configuration. This creates a path from discrete structures to spherical codes, forbidden inner products, and universal optimality.

**Opened branch:** strongly regular graphs  
**Later connection:** spectral embeddings, spherical codes, T-avoiding configurations  
**Motivation trace:** a graph can become a point configuration, and a point configuration can become an optimization problem.


---

## Current semester connections

| Course / background | Connection to this reading |
|---|---|
| Discrete Mathematics | Provides the first formal exposure to graphs, proofs, paths, connectivity, and combinatorial reasoning |
| MAT1001 Calculus | Supports later ideas around potentials, energy, optimization, and approximation |
| MAT1002 Linear Algebra | Provides the matrix and eigenspace language needed to connect graph theory to spectral embeddings |
| Programming / computation | Supports experiments with adjacency matrices, graph spectra, and small examples |
| Research-facing paper | Provides the long-range target: graph-derived spherical codes, T-avoiding constraints, and universal optimality |

---

## Reading priorities

The whole book does not need to be mastered at once. The current priority is to build a clean path toward spectral graph theory and research-facing graph structures.

### Priority A — Core graph language

- Graphs, subgraphs, complements
- Degrees and degree sequences
- Paths, cycles, trails, walks
- Connectivity and cut-vertices
- Trees and spanning trees
- Bipartite graphs
- Planar graphs
- Matchings and coverings
- Coloring
- Extremal graph theory

### Priority B — Research bridge topics

- Regular graphs
- Graph complements
- Strongly regular graphs
- Adjacency matrices
- Eigenvalues of graphs
- Graph embeddings
- Distance and inner product structures
- Combinatorial designs and codes

### Priority C — Later / optional depth

- Advanced extremal results
- Algebraic graph theory beyond the first pass
- Deeper design theory
- Connections to coding theory
- Connections to spherical codes and linear programming bounds

---

## Chapter log

Use this section to track chapter-level progress.

| Chapter / section | Topic | Status | Notes |
|---|---|---|---|
| Ch. 1 | Fundamental concepts | To read | Build precise vocabulary |
| Ch. 2 | Trees and distance | To read | Important for structure and proof style |
| Ch. 3 | Matchings and factors | To read | Useful for combinatorial maturity |
| Ch. 4 | Connectivity and paths | To read | Strong connection to structural graph theory |
| Ch. 5 | Coloring | To read | Important for discrete constraints |
| Ch. 6 | Planar graphs | Optional | Useful but not the main research bridge |
| Ch. 7 | Edges and cycles | Optional | Return if needed |
| Ch. 8 | Algebraic methods | High priority later | Bridge to spectral graph theory |
| Ch. 9 | Extremal problems | Medium priority | Helps with proof culture and bounds |

---
## Paper log

Use this section to track progress through the research-facing paper.

| Part | Topic | Status | Notes |
|---|---|---|---|
| Abstract | T-avoiding spherical codes and designs | Started | Main vocabulary and target problems |
| Introduction | Problems and motivation | To reread | Connects codes, designs, energy, and LP methods |
| Definitions | Spherical codes, designs, energy, universal optimality | To summarize | Build a glossary |
| General LP theorems | Polynomial certificates | Later | Read for proof skeleton, not every coefficient |
| Strongly regular graphs | Spectral embeddings from graph structure | High priority | Best bridge from graph theory |
| Universal optimality section | Energy bounds and graph-derived codes | High priority | Research-facing destination |
| Appendix | Technical coefficient checks | Skip for now | Return only if needed |

---

## Footprint trace

This section records not only what was studied, but why it became meaningful.

### 2026-03 — Discrete Mathematics → Graph Theory

Graph theory first became visible through discrete mathematics. The important shift was realizing that mathematics can describe structure directly: paths, constraints, connectivity, and networks.

**Opened branch:** graph theory  
**Later connection:** adjacency matrices, spectral graph theory, strongly regular graphs  
**Motivation trace:** graph theory made mathematics feel structural rather than merely procedural.

---

### 2026-S2 — Linear Algebra → Graph Theory becomes spectral

Linear algebra is expected to turn graph theory from a purely combinatorial language into a spectral and geometric one.

**Opened branch:** adjacency matrices and eigenspaces  
**Later connection:** spectral embeddings of graphs  
**Motivation trace:** matrices may become the bridge between discrete structure and geometric configuration.

---

### Future footprint — Strongly regular graphs → Spherical codes

Strongly regular graphs are expected to become a key bridge topic: their adjacency matrices have highly controlled eigenvalue structure, and their spectral embeddings can produce spherical codes.

**Opened branch:** spectral graph theory  
**Later connection:** spherical codes, forbidden inner products, universal optimality  
**Motivation trace:** this is where graph theory may connect directly to current research-facing mathematics.


### 2026 — Research-facing paper → T-avoiding spherical codes

The paper on T-avoiding spherical codes and designs gives a concrete destination for the graph theory route. The key discovery is that forbidden graph-like structure can be translated into forbidden inner products on a sphere.

**Opened branch:** T-avoiding spherical codes  
**Later connection:** linear programming bounds, energy minimization, universal optimality  
**Motivation trace:** the same structural instinct behind graph theory appears again in geometry, where inner products and distances become constraints.

---

## Concept notes

### Graph

A graph is a set of vertices together with edges connecting pairs of vertices. The first goal is to become fluent with graph vocabulary and proof style.

### Path

A path records an ordered movement through distinct vertices. Paths are one of the first places where graph theory begins to feel like structure rather than calculation.

### Connectivity

Connectivity asks whether a graph stays in one piece and how robust that connectedness is. This is important for both theoretical graph structure and network-like intuition.

### Regular graph

A graph is regular if every vertex has the same degree. Regularity is a key step toward spectral graph theory because it gives the adjacency matrix a more controlled structure.

### Strongly regular graph

A strongly regular graph has a fixed number of vertices, a fixed degree, and fixed numbers of common neighbors for adjacent and non-adjacent vertex pairs. This creates a strong bridge between combinatorics, linear algebra, and geometry.

### Adjacency matrix

The adjacency matrix records graph structure as a matrix. This is the main bridge from graph theory to linear algebra.

### Spectral embedding

A spectral embedding uses eigenvectors or eigenspaces of a graph-related matrix to represent vertices as points in Euclidean space or on a sphere.

---

## Active questions

- How does the adjacency matrix encode the structure of a graph?
- Why do regular graphs have especially useful spectral properties?
- What makes strongly regular graphs so rigid?
- How does an eigenspace embedding turn graph vertices into points on a sphere?
- Why do adjacent and non-adjacent vertex pairs produce controlled inner products in some spectral embeddings?
- How can graph theory connect to spherical codes and energy-minimizing configurations?
- What exactly does universal optimality require?
- How does the T-avoiding condition change ordinary spherical code problems?
- Which strongly regular graph examples are small enough to reproduce computationally?
- What is the simplest polynomial certificate example I can understand completely?

---

## Mini-project ideas

### 1. Adjacency matrix experiments

Choose small graphs and compute:

- adjacency matrix
- degree sequence
- eigenvalues
- eigenvectors
- basic graph invariants

Possible examples:

- cycle graphs
- complete graphs
- complete bipartite graphs
- Petersen graph
- small regular graphs

---

### 2. Strongly regular graph notebook

Choose one small strongly regular graph and document:

- parameters
- adjacency matrix
- eigenvalues
- eigenspaces
- spectral embedding
- inner product distribution

Possible output:

```text
Graph → Adjacency matrix → Eigenvalues → Eigenspace → Spherical embedding → Inner product set
```

---

### 3. Reading-to-research note

Write a short note explaining how graph theory connects to:

- linear algebra
- spectral graph theory
- spherical codes
- forbidden-distance or forbidden-inner-product problems
- optimization and universal bounds


---

### 4. T-avoiding spherical code glossary

Build a small glossary from the research-facing paper.

Include:

- spherical code
- inner product set
- maximal cosine
- T-avoiding code
- spherical design
- potential energy
- absolutely monotone potential
- linear programming bound
- universal optimality

Goal:

```text
Definitions → one example → one question → one connection to graph theory
```

---

### 5. Strongly regular graph to spherical code example

Choose a small strongly regular graph and try to reproduce the bridge suggested by the paper.

Steps:

1. Write down the graph parameters.
2. Build or find the adjacency matrix.
3. Compute eigenvalues and eigenspaces.
4. Produce a spectral embedding.
5. Compute pairwise inner products.
6. Identify possible forbidden intervals.
7. Connect the example back to T-avoiding spherical codes.

---

## Weekly update template

Copy this template into the progress folder when needed.

```markdown
# Reading update: YYYY-MM-DD

## Sections read

-

## Main concepts

-

## What became clearer

-

## What is still unclear

-

## Connection to the roadmap

-

## Footprint / motivation trace

-

## Next actions

- [ ] 
- [ ] 
```

---

## Maintenance rule

This file should stay lightweight. Detailed notes can go into separate files under `topics/`, `courses/`, or `progress/`.

Suggested workflow:

1. Update this file when a new reading milestone appears.
2. Add detailed concept notes elsewhere.
3. Link important ideas back to the roadmap.
4. Record emotional or intellectual triggers in the footprint trace.
5. Keep all public-facing notes anonymous and focused on learning content.
