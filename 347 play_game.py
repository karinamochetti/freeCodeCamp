def play_game(p1, p2):
    PAYOFF_MATRIX = {
        ("C", "C"): (3, 3),
        ("D", "D"): (1, 1),
        ("D", "C"): (5, 0),
        ("C", "D"): (0, 5)
    }

    score1, score2 = 0, 0
    for choice1, choice2 in zip(p1, p2):
        p1_gain, p2_gain = PAYOFF_MATRIX[(choice1, choice2)]
        score1 += p1_gain
        score2 += p2_gain

    return [score1, score2]

print(play_game("CCCC", "CCCC"))
print(play_game("DDDD", "DDDD"))
print(play_game("CCDD", "CDDD"))
print(play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD"))
print(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"))
