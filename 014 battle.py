import string

def battle(my_army, opposing_army):

    def score(char):
        if char.isalpha():
            return int(ord(char)-ord('a')+1)
        if char.isdigit():
            return int(char)
        return 0

    if len(my_army) > len(opposing_army): return "Opponent retreated"
    if len(my_army) < len(opposing_army): return "We retreated"

    my_wins = 0
    oppo_wins = 0

    for my_char, oppo_char in zip(my_army, opposing_army):
        my_val = score(my_char)
        oppo_val = score(oppo_char)
        
        if my_val > oppo_val:
            my_wins += 1
        elif my_val < oppo_val:
            oppo_wins += 1
    
    if my_wins > oppo_wins: return "We won"
    if my_wins < oppo_wins: return "We lost"
    else: return "It was a tie"


print(battle("Hello", "World"))
print(battle("pizza", "salad"))
print(battle("C@T5", "D0G$"))
print(battle("kn!ght", "orc"))
print(battle("PC", "Mac"))
print(battle("Wizards", "Dragons"))
print(battle("Mr. Smith", "Dr. Jones"))
