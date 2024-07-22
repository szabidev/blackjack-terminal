from logo import logo
from actions import draw_one_card, print_cards, is_blackjack, calculate_score, print_score, check_winner
from shared import deck, player_cards, player_cards_to_print, cpu_cards, cpu_cards_to_print

# Blackjack logo
print(logo)

# Determine players
# Ask for player name before draw
human = input(f"What is your name?\n")
cpu = 'cpu'
play = True


def play_game():
    blackjack = False
    player_score = 0
    cpu_score = 0

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
        player_score += calculate_score(player_cards, human)
        print_score(human, player_score)
        blackjack = True
        return blackjack

    if is_blackjack(cpu_cards):
        print(f"{cpu} has Blakcjack!!! You lost!")
        print('======================================')
        cpu_score += calculate_score(cpu_cards, cpu)
        print_score(cpu, cpu_score)
        blackjack = True
        return blackjack

    # If nobody has blackjack, calculate the score and display it
    if not blackjack:
        # Check if players have an Ace, ask for it\'s value
        player_score += calculate_score(player_cards, human)
        print_score(human, player_score)
        cpu_score += calculate_score(cpu_cards, cpu)
        print_score(cpu, cpu_score)

        #  If player score is less than 17 tell the player he needs another card
        while player_score <= 17:
            input(f"Your score is {player_score}, you must draw another card.\nPress 'Enter' to continue.\n")
            draw_one_card(deck, 1, player_cards, player_cards_to_print)
            player_score += calculate_score([player_cards[-1]], human)
            print_cards(human, player_cards_to_print)
            print_score(human, player_score)

        # If 17 < player_score < 20 ask the user if it wants to stop or continue playing, loop to make sure user types yes or no
        if 17 < player_score < 20:
            while True:
                answer = input(f"Your score is {player_score}.\nDo you want another card?\nType 'yes' to draw or 'no' to stop playing:\n").lower()
                if answer == 'yes':
                    draw_one_card(deck, 1, player_cards, player_cards_to_print)
                    player_score += calculate_score([player_cards[-1]], human)
                    print_cards(human, player_cards_to_print)
                    print_score(human, player_score)
                    if player_score >= 20:
                        break
                elif answer == 'no':
                    break
                else:
                    print("Please type 'yes' or 'no'.\n")

        # Keep drawing cards until cpu_score > 17
        while cpu_score < 17:
            draw_one_card(deck, 1, cpu_cards, cpu_cards_to_print)
            cpu_score += calculate_score([cpu_cards[-1]], cpu)
            print_cards(cpu, cpu_cards_to_print)

        print_score(cpu, cpu_score)

        # Compare scores to determine winners
        if cpu_score > 21:
            print(f"{cpu} score is {cpu_score}.\nYou win!")
            return
        elif player_score > 21:
            print(f"{cpu} score is {cpu_score}.\nYou lose!")
            return
        else:
            check_winner(human, cpu, player_score, cpu_score)


def main():
    while True:
        # Ask the user if they want to play or replay the game
        play_response = input("Do you want to play Blackjack? Type 'yes' to play, or anything else to quit: ").lower()

        # If the user responds with 'yes', start or replay the game
        if play_response == 'yes':
            play_game()
        else:
            # If the user responds anything else quit playing the game
            print("Thank you for playing! Goodbye.")
            break  # Exit the loop and end the program


if __name__ == "__main__":
    main()

