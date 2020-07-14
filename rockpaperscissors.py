def fight(p1,p2):
    if p1 == p2:
        return "Tie"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 wins."
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 wins."
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 wins."
    elif p2 == 'rock' and p1 == 'scissors':
        return "Player 2 wins."
    elif p2 == 'paper' and p1 == 'rock':
        return "Player 2 wins."
    elif p2 == 'scissors' and p1 == 'paper':
        return "Player 2 wins."

    
validInput = ['rock','paper','scissors']

p1Choice = input("Player 1? ")

while p1Choice not in validInput:
    print("Please enter a valid input")
    p1Choice = input("Player 1? ")

p2Choice = input("Player 2? ")

while p2Choice not in validInput:
    print("Please enter a valid input")
    p1Choice = input("Player 2? ")

print(fight(p1Choice,p2Choice))
fight("rock","rock")


