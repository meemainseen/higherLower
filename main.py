import random
from art import logo, vs
from game_data import data
import os
from rich import print

# Define compare. A function that compares followers count in the selected dictionaries and returns string as output
def compare(A, B):
  if A['follower_count'] > B['follower_count']:
    return 'A'
  else:
    return 'B'
  
# Initial Selection. Choose two random entries and save them to a list. sample is used instead of choices to avoid dupliacte choices
selection = random.sample(data, k=2)

A = selection[0]
B = selection[1]

# Declaring score and game end variables
score = 0
game_end = False
# Print logo
print(f"[red]{logo}[/red]")
# The game loop 
while not game_end:
  # Print initial comparison statements 
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}") 
  # For testing only
  #print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} : {A['follower_count']}") 
  print(f"[red]{vs}[/red]")
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
  # For testing only
  #print(f"Against B: {B['name']}, a {B['description']}, from {B['country']} : {B['follower_count']}")
  
  # Player input is stored as a choice which is then checked against the output of the compared function
  choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  # Returned value of compare function
  result = compare(A, B)
  # If choice is correct. Score is incremented and the game continues
  if choice == result:
    score += 1
    os.system('clear')
    # Print logo
    print(f"[red]{logo}[/red]")
    # Print current score
    print(f"[blue]You're right! Current score: {score}[/blue]")
    # Dictionary entry B now becomes A 
    A = B
    # Variable B gets assigned a random entry from the data list
    B = random.choice(data)
    # To avoid duplicate >> If B matches A, B is assigned another random entry from the data list 
    if B['name'] == A['name']:
      B = random.choice(data)
      
  # If player choice does not match the result 
  else:
    # Game Ends
    game_end = True
    os.system('clear')
    print(f"[red]{logo}[/red]")
    # Prints final score
    print(f"[red]Oops! that was incorrect. Your score: {score}[/red]")