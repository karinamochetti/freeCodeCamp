def prime_factorization(n):
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    fact = []
    for p in PRIMES:
        while n%p == 0:
            fact.append(p)
            n /= p
    return fact

print(prime_factorization(20))
print(prime_factorization(17))
print(prime_factorization(15))
print(prime_factorization(35))
print(prime_factorization(999))
print(prime_factorization(360))
print(prime_factorization(510510))
