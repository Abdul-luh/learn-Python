def getChoices():
    
    playerChoice = input("Enter your choice: (rock, paper, scissors)")
    computerChoice = "paper"
    choices = {"player": playerChoice, "computer": computerChoice}
    return choices
choices = getChoices()
print(choices)

# dictionaries 
dict = {"name": "John", "color": choices}