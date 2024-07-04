# What is the largest prime factor of 600_851_475_143?

import math


def factors(n):
    factors = []
    current_factor = 2
    if n % current_factor == 0:
        while n % current_factor == 0:
            factors.append(current_factor)
            n //= current_factor

    current_factor = 3
    while n > 1:
        if n % current_factor == 0:
            while n % current_factor == 0:
                factors.append(current_factor)
                n //= current_factor
        current_factor += 2
    return factors


def unique_factors(n):
    factors = []
    current_factor = 2
    current_factor = 2
    if n % current_factor == 0:
        while n % current_factor == 0:
            factors.append(current_factor)
            n //= current_factor

    current_factor = 3
    while n > 1:
        if n % current_factor == 0:
            factors.append(current_factor)
            while n % current_factor == 0:
                n //= current_factor
        current_factor += 1
    return factors


def largest_factor(n):
    largest = 1
    current_factor = 2
    if n % current_factor == 0:
        while n % current_factor == 0:
            n //= current_factor
        largest = 2

    current_factor = 3
    max_factor = math.sqrt(n)
    while n > 1 and current_factor <= max_factor:
        if n % current_factor == 0:
            while n % current_factor == 0:
                n //= current_factor
            largest = current_factor
            max_factor = math.sqrt(n)
        current_factor += 2
    if n == 1:
        return largest
    return n


if __name__ == "__main__":
    k = 343567
    print(factors(k))
    print(unique_factors(k))
    print(largest_factor(k))
