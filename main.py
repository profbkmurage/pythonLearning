import random  # an example of an import statement

# dictionaries are used to store key-value pairs
# dict = {"name" :"beau" , "color": "coffee black"}
# food = [] defines a list
# computer2_choice = "rock"----> the way to declare variables in python

player_choice = "rock"
computer_choice = "paper"

print(player_choice)
print(computer_choice)
print(player_choice + " " + computer_choice)


def get_choices() -> object:  # definition of a function
    player2_choice = input("Enter your choice, paper, scissors or rock ")
    computer_choices = ["paper", "rock", "scissors"]
    choices = {"playerOption": player2_choice, "computer3": random.choice(computer_choices)}
    return choices


response = get_choices()  # calling a function
print(response)


def check_win(player, computer):
    print('you chose ' + player + ' .and the computer chose ' + computer)
    if player == computer:
        return f"its a tie! you chose {player} and computer chose {computer}"


print(check_win("rock", "rock"))
