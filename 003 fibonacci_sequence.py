def fibonacci_sequence(start_sequence, length):
    sequence = []
    if length == 0:
        sequence = []
    elif length == 1:
        sequence = [start_sequence[0]]
    else:
        sequence = start_sequence
        for i in range(2, length):
            sequence.append(sequence[-1]+sequence[-2])
    return sequence

print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))