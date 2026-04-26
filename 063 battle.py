def battle(our_team, opponent):
    our_words = our_team.split()
    their_words = opponent.split()
    our_points = 0
    their_points = 0

    for our_word, their_word in zip(our_words,their_words):

        our_values_lower = [ord(c)-ord("a")+1 for c in our_word if c.islower()]
        our_values_upper = [2*(ord(c)-ord("A")+1) for c in our_word if c.isupper()]

        their_values_lower = [ord(c)-ord("a")+1 for c in their_word if c.islower()]
        their_values_upper = [2*(ord(c)-ord("A")+1) for c in their_word if c.isupper()]

        our_values = our_values_lower + our_values_upper
        their_values = their_values_lower + their_values_upper

        if sum(our_values) > sum(their_values):
            our_points += 1
        if sum(our_values) < sum(their_values):
            their_points += 1

    if our_points > their_points:
        return "We win"
    elif our_points < their_points:
        return "We lose"
    else:
        return "Draw"

print(battle("hello world", "hello word"))
print(battle("Hello world", "hello world"))
print(battle("lorem ipsum", "kitty ipsum"))
print(battle("hello world", "world hello"))
print(battle("git checkout", "git switch"))
print(battle("Cheeseburger with fries", "Cheeseburger with Fries"))
print(battle("We must never surrender", "Our team must win"))
