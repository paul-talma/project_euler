# What is the largest prime factor of 600_851_475_143?

import math


def all_primes_below(n):
    primes = []
    for i in range(2, n):
        if all([i % k != 0 for k in primes]):
            primes.append(i)
    return primes


def prime_factors(n):
    return [p for p in all_primes_below(int(math.sqrt(n))) if n % p == 0]


if __name__ == "__main__":
    print(prime_factors(600_851_475_143))
