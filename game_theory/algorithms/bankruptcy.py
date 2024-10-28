"""
Module for division rules for solving bankruptcy problems.
"""

from game_theory import NegativeNumberException


def constrained_equal_awards(claims, asset):
    """
    Calculate allocations using the constrained equal awards method.
    If the asset is larger than the sum of claims, returns the claims list itself.

    Args:
        claims (list): A list of claims. Each element of the list is a non-negative float number.
        asset (float): The total amount of available assets. This is a non-negative number.

    Raises:
        NegativeNumberException: Claims cannot be a negative number.

    Returns:
        list: A list of allocations.
        float: The r value in the equation a_i = min(r, c_i). If the sum of claims is less than the asset,
        then the r-value is the maximum claim value.
    """

    if any(c < 0 for c in claims):
        raise NegativeNumberException(
            "Claims cannot be a negative number.", claims)

    if asset < 0:
        raise NegativeNumberException(
            "Asset cannot be a negative number.", asset)

    # sum of claims is less than the asset (no bankruptcy)
    if sum(claims) <= asset:
        return claims, max(claims)

    equal_alloc = asset / len(claims)

    if all(c >= equal_alloc for c in claims):
        return [equal_alloc for _ in range(len(claims))], equal_alloc

    r = min(claims)
    allocations = [r for _ in range(len(claims))]

    while asset > sum(allocations):
        remained_claims = [c - r for c in claims]
        r_prime = min(c for c in remained_claims if c > 0)
        positive_remained_claim_length = len(
            [c for c in remained_claims if c > 0])

        if asset - (sum(allocations) + r_prime * positive_remained_claim_length) < 0:
            r_prime = (asset - sum(allocations)) / \
                positive_remained_claim_length

        allocations = [alloc + r_prime if remained > 0 else alloc for alloc,
                       remained in zip(allocations, remained_claims)]
        r += r_prime

    return allocations, r


def CEA(claims, asset):
    """
    Calculate allocations using the constrained equal awards method.

    Args:
        claims (list): A list of claims. Each element of the list is a non-negative float number.
        asset (float): The total amount of available assets. This is a non-negative number.

    Raises:
        NegativeNumberException: Claims cannot be a negative number.

    Returns:
        list: A list of allocations.
        float: The r value in the equation a_i = min(r, c_i). If the sum of claims is less than the asset,
        then the r-value is the maximum claim value.
    """
    return constrained_equal_awards(claims, asset)


def constrained_equal_losses(claims, asset):
    """
    Calculate allocations using the constrained equal losses method.
    If the asset is larger than the sum of claims, returns the claims list itself.

    Raises:
        NegativeNumberException: Claims cannot be a negative number.

    Returns:
        list: A list of allocations.
        float: The r value in the equation a_i = max(0, c_i-r). If the sum of claims is less than the asset,
        then the r-value is 0.
    """

    # checks
    if any(c < 0 for c in claims):
        raise NegativeNumberException(
            "Claims cannot be a negative number.", claims)

    if asset < 0:
        raise NegativeNumberException(
            "Asset cannot be a negative number.", asset)

    total_loss = sum(claims) - asset

    if total_loss <= 0:
        return claims, 0

    equal_loss = total_loss / len(claims)

    if all(c >= equal_loss for c in claims):
        return [c - equal_loss for c in claims], equal_loss

    r = min(claims)
    losses = [r for _ in range(len(claims))]

    while total_loss > sum(losses):
        remained_claims = [c - r for c in claims]
        r_prime = min(c for c in remained_claims if c > 0)
        positive_remained_claim_length = len(
            [c for c in remained_claims if c > 0])

        if total_loss - (sum(losses) + r_prime * positive_remained_claim_length) < 0:
            r_prime = (total_loss - sum(losses)) / \
                positive_remained_claim_length

        losses = [alloc + r_prime if remained > 0 else alloc for alloc,
                  remained in zip(losses, remained_claims)]
        r += r_prime

    return [claim - loss for claim, loss in zip(claims, losses)], r
