import math


class Fraction:
    """A fraction with an integer numerator and a strictly positive integer denominator."""

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        """
        Create a fraction in lowest terms, with the sign kept in the numerator.

        Args:
            numerator (int): The numerator.
            denominator (int): The denominator, cannot be 0. Defaults to 1.

        Raises:
            TypeError: If numerator or denominator is not an int.
            ZeroDivisionError: If denominator is 0.
        """
        # type() instead of isinstance(), so that True/False are not accepted
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Numerator and denominator must be integers.")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0.")

        # Keep the sign in the numerator, so the denominator is always > 0
        if denominator < 0:
            numerator, denominator = -numerator, -denominator

        # Store the fraction in lowest terms
        divisor = math.gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor

    @property
    def numerator(self) -> int:
        """The numerator (read-only)."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """The denominator (read-only), always > 0."""
        return self._denominator

    def __eq__(self, other: object) -> bool:
        """Return True if both fractions have the same value."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator == other.numerator
                and self.denominator == other.denominator)

    def __ne__(self, other: object) -> bool:
        """Return True if the fractions have different values."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self == other

    def __lt__(self, other: object) -> bool:
        """Return True if self is smaller than other (a/b < c/d <=> a*d < c*b)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: object) -> bool:
        """Return True if self is smaller than or equal to other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: object) -> bool:
        """Return True if self is greater than other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: object) -> bool:
        """Return True if self is greater than or equal to other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other: object) -> "Fraction":
        """Return the sum of self and other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other: object) -> "Fraction":
        """Return the difference of self and other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other: object) -> "Fraction":
        """Return the product of self and other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other: object) -> "Fraction":
        """Return the quotient of self and other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)
