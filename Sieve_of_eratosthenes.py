import math


def Sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # 전부 True로 채움
    primes[0] = False
    primes[1] = False  # 1제외

    for i in range(2, n + 1):  # 2 <= i < n + 1
        if primes[i]:
            for j in range(2 * i, n, i):  # 배수 처리
                primes[j] = False

    return [i for i in range(2, n) if primes[i]]


n = int(input())
print(Sieve_of_eratosthenes(n))
