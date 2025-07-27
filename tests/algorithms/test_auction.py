import pytest

from game_theory import NegativeNumberException
from game_theory.algorithms.auction import (
    first_price_auction,
    generalized_second_price_auction,
    second_price_auction,
)


# Tests for first_price_auction
def test_first_price_auction_positive():
    assert first_price_auction([1, 5, 3]) == (1, 5)


def test_first_price_auction_edge_all_equal():
    assert first_price_auction([2, 2, 2]) == (0, 2)


def test_first_price_auction_edge_single_bidder():
    assert first_price_auction([10]) == (0, 10)


def test_first_price_auction_error_empty():
    with pytest.raises(ValueError):
        first_price_auction([])


def test_first_price_auction_error_negative_bid():
    with pytest.raises(NegativeNumberException):
        first_price_auction([5, -2, 3])


# Tests for second_price_auction
def test_second_price_auction_positive():
    assert second_price_auction([4, 6, 2]) == (1, 4)


def test_second_price_auction_edge_all_equal():
    # the winner is the last bidder with the highest bid
    assert second_price_auction([3, 3, 3]) == (2, 3)


def test_second_price_auction_edge_single_bidder():
    assert second_price_auction([8]) == (0, 0)


def test_second_price_auction_error_empty():
    with pytest.raises(ValueError):
        second_price_auction([])


def test_second_price_auction_error_negative_bid():
    with pytest.raises(NegativeNumberException):
        second_price_auction([1, -3, 2])


# Tests for generalized_second_price_auction
def test_gspa_positive():
    assert generalized_second_price_auction([10, 9, 8], [0.5, 0.3]) == [
        (0, 0, 9),
        (1, 1, 8),
    ]


def test_gspa_edge_one_slot():
    assert generalized_second_price_auction([7], [0.4]) == [(0, 0, 0)]


def test_gspa_edge_extra_bidders():
    assert generalized_second_price_auction([9, 6, 4], [0.5]) == [(0, 0, 6)]


def test_gspa_error_empty_bids():
    with pytest.raises(ValueError):
        generalized_second_price_auction([], [0.5])


def test_gspa_error_negative_slot():
    with pytest.raises(NegativeNumberException):
        generalized_second_price_auction([5], [-0.1])

