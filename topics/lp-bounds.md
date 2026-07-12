# Linear Programming Bounds

## Core idea

A linear programming bound uses a carefully chosen polynomial to prove that no configuration can beat a certain limit.

## Proof skeleton

1. Choose a polynomial `f(t)`.
2. Force `f(t)` to have the correct sign on allowed inner products.
3. Expand `f(t)` in a sphere-appropriate orthogonal polynomial basis.
4. Check signs of coefficients.
5. Use positivity to obtain a bound.
6. Show a known configuration attains the bound.

## Why this matters

This turns an optimization problem into a certificate problem. Instead of searching over all configurations, one proves that a bound must hold for all of them.

## Key vocabulary

- polynomial certificate
- Gegenbauer expansion
- positive definiteness
- moment
- design condition
- cardinality bound
- energy bound

## Study target

The first goal is not to reproduce every coefficient. The first goal is to understand why a polynomial can certify optimality.
