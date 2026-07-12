# Notebook Plan — SRG Spectral Embedding

This is a plan for a future computational notebook.

## Step 1 — Choose a graph

Pick a small graph with known regular structure.

## Step 2 — Build adjacency matrix

Represent the graph as a matrix `A`.

## Step 3 — Compute spectrum

Compute eigenvalues and eigenspaces of `A`.

## Step 4 — Choose eigenspace

Use one nontrivial eigenspace for vertex coordinates.

## Step 5 — Normalize

Normalize embedded vectors so they lie on a unit sphere.

## Step 6 — Compute inner products

Compute all `x_i · x_j` for distinct vertices.

## Step 7 — Summarize

Create a table:

| Inner product | Frequency |
|---|---|
| | |

## Step 8 — Test T-avoiding intervals

Choose intervals between observed inner product values and test whether the configuration avoids them.

## Step 9 — Energy experiments

Compute pairwise energy for simple potentials.

## Final output

A short note explaining how graph structure became a spherical point configuration.
