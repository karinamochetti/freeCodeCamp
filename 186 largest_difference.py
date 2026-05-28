def largest_difference(skater1, skater2):
    max_diff = 0
    index = -1
    for idx, (s1, s2) in enumerate(zip(skater1, skater2), start=1):
        if abs(s1-s2) > max_diff: 
            max_diff = abs(s1-s2)
            index = idx
    return index

print(largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]))
print(largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]))
print(largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95]))
print(largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01]))
print(largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10]))
