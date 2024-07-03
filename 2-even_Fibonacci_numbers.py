# By considering the terms in the Fibonacci sequence whose values do not exceed four
# million, find the sum of even-valued terms
# Note: the sequence is seeded with 1, 2

# note that every third term of the sequence is even
# k_i + k_i+1 = k_i+2


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    arr = [1, 2] + [1] * (n - 1)
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1]


if __name__ == "__main__":
    print(sum([fib(i) for i in range(32) if fib(i) % 2 == 0 and fib(i) <= 4_000_000]))
