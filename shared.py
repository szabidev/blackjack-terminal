# Define the ranks and suits
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['s', 'h', 'd', 'c']  # s=spades, h=hearts, d=diamonds, c=clubs
# Create the deck
deck = [rank + suit for rank in ranks for suit in suits]

# Initial cards and score
player_score = 0
player_cards = []
player_cards_to_print = []
cpu_score = 0
cpu_cards = []
cpu_cards_to_print = []
