import math

def nth_prime(n):
    def isPrime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    
    primes = 0
    i = 1
    while primes < n:
        i += 1
        if isPrime(i): primes += 1

    return i

print(nth_prime(5))
print(nth_prime(10))
print(nth_prime(16))
print(nth_prime(99))
print(nth_prime(1000))
