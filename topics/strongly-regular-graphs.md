# Strongly Regular Graphs

## Definition

A strongly regular graph with parameters `(v, k, lambda, mu)` has:

- `v` vertices,
- every vertex has degree `k`,
- every adjacent pair has `lambda` common neighbors,
- every non-adjacent pair has `mu` common neighbors.

## Why they matter

Strongly regular graphs sit at a useful intersection of graph theory, linear algebra, combinatorics, and spherical geometry.

Their adjacency matrices have a small number of eigenvalues, which makes them suitable for spectral embeddings.

## Research bridge

```mermaid
flowchart LR
  SRG[Strongly Regular Graph] --> A[Adjacency Matrix]
  A --> E[Three Eigenvalues]
  E --> S[Spectral Embeddings]
  S --> C[Spherical Code]
  C --> T[T-avoiding Conditions]
```

## Core questions

- Why does a strongly regular graph have only three adjacency eigenvalues?
- Which eigenspace gives a useful embedding?
- How do adjacent and non-adjacent pairs translate into inner products?
- When does the resulting code satisfy useful T-avoiding conditions?

## Mini-goal

Be able to take one small strongly regular graph, compute its spectrum, build a spectral embedding, and calculate its inner product distribution.
