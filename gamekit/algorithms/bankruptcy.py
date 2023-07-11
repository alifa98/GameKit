"""
division rules for solving bankruptcy problem.
"""

from gamekit import NegativeNumberException


def constrained_equal_awards(claims, asset):
    """
    This function returns a list of allocations based on the constrained equal allocation method.
    If the asset is larger than the sum of claims, returns the claims list itself.

    See: https://en.wikipedia.org/wiki/Constrained_equal_awards

    Parameters:
        claims (list): list of claims (list of non-negative float numbers)
        asset (float): total amount of our assets (non-negative)
    Returns:
        list: list of allocations
        r: the r value in the $a_i = min(r, c_i) $ (if sum of claims become less than asset, then the r-value would be the largest claim value.)
    """

    # checks
    if any(c < 0 for c in claims):
        raise NegativeNumberException("Claims cannot be a negative number.")

    if asset < 0:
        raise NegativeNumberException("Asset cannot be a negative number.")

    if sum(claims) <= asset:
        return claims, max(claims)
    else:

        equal_alloc = asset / len(claims)

        if all(c >= equal_alloc for c in claims):
            return [equal_alloc for _ in range(len(claims))], equal_alloc

        else:
            r = min(claims)
            allocations = [r for _ in range(len(claims))]

            while asset > sum(allocations):

                remained_claims = [c - r for c in claims]

                # r_prime: the next best amount to allocate to all
                r_prime = min(c for c in remained_claims if c > 0)
                positive_remained_claim_length = len(
                    list(filter(lambda x: (x > 0), remained_claims))
                )

                if asset - (sum(allocations) + r_prime * positive_remained_claim_length) > 0:
                    for i in range(len(claims)):
                        if remained_claims[i] > 0:
                            allocations[i] += r_prime
                    r += r_prime
                else:
                    # there is not any limitation by claims, so we divide assets equally among remained claims
                    r_prime = (asset - sum(allocations)) / \
                              positive_remained_claim_length
                    for i in range(len(claims)):
                        if remained_claims[i] > 0:
                            allocations[i] += r_prime
                    r += r_prime

            return allocations, r


def CEA(claims, asset):
    """
    equal to the `constrained_equal_awards` function.
    """
    return constrained_equal_awards(claims, asset)


def constrained_equal_losses(claims, asset):
    """
    This function returns a list of allocations based on the constrained equal loss method.
    If the asset is larger than the sum of claims, returns the claims list itself.

    See: https://en.wikipedia.org/wiki/Constrained_equal_losses

    Parameters:
        claims (list): list of claims (list of non-negative float numbers)
        asset (float): total amount of our assets (non-negative)
    Returns:
        list: list of allocations
        r: the r value in the $a_i = max(0, c_i-r) $ (if sum of claims become less than asset, then the r-value would be 0.)
    """
    # checks
    if any(c < 0 for c in claims):
        raise NegativeNumberException("Claims cannot be a negative number.")

    if asset < 0:
        raise NegativeNumberException("Asset cannot be a negative number.")

    total_loss = sum(claims) - asset

    if total_loss <= 0:
        return claims, 0

    losses, r = constrained_equal_awards(claims, total_loss)

    return [claim - loss for claim, loss in zip(claims, losses)], r
