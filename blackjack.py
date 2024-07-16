from logo import logo
from actions import draw_one_card, print_cards, is_blackjack, calculate_score, print_score, check_winner
from shared import deck, player_cards, player_cards_to_print, cpu_cards, cpu_cards_to_print


# Blackjack logo
print(logo)

# Determine players
# Ask for player name before draw
# human = input(f"What is your name?\n")
human = 'player'
cpu = 'cpu'


def play_game():
    player_score = 0
    cpu_score = 0
    blackjack = False
    # First round. Draw cards
    draw_one_card(deck, 2, player_cards, player_cards_to_print)
    draw_one_card(deck, 2, cpu_cards, cpu_cards_to_print)

    # Display cards
    print_cards(human, player_cards_to_print)
    print_cards(cpu, cpu_cards_to_print)

    # Check if any of the payers have blackjack
    print(is_blackjack(player_cards))
    print(is_blackjack(cpu_cards))
    if is_blackjack(player_cards):
        print(f"Blackjack!!! Congratulations {human} you won!")
        print('======================================')
        blackjack = True
        return blackjack

    if is_blackjack(cpu_cards):
        print(f"{cpu} has Blakcjack!!! You lost!")
        print('======================================')
        blackjack = True
        return blackjack

    # If nobody has blackjack, calculate the score and display it
    if not blackjack:
        # Check if players have an Ace, ask for it\'s value
        player_score = calculate_score(player_cards, human)
        print_score(human, player_score)
        cpu_score = calculate_score(cpu_cards, cpu)
        print_score(cpu, cpu_score)

    print(player_score, 'playerscore')
    print(cpu_score, 'cpu score')

    while player_score < 18:
        answer = input(f"Your score is {player_score}, do you want another card? Type 'yes' or 'no'\n")
        # Draw ome card for player and one for cpu, display both stats
        if answer == 'yes':
            print(player_cards, 'ply')
            draw_one_card(deck, 1, player_cards, player_cards_to_print)
            if cpu_score < 18:
                draw_one_card(deck, 1, cpu_cards, cpu_cards_to_print)
            player_score = calculate_score(player_cards, human)
            cpu_score = calculate_score(cpu_cards, cpu)
            print_cards(human, player_cards_to_print)
            print_score(human, player_score)
            print_cards(cpu, cpu_cards_to_print)
            print_score(cpu, cpu_score)
            check_winner(human, cpu, player_score, cpu_score)
        # Draw one card for cpu, display both stats
        elif answer == 'no':
            print('no')
            if cpu_score < 18:
                draw_one_card(deck, 1, cpu_cards, cpu_cards_to_print)
                print_cards(human, player_cards_to_print)
                print_cards(cpu, cpu_cards_to_print)
                cpu_score = calculate_score(cpu_cards, cpu)
                print_score(human, player_score)
                print_score(cpu, cpu_score)
                check_winner(human, cpu, player_score, cpu_score)

            else:
                print_cards(human, player_cards_to_print)
                print_score(human, player_score)
                print_cards(cpu, cpu_cards_to_print)
                print_score(cpu, cpu_score)
                check_winner(human, cpu, player_score, cpu_score)
        else:
            return


play_game()

