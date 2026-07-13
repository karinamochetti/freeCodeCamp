from collections import Counter

def five_dice(dice):
    counts = Counter(dice)
    frequencies = list(counts.values())
    dices_str = "".join(str(num) for num in sorted(counts.keys()))

    if len(counts) == 1:
        return "five of a kind"
    if 4 in frequencies:
        return "four of a kind"
    if 3 in frequencies and 2 in frequencies:
        return "full house"
    if dices_str in ["12345", "23456"]:
        return "large straight"
    if any(seq in dices_str for seq in ["1234", "2345", "3456"]):
        return "small straight"
    if 3 in frequencies:
        return "three of a kind"
    if len(counts) == 3 and 2 in frequencies:
        return "two pair"
    if 2 in frequencies:
        return "pair"
    return "no pair"

print(five_dice([1, 1, 1, 1, 1]))
print(five_dice([5, 5, 5, 6, 5]))
print(five_dice([2, 5, 6, 4, 3]))
print(five_dice([4, 3, 3, 3, 1]))
print(five_dice([4, 6, 2, 6, 5]))
print(five_dice([1, 4, 5, 6, 2]))
print(five_dice([1, 3, 4, 6, 2]))
print(five_dice([2, 2, 5, 2, 5]))
print(five_dice([6, 4, 5, 6, 4]))

