def rock_paper_scissors(player1, player2):
    rules = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    
    if player1 == player2:
        return "Tie"

    if rules[player1] == player2:
        return "Player 1 wins"
    return "Player 2 wins"

print(rock_paper_scissors("Rock", "Rock"))
print(rock_paper_scissors("Rock", "Paper"))
print(rock_paper_scissors("Scissors", "Paper"))
print(rock_paper_scissors("Rock", "Scissors"))
print(rock_paper_scissors("Scissors", "Scissors"))
print(rock_paper_scissors("Scissors", "Rock"))
