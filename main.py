import random
def getChoices():
    
    playerChoice = input("Enter your choice (rock, paper, scissors): ")
    randomChoice = random.randint(0, 2)
    options = ["rock", "paper", "scissors"]
    computerChoice = options[randomChoice]
    
    choices = {"player": playerChoice, "computer": computerChoice}
    return choices
choices = getChoices()
print(choices)

# dictionaries 
dict = {"name": "John", "color": choices}