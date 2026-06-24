from collections import Counter

def get_best_hand(cards):
    suits = [card[1] for card in cards]
    ranks = [card[0] for card in cards]
    suits_fre = Counter(suits)
    ranks_fre = Counter(ranks)

    def isSorted(ranks):
        value = {"A": 1, "T": 10, "J": 11, "Q": 12, "K": 13}
        int_ranks = sorted([int(r) if r.isdigit() else value[r] for r in ranks])
        if any((a2-a1)!=1 for a1,a2 in zip(int_ranks[:-1], int_ranks[1:])):
            return False
        return True

    if len(suits_fre) == 1 and all(r in ranks for r in ["A", "K", "Q", "J", "T"]):
        return "Royal Flush"
    if len(set(suits)) == 1 and isSorted(ranks):
        return "Straight Flush"
    if 4 in ranks_fre.values():
        return "Four of a Kind"
    if 3 in ranks_fre.values() and 2 in ranks_fre.values():
        return "Full House"
    if len(suits_fre) == 1:
        return "Flush"
    if isSorted(ranks):
        return "Straight"
    if 3 in ranks_fre.values():
        return "Three of a Kind"
    if list(ranks_fre.values()).count(2) == 2:
        return "Two Pair"
    if len(ranks_fre) == 4:
        return "Pair"
    return "High Card"

print(get_best_hand(["7s", "7h", "7d", "2c", "5h"]))
print(get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]))
print(get_best_hand(["2h", "5h", "7h", "9h", "Jh"]))
print(get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]))
print(get_best_hand(["Ts", "Th", "9d", "9c", "8h"]))
print(get_best_hand(["9c", "8c", "7c", "6c", "5c"]))
print(get_best_hand(["As", "Kh", "Jd", "8c", "5h"]))
print(get_best_hand(["As", "2h", "3d", "4c", "5h"]))
print(get_best_hand(["Ts", "Th", "7c", "6d", "5h"]))
print(get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]))
