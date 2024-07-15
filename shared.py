human = input(f"What is your name?\n")
cpu = 'cpu'

# Define the ranks and suits
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['s', 'h', 'd', 'c']  # s=spades, h=hearts, d=diamonds, c=clubs

# Create the deck
deck = [rank + suit for rank in ranks for suit in suits]
player_score = 0
cpu_score = 0
