def is_circular_prime(n):

    def is_prime(n):
        if n == 1 or n%2==0: return False
        return not any(i for i in range(2,n) if n%i==0)

    m = n
    for _ in range(len(str(m))):
        s = str(m)
        m = int(s[1:] + s[:1])
        if not is_prime(m):
            return False
    return True

print(is_circular_prime(197))
print(is_circular_prime(23))
print(is_circular_prime(13))
print(is_circular_prime(89))
print(is_circular_prime(1193))
