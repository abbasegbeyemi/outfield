from collections import namedtuple
from typing import Union


def aboki_name(name):
    """Decorator to tell you the name of your aboki"""
    def function_decorator(func):
        def function_wrapper(*args, **kwargs):
            print(f"{name.center(30, '*')} with the dollar. We dey convert.")
            return func(*args, **kwargs)

        return function_wrapper
    return function_decorator


class Ccy:
    """A class that contains an amount and it's current unit, that also enables arithmetic operations between currencies"""

    def __init__(self, value: Union[float, int], unit: str = 'USD'):
        """Constructor for Ccy"""
        # Currencies tonversion to dollars as a named tuple cause why not?
        Currencies = namedtuple('Currencies', ['EUR', 'GBP', 'NGN', 'USD'])
        self._currencies = Currencies(0.84, 0.78, 383.45, 1)

        self.value = value
        unit = str(unit).strip().upper()

        if unit not in self._currencies._fields:
            raise TypeError("Unsupported unit type")

        else:
            self.unit = unit

    @aboki_name("Sammy")
    def convert_currency(self, value: Union[int, float] = None, new_unit: str = 'USD'):
        """Base currency is USD so we always want to convert to USD before performing any operations"""
        if value is None:
            value = self.value

        # Make sure the new unit is uppercase and stripped of any spaces
        unit_check = str(new_unit).strip().upper()

        # If the cleaned up new unit is not in our list return
        if unit_check not in self._currencies._fields:
            raise TypeError("Unsupported unit type")

        # Convert the currency to dollar first by dividing by the exchange rate
        to_dollar = value / getattr(self._currencies, self.unit)

        if unit_check == 'USD':
            # Return the dollar value if that is what they're asking for
            return to_dollar
        else:
            # If they want another currency, multiply dollary by the exchange rate and return the new currency
            div = getattr(self._currencies, unit_check)
            return value * div

    def __add__(self, other):
        """This is to add two currencies together"""
        # First convert both to base USD and int or float is assumed to be dollar value
        if type(other) == int:
            other_dollar = other
        else:
            other_dollar = other.convert_currency()

        this_dollar = self.convert_currency()

        # Convert the sum to the currency of the value before the plus sign
        res_value = self.convert_currency((other_dollar + this_dollar), self.unit)
        # Return a new amount based on the result
        return Ccy(res_value, self.unit)

    def __radd__(self, other):
        """This is to add two currencies together"""
        # First convert both to base USD and int or float is assumed to be dollar value
        if type(other) == int:
            other_dollar = other
        else:
            other_dollar = other.convert_currency()

        this_dollar = self.convert_currency()
        # Convert the sum to the currency of the value before the plus sign
        res_value = self.convert_currency((other_dollar + this_dollar), self.unit)
        # Return a new amount based on the result
        return Ccy(res_value, self.unit)

    def __repr__(self):
        return f"Money: {self.value:.2f} {self.unit}"


if __name__ == '__main__':
    abbas_money = Ccy(200, 'gbp')
    ruki_money = Ccy(500, 'eur')
    shola_money = Ccy(1000)

    print("Ruki is ", ruki_money + 5)
    print(200 + abbas_money + 50 + ruki_money + 35 + shola_money)
