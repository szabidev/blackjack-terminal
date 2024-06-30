import re
from logo import logo
from unicards import unicard
import random
print(logo)
############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


















# Function to separate uppercase letters and numbers (the first elements) from the string, to determine the card score
def separate_card(card):
    match = re.match(r"([A-Z0-9])", card)
    if match:
        return match.group()
    else:
        return None


# Function to check if a card is spade or not, if false change unicard card color
def is_spade(card):
    return not bool(re.search('s$', card))


# Function to combine unicard() and is_spade() for better readability
def display_cards(card):
    return unicard(card, is_spade(card))


# Define the ranks and suits
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['s', 'h', 'd', 'c']  # s=spades, h=hearts, d=diamonds, c=clubs
# Create the deck
deck = [rank + suit for rank in ranks for suit in suits]


# Draw cards
first_draw = random.sample(deck, 4)
# Check cards after first draw, split them for the players
player_cards = [first_draw[0], first_draw[1]]
player_cards_to_print = [display_cards(player_cards[0]), display_cards(player_cards[1])]
cpu_cards = [first_draw[2], first_draw[3]]
cpu_cards_to_print = [display_cards(cpu_cards[0]), display_cards(cpu_cards[1])]
human = 'player'
cpu = 'cpu'


# TODO calculate score
def calculate_score(cards, player):
    score = 0
    for card in cards:
        card_value = separate_card(card)
        if card_value == 'K' or card_value == 'J' or card_value == "Q":
            card_value = 10
        elif card_value == 'A':
            if player == cpu:
                if score < 8:
                    card_value = 11
                else:
                    card_value = 1
            else:
                card_value = int(input("Choose the value of Ace, type '1' or '11':\n"))
        score += int(card_value)
    return score


def draw_card(cards, player, score_sheet):
    card = random.sample(deck, 1)
    card_to_print = display_cards(card[0])
    print(f"Next {player} card is {card_to_print}")
    # ?
    score_sheet += calculate_score(cards, player)
    # TODO breaks here and asks to choose ace value, fix it
    print(f"Current {player} score is {score_sheet}")


player_score = calculate_score(player_cards, human)
cpu_score = calculate_score(cpu_cards, cpu)
print(f"Your cards are {' '.join(player_cards_to_print)}")
print(f"Current player score: {player_score}")
print(f"Computers cards are {''.join(cpu_cards_to_print)}")
print(f"Current computer score: {cpu_score}")
if player_score == 21:
    print(f"{human} wins")

if cpu_score == 21:
    print(f"{cpu} wins")

if player_score < 15:
    print('Your score is less then 15, you must draw another card')
    draw_card(deck, human, player_score)

