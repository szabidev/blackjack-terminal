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
    blackjack = False

    # First round. Draw cards
    draw_one_card(deck, 2, player_cards, player_cards_to_print)
    draw_one_card(deck, 2, cpu_cards, cpu_cards_to_print)

    # Display cards
    print_cards(human, player_cards_to_print)
    print_cards(cpu, cpu_cards_to_print)

    # Check if any of the players have blackjack
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

        #  If player score is less than 17 tell the player he needs another card
        if player_score < 17:
            input(f"Your score is {player_score}, you must draw another card. Press 'Enter' to continue.\n")
            draw_one_card(deck, 1, player_cards, player_cards_to_print)
            player_score = calculate_score(player_cards, human)
            print_cards(human, player_cards_to_print)
            print_score(human, player_score)
        # If player score is 17 >= player_score <= 20 ask if he wants another card or stop playing
        elif 17 >= player_score <= 20:
            answer = input(f"Your score is {player_score}, do you want another card? Type 'yes' to draw or 'no' to stop.\n")
            # Continue
            if answer.lower() == 'yes':
                draw_one_card(deck, 1, player_cards, player_cards_to_print)
                player_score = calculate_score(player_cards, human)
                print_cards(human, player_cards_to_print)
                print_score(human, player_score)
            # Stop
            elif answer.lower() == 'no':
                print_cards(human, player_cards_to_print)
                print_score(human, player_score)
        elif player_score == 21:
            print(f"Congratulations {human} your score is {player_score}! You won!")
        else:
            print(f"{human} your score is {player_score}. You lost! Game Over!")

        # Check cpu score, if less than 19 draw another card
        if cpu_score < 19:
            print(f"{cpu} score is {cpu_score}, draws another card")
            draw_one_card(deck, 1, cpu_cards, cpu_cards_to_print)
            cpu_score = calculate_score(cpu_cards, cpu)
            print_cards(cpu, cpu_cards_to_print)
            print_score(cpu, cpu_score)
        elif 19 == cpu_score < 21:
            cpu_score = calculate_score(cpu_cards, cpu)
            print_cards(cpu, cpu_cards_to_print)
            print_score(cpu, cpu_score)
            print(f"{cpu} score is {cpu_score}")
        elif cpu_score == 21:
            print(f"{cpu} score is {cpu_score}. You lost! Play again?")


play_game()

