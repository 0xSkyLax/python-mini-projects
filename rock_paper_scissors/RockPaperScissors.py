import random

def play():
    user = input("What's your choice?:\nRock (R), Paper (P), Scissors (S)\n").lower()
    computer = random.choice(["r", "p", "s"])
    print(f"The Computer played {computer.upper()}")
    if user == computer:
        return "It's a Tie"
    if is_win(user, computer):
        return "You won"   
    return "You lost"


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())