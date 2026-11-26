import pytest

from fraction import Fraction


# ---------- 2.1: Initialiser ----------

@pytest.mark.parametrize(
    "numerator, denominator, expected",
    [
        (2, 4, (1, 2)),     # reduced to lowest terms
        (3, 1, (3, 1)),     # already in lowest terms
        (1, -2, (-1, 2)),   # sign moved to the numerator
        (-2, -4, (1, 2)),   # two negatives give a positive fraction
        (0, 5, (0, 1)),     # zero is stored as 0/1
    ],
)
def test_init_lowest_terms_and_sign(numerator: int, denominator: int, expected: tuple[int, int]) -> None:
    """Fractions are stored in lowest terms, with the sign in the numerator."""
    f = Fraction(numerator, denominator)
    assert (f.numerator, f.denominator) == expected


def test_init_default_denominator() -> None:
    """The denominator defaults to 1."""
    f = Fraction(3)
    assert (f.numerator, f.denominator) == (3, 1)


def test_zero_denominator_raises() -> None:
    """A denominator of 0 raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 0)


@pytest.mark.parametrize(
    "numerator, denominator",
    [(1.5, 2), (1, "2"), (True, 2), (1, None)],
)
def test_non_integer_raises(numerator: object, denominator: object) -> None:
    """Values that are not integers (including bool) raise TypeError."""
    with pytest.raises(TypeError):
        Fraction(numerator, denominator)


def test_attributes_are_read_only() -> None:
    """numerator and denominator cannot be changed after creation."""
    f = Fraction(1, 2)
    with pytest.raises(AttributeError):
        f.numerator = 5
    with pytest.raises(AttributeError):
        f.denominator = 5


# ---------- 2.1: Comparisons ----------

def test_equal_and_not_equal() -> None:
    """Equal values are equal even if written differently."""
    assert Fraction(1, 2) == Fraction(2, 4)
    assert not Fraction(1, 2) != Fraction(2, 4)
    assert Fraction(1, 2) != Fraction(1, 3)
    assert not Fraction(1, 2) == Fraction(1, 3)


def test_ordering() -> None:
    """<, <=, > and >= give the correct result."""
    small, big = Fraction(1, 3), Fraction(1, 2)
    assert small < big and not big < small
    assert small <= big and big >= small
    assert big > small and not small > big
    assert Fraction(1, 2) <= Fraction(2, 4)  # equal values
    assert Fraction(1, 2) >= Fraction(2, 4)


def test_ordering_negative() -> None:
    """Comparisons also work for negative fractions."""
    assert Fraction(-1, 2) < Fraction(1, 3)
    assert Fraction(-1, 2) < Fraction(-1, 3)
    assert Fraction(1, -2) == Fraction(-1, 2)


def test_sorting() -> None:
    """A list of fractions can be sorted."""
    fractions = [Fraction(3, 4), Fraction(-1, 2), Fraction(1, 3)]
    assert sorted(fractions) == [Fraction(-1, 2), Fraction(1, 3), Fraction(3, 4)]


def test_compare_with_other_types() -> None:
    """Comparing with something that is not a Fraction."""
    assert Fraction(1, 2) != 0.5
    assert not Fraction(1, 2) == 0.5
    with pytest.raises(TypeError):
        Fraction(1, 2) < 1


# ---------- 2.2: Other special methods ----------
# TODO (2.2): Tests for the arithmetic methods go here.
