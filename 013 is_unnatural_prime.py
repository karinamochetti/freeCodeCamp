def is_unnatural_prime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(is_unnatural_prime(1))
print(is_unnatural_prime(-1))
print(is_unnatural_prime(19))
print(is_unnatural_prime(-23))
print(is_unnatural_prime(0))
print(is_unnatural_prime(97))
print(is_unnatural_prime(-61))
print(is_unnatural_prime(99))
print(is_unnatural_prime(-44))
