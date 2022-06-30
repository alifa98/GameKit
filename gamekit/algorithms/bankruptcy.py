

"""
division rules for solving bankruptcy problem.
"""

from gamekit import NegativeNumberException


def constrained_equal_awards(claims: list, asset: float) -> list:
    """
    This function returns a list of allocations based onthe constrained equal allocation method.
    If the asset is larger than the sum of claims, returns the claims list itself.

    See: https://en.wikipedia.org/wiki/Constrained_equal_awards

    Parameters:
        claims (list): list of claims (list of non-negative float numbers)

    Returns:
        list: list of allocations
        r: the r value in the $a_i = min(r, c_i) $ (if sum of claims become less than asset, then the r-value would be the asset itself.)
    """

    # checks
    if any(c < 0 for c in claims):
        raise NegativeNumberException("Claims cannot be a negative number.")

    if asset < 0:
        raise NegativeNumberException("Asset cannot be a negative number.")

    if(sum(claims) <= asset):
        return claims, asset
    else:

        equal_alloc = asset/len(claims)

        if all(c >= equal_alloc for c in claims):
            return [equal_alloc for c in range(len(claims))], equal_alloc

        else:
            r = min(claims)
            allocations = [r for i in range(len(claims))]

            while(asset > sum(allocations)):

                remained_claims = [c - r for c in claims]

                # r_prime: the next best amount to to allocate to all
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
