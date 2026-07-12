# Mini-project — Spectral Embeddings of Small Strongly Regular Graphs

## Project question

How do small strongly regular graphs produce spherical codes through their eigenspaces?

## Inputs

- a small strongly regular graph
- its adjacency matrix
- eigenvalues and eigenspaces

## Expected outputs

- graph parameters
- adjacency spectrum
- selected eigenspace
- embedded vertex coordinates
- inner product set
- distance distribution
- possible forbidden intervals `T`
- sample energy values for simple potentials

## Method sketch

```mermaid
flowchart LR
  G[Choose a graph] --> A[Build adjacency matrix]
  A --> E[Compute eigenvalues]
  E --> V[Choose eigenspace]
  V --> X[Embed vertices]
  X --> IP[Compute inner products]
  IP --> T[Identify possible T-avoiding intervals]
  T --> EN[Compute sample energies]
```

## Beginner-level success criterion

A successful first version does not need to prove a theorem. It only needs to reproduce the pipeline cleanly for one example.

## Possible notebook structure

1. Define graph.
2. Build adjacency matrix.
3. Compute spectrum.
4. Select eigenspace.
5. Normalize embedded points.
6. Compute pairwise inner products.
7. Summarize the inner product distribution.
8. Test simple forbidden intervals.
9. Compute sample energy values.

## Research-facing value

This project connects graph theory, linear algebra, computation, spherical codes, and energy-style optimization.
