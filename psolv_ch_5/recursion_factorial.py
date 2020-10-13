# Recursive fuction to compute the factorial of a number
from typing import Union


def factorial(number: Union[int, float]) -> Union[int, float]:
    if number <= 1:
        return 1

    else:
        return number * factorial(number - 1)


def recurse_reverse(list_in: list) -> list:
    last_val = list_in.pop()
    result = [last_val]
    if len(list_in) < 1:
        return result

    else:
        result.extend(recurse_reverse(list_in))
        return result


if __name__ == '__main__':
    # print(factorial(-1))
    print(recurse_reverse([1, 2, 3, 4, 5]))
