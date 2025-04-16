# GameKit

[![PyTests](https://github.com/alifa98/GameKit/actions/workflows/python-testrun.yml/badge.svg)](https://github.com/alifa98/GameKit/actions/workflows/python-testrun.yml)
[![Publish Python Package](https://github.com/alifa98/GameKit/actions/workflows/publish.yml/badge.svg)](https://github.com/alifa98/GameKit/actions/workflows/publish.yml)

## What is this?

This is a python package for game theory-related algorithms.

## How can I install this?

```bash
pip install gameTheory
```

Usage:

```python
from game_theory.algorithms.bankruptcy import constrained_equal_losses

# Example: Constrained Equal Losses
claims = [60, 90]
asset = 100
allocations, r = constrained_equal_losses(claims, asset)
print(allocations, r)
# Output: [35.0, 65.0] 25.0
```

Note: Currently, this repository is under development.

## What do you mean by a library for game theory?

In game theory, we deal with problems like finding equilibrium, evolutionarily stable strategies, stable matching, fair division, bankruptcy, voting, etc. In this package, we are implementing the algorithms proposed for these problems. For example, a function that finds the stable matching for marriage problem with the Gale-Shapley algorithm.

## Can I contribute to this repository?

We would be glad if you contributed to this package even by creating an issue and requesting a new feature. You are always welcome to make a bug report, open an improvement suggestion issue, or send pull requests. Moreover, you can implement the `new feature` issues that [have not been assigned](https://github.com/alifa98/GameKit/issues?q=is%3Aissue+is%3Aopen+no%3Aassignee) and send pull requests.
Also look at the [TODO](todo.md) list for the next features or improvements.

## Where can I find the theory behind the algorithms?

- [Game Theory, Alive](https://homes.cs.washington.edu/~karlin/GameTheoryBook.pdf)
- Any other game theory book

## Build and Test

To build the package, you can use the following command:

```bash
python3 -m build
```

To test the package, you can use the following command:

```bash
pytest
```

## How can I contact you?

You can open a new discussion in this repository's [Discussion](https://github.com/alifa98/GameKit/discussions) section for any question.

If you want to contact us by email, you can send your feedback, question, proposal, or requests to <ali@faraji.info>
