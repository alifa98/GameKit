"""
Module for implementing classical auction mechanisms from game theory.
"""

from game_theory import NegativeNumberException


def first_price_auction(bids):
    """
    First-Price Sealed-Bid Auction:
    Highest bidder wins and pays their bid.

    Args:
        bids (list): A list of non-negative bids (floats or ints).

    Returns:
        winner (int): Index of the winning bidder.
        price (float): Price paid (equal to winning bid).
    """
    if not bids:
        raise ValueError("Bids list cannot be empty.")

    if any(b < 0 for b in bids):
        raise NegativeNumberException("Bids must be non-negative.", bids)

    winner = max(range(len(bids)), key=lambda i: bids[i])
    return winner, bids[winner]


def second_price_auction(bids):
    """
    Second-Price (Vickrey) Sealed-Bid Auction:
    Highest bidder wins and pays the second-highest bid.

    If the winner is not unique, the winner is the last bidder index with the highest bid.

    Args:
        bids (list): A list of non-negative bids.

    Returns:
        winner (int): Index of winning bidder.
        price (float): Price paid (second-highest bid).
    """
    if not bids:
        raise ValueError("Bids list cannot be empty.")

    if any(b < 0 for b in bids):
        raise NegativeNumberException("Bids must be non-negative.", bids)

    sorted_bids = sorted(((bid, i) for i, bid in enumerate(bids)), reverse=True)
    highest_bid, winner = sorted_bids[0]
    second_highest_bid = sorted_bids[1][0] if len(bids) > 1 else 0.0

    return winner, second_highest_bid


def generalized_second_price_auction(bids, slots):
    """
    Generalized Second-Price Auction (e.g., search ads).

    Args:
        bids (list): A list of non-negative bids (CPC).
        slots (list): A list of slot click-through rates (CTR), descending order.

    Returns:
        allocation (list of tuples): (bidder index, assigned slot, price per click).
    """
    if not bids or not slots:
        raise ValueError("Bids and slots must be non-empty lists.")

    if any(b < 0 for b in bids):
        raise NegativeNumberException("Bids must be non-negative.", bids)

    if any(s < 0 for s in slots):
        raise NegativeNumberException("Slots must be non-negative.", slots)

    if len(bids) < len(slots):
        slots = slots[: len(bids)]

    sorted_bidders = sorted(((bid, i) for i, bid in enumerate(bids)), reverse=True)
    allocation = []

    for j, (slot_ctr) in enumerate(slots):
        if j >= len(sorted_bidders):
            break
        _, bidder = sorted_bidders[j]
        next_bid = sorted_bidders[j + 1][0] if j + 1 < len(sorted_bidders) else 0.0
        price = next_bid  # Pay the bid of the next highest bidder
        allocation.append((bidder, j, price))

    return allocation
