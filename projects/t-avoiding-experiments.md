# Mini-project — T-avoiding Code Experiments

## Project question

How does changing a forbidden inner product interval `T` affect small spherical code experiments?

## Scope

This is exploratory and computational. It is meant to build intuition before attempting proofs.

## Possible experiments

- Start with a small point configuration on a circle or sphere.
- Compute all pairwise inner products.
- Choose several forbidden intervals.
- Check whether the configuration is T-avoiding.
- Compute simple pairwise energies.
- Compare how the constraints change the feasible set.

## Useful potentials

- `h(t) = exp(t)`
- `h(t) = 1 / (1 - t)` where defined
- simple polynomial potentials

## Output

- a table of inner products
- a table of T-avoiding status
- a short explanation of what changes as `T` changes

## Main learning goal

Develop intuition for forbidden-distance constraints before studying full LP bound proofs.
