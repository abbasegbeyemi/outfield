class Fraction():

    def __init__(self, top, bottom):
        self._num = top
        # Force denominator to positive everytime
        self._den = abs(bottom)

        # Check to make sure that the fractions are always both integers
        if type(top) is not int or type(bottom) is not int:
            raise TypeError("Only integers are allowed babe.")

    @property
    def num(self):
        return self._num // gcd(self._num, self._den)

    @property
    def den(self):
        return self._den // gcd(self._num, self._den)

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        """Add two fractions"""
        return Fraction(((other.den * self.num) + (self.den * other.num)), (self.den * other.den))

    def __sub__(self, other):
        """Subtract two fractions"""
        return Fraction(((other.den * self.num) - (self.den * other.num)), (self.den * other.den))

    def __mul__(self, other):
        """Multiply two fractions"""
        return Fraction((self.num * other.num), (self.den * other.den))

    def __truediv__(self, other):
        # Divide two fractions
        return Fraction((self.num * other.den), (self.den * other.num))

    def __eq__(self, other):
        """Equality is achieved by cross multiplying"""
        return self.num * other.den == self._den * other.num

    def __gt__(self, other):
        return self.num * other.den > self._den * other.num

    def __lt__(self, other):
        return self.num * other.den < self._den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self._den * other.num

    def __le__(self, other):
        return self.num * other.den <= self._den * other.num

    def __ne__(self, other):
        return self.num * other.den != self._den * other.num


def gcd(m, n):
    """This to to find the greatest common denominator of a fraction. Euclids algo"""
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n

    return n


if __name__ == '__main__':
    f1 = Fraction(3, 7)
    f2 = Fraction(1, 2)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 == f1)
    print(f2 > f1)
    print(f2 < f1)

    f3 = Fraction(1.2, 3)
