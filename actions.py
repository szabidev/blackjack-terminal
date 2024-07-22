import re
from unicards import unicard
import random
from shared import deck


def separate_card(card):
    """Function to search string and find uppercase letters, numbers, and optionally a suit character"""
    match = re.match(r"(\d{1,2}|[A-Z0-9])[shdc]?", card)
    if match:
        return match.group(1)
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
        is_ace = card == 'As' or card == 'Ad' or card == 'Ah' or card == 'Ac'
        if is_ace:
            blackjack_score += 11
        elif separate_card(card) == "K" or separate_card(card) == "Q" or separate_card(card) == "J" or separate_card(card) == "10":
            blackjack_score += 10
        else:
            blackjack_score += int(separate_card(card))

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


def check_winner(player, opponent, ply_score, opp_score):
    """Compare the scores of two players and determine the winner, or if it's a draw"""
    if ply_score > opp_score:
        print(f"Congratulations {player} your score is {ply_score}. You won!")
    elif opp_score > ply_score:
        print(f"{opponent} score is {opp_score}. You lost!")
    else:
        print(f"{player} score: {ply_score}")
        print(f"{opponent} score: {opp_score}")
        print(f"It's a draw")


def calculate_score(cards, player):
    """This function calculates and returns the score without modifying global variables, takes a deck of cards and user as arguments."""
    score = 0
    for card in cards:
        card_value = separate_card(card)
        if card_value in ['K', 'J', "Q"]:
            card_value = 10
        elif card_value == "A":
            if player == "cpu":
                card_value = 11 if score <= 10 else 1
            else:
                card_value = int(input("Choose the value of Ace, type '1' or '11':\n"))
                print('======================================')
        score += int(card_value)
    return score


def draw_one_card(deck_of_cards, num_of_draw, ply_cards, to_print):
    new_card = ''
    for _ in range(num_of_draw):
        new_card = ''.join(random.sample(deck_of_cards, 1))
        ply_cards.append(new_card)
        to_print.append(display_cards(new_card))
        deck.remove(new_card)
    return new_card


def print_cards(player, to_print):
    print(f"{player}'s cards are {' '.join(to_print)}")
    print('======================================')


def print_score(player, score):
    print(f"Current {player} score is {score}")
    print('======================================')
    return score


