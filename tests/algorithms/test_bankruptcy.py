import pytest

from game_theory.algorithms.bankruptcy import *
from game_theory import NegativeNumberException


def test_constrained_equal_awards_two_person_equal():
    claims = [50, 60]
    asset = 50
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [25, 25]
    assert r == 25


def test_constrained_equal_awards_two_person_unequal():
    claims = [50, 24]
    asset = 50
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [26, 24]
    assert r == 26


def test_constrained_equal_awards_three_person_equal():
    claims = [50, 24, 68]
    asset = 60
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [20, 20, 20]
    assert r == 20


def test_constrained_equal_awards_three_person_unequal():
    claims = [50, 24, 68]
    asset = 75
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [25.5, 24, 25.5]
    assert r == 25.5


def test_constrained_equal_awards_same_allocation():
    claims = [50, 24, 68, 80]
    asset = 1000
    allocations, r = constrained_equal_awards(claims, asset)

    assert allocations == [50, 24, 68, 80]
    assert r == 80


def test_constrained_equal_awards_non_negative_asset():
    with pytest.raises(NegativeNumberException, match="Asset cannot be a negative number."):
        claims = [50, 24, 68]
        asset = -25
        constrained_equal_awards(claims, asset)


def test_constrained_equal_awards_non_negative_claims():
    with pytest.raises(NegativeNumberException, match="Claims cannot be a negative number."):
        claims = [50, -24, 68]
        asset = 25
        constrained_equal_awards(claims, asset)


def test_constrained_equal_losses_two_person_equal_loss_1():
    claims = [60, 90]
    asset = 100
    allocations, r = constrained_equal_losses(claims, asset)
    assert allocations == [35, 65]
    assert r == 25


def test_constrained_equal_losses_two_person_equal_loss_2():
    claims = [50, 100]
    asset = 100
    allocations, r = constrained_equal_losses(claims, asset)
    assert allocations == [25, 75]
    assert r == 25


def test_constrained_equal_losses_two_person_equal_loss_3():
    claims = [40, 80]
    asset = 100
    allocations, r = constrained_equal_losses(claims, asset)
    assert allocations == [30, 70]
    assert r == 10


def test_constrained_equal_losses_two_person_unequal_loss():
    claims = [450, 50]
    asset = 100
    allocations, r = constrained_equal_losses(claims, asset)
    assert allocations == [100, 0]
    assert r == 350


def test_constrained_equal_losses_three_person_unequal_loss():
    claims = [50, 100, 150]
    asset = 100
    allocations, r = constrained_equal_losses(claims, asset)
    assert allocations == [0, 25, 75]
    assert r == 75


def test_constrained_equal_losses_three_person_same_allocation():
    claims = [50, 100, 150]
    asset = 300
    allocations, r = constrained_equal_losses(claims, asset)
    assert allocations == [50, 100, 150]
    assert r == 0


def test_constrained_equal_losses_non_negative_asset():
    with pytest.raises(NegativeNumberException, match="Asset cannot be a negative number."):
        claims = [50, 24, 68]
        asset = -25
        constrained_equal_losses(claims, asset)


def test_constrained_equal_losses_non_negative_claims():
    with pytest.raises(NegativeNumberException, match="Claims cannot be a negative number."):
        claims = [50, -24, 68]
        asset = 25
        constrained_equal_losses(claims, asset)
