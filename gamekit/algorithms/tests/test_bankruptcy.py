import pytest

from gamekit.algorithms.bankruptcy import *
from gamekit import NegativeNumberException


def test_two_person_equal():
    claims = [50, 60]
    asset = 50
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [25, 25]
    assert r == 25


def test_two_person_unequal():
    claims = [50, 24]
    asset = 50
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [26, 24]
    assert r == 26


def test_three_person_equal():
    claims = [50, 24, 68]
    asset = 60
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [20, 20, 20]
    assert r == 20


def test_three_person_unequal():
    claims = [50, 24, 68]
    asset = 75
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [25.5, 24, 25.5]
    assert r == 25.5

def test_same_allocation():
    claims = [50, 24, 68, 80]
    asset = 1000
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [50, 24, 68, 80]
    assert r == 80


def test_non_negative_asset():
    with pytest.raises(NegativeNumberException, match="Asset cannot be a negative number."):
        claims = [50, 24, 68]
        asset = -25
        allocations, r = constrained_equal_awards(claims, asset)


def test_non_negative_asset():
    with pytest.raises(NegativeNumberException, match="Claims cannot be a negative number."):
        claims = [50, -24, 68]
        asset = 25
        allocations, r = constrained_equal_awards(claims, asset)
