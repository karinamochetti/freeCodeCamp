def sock_pairs(pairs, cycles):
    socks = 2*pairs
    socks -= cycles//2
    socks += cycles//3
    socks -= cycles//5
    socks += 2*(cycles//10)
    return max(0, socks) // 2

print(sock_pairs(2, 5))
print(sock_pairs(1, 2))
print(sock_pairs(5, 11))
print(sock_pairs(6, 25))
print(sock_pairs(1, 8))
