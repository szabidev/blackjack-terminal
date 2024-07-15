from logo import logo
from actions import display_cards, is_blackjack, draw_card, draw_one_card, print_cards, print_score
from shared import human, cpu, deck, player_score, cpu_score

# Blackjack logo
print(logo)

# Draw 4 cards
first_draw = draw_card(deck, 4)
# Check cards after first draw, split them for the players
player_cards = [first_draw[0], first_draw[1]]
player_cards_to_print = [display_cards(player_cards[0]), display_cards(player_cards[1])]
cpu_cards = [first_draw[2], first_draw[3]]
cpu_cards_to_print = [display_cards(cpu_cards[0]), display_cards(cpu_cards[1])]

# Print cards after first draw
print_cards(human, player_cards_to_print)
print_cards(cpu, cpu_cards_to_print)

# Print score after first round
print_score(player_cards, human)
print_score(cpu_cards, cpu)


if is_blackjack(player_cards):
    print(f"Blackjack!!! Congratulations {human} you win")
if is_blackjack(cpu_cards):
    print(f"Blackjack!!! {cpu} won!")

if player_score <= 15:
    new_card_player_card = draw_one_card(deck, 1, player_cards, player_cards_to_print)
    print(f"Your card is {new_card_player_card}")

if cpu_score <= 15:
    new_cpu_card = draw_one_card(deck, 1, cpu_cards, cpu_cards_to_print)
    print(f"{cpu} card is {new_cpu_card}")

# Print cards after second draw
print_cards(human, player_cards_to_print)
print_cards(cpu, cpu_cards_to_print)

# print(player_cards)
# print(cpu_cards)
# print(len(deck), 'deck')
print(cpu_cards, 'cpu cards')
print(player_cards, 'player cards')

