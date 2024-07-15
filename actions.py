import re
from unicards import unicard
import random
from shared import human, cpu, deck


def separate_card(card):
    """Function to search string and find uppercase letters and numbers"""
    match = re.match(r"([A-Z0-9])", card)
    if match:
        return match.group()
    else:
        return None


def is_spade(card):
    """Function to check if current card is spade or not"""
    return not bool(re.search('s$', card))


def display_cards(card):
    """Function to display unicard format playing cards"""
    return unicard(card, is_spade(card))


def is_blackjack(cards):
    """"Checks if player has blackjack, checking and assigning the value of card from {cards} list argument """
    blackjack_score = 0
    for card in cards:
        if separate_card(card) == "A":
            blackjack_score += 11
        if separate_card(card) == "K" or separate_card(card) == "Q" or separate_card(card) == "J" or separate_card(card) == "10":
            blackjack_score += 10
    print(blackjack_score, 'blackjack score')

    if blackjack_score == 21:
        return True
    else:
        return False


def draw_card(deck_of_cards, num_of_cards_to_draw):
    """"Draw one card from the deck and remove it from that deck"""
    playing_cards = random.sample(deck_of_cards, num_of_cards_to_draw)
    print(playing_cards, 'playing cards')
    if len(playing_cards) < 1:
        deck.remove(playing_cards[0])

    if len(playing_cards) >= 1:
        for playing_card in deck_of_cards:
            if playing_card == playing_cards[0] or playing_card == playing_cards[1] or playing_card == playing_cards[2] or playing_card == playing_cards[3]:
                deck.remove(playing_card)

    return playing_cards


def calculate_score(cards, player):
    score = 0
    for card in cards:
        card_value = separate_card(card)
        if card_value == 'K' or card_value == 'J' or card_value == "Q":
            card_value = 10
        elif card_value == "A":
            if player == cpu:
                if score <= 10:
                    card_value = 11
                else:
                    card_value = 1
            if player == human:
                card_value = int(input("Choose the value of Ace, type '1' or '11':\n"))
        else:
            card_value = card_value
        score += int(card_value)
    # print(score, 'score')
    return score


def draw_one_card(deck_of_cards, num_of_draw, ply_cards, to_print):
    new_card = "".join(random.sample(deck_of_cards, num_of_draw))
    ply_cards.append(new_card)
    to_print.append(display_cards(new_card))
    deck.remove(new_card)
    return new_card


def print_cards(player, to_print):
    print(f"{player}'s cards are {' '.join(to_print)}")


def print_score(player_deck, player):
    score = calculate_score(player_deck, player)
    print(f"Current {player} score is {score}")

# Draw cards 2 and 2 for each player

# Check if any of the cards are A, K, Q , J, and who is the player
    # if player  == human ask if A = 11 or 1
    # if cpu and score less than or = to 15 A = 1 else A = 11

# Check player scores

#  Check if any of the players have blackjack
    # If yes declare winner
    # If no continue the game

# Add up scores (player, cpu)

# Check score if less than or equal to 15
    # If yes draw one card, remove from deck
    # If no but less then 19 ask if player wants another card

# Add up scores again, add card to player card list
