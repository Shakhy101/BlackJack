############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_ended = False
new_game = True


def clear():
    return os.system('clear')


def deal_card(cards):
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(list_of_cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0  # blackjack
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)
    return sum(list_of_cards)


def compare(user_score, computer_score):
    if computer_score == 0:
        return "Blackjack, computer wins."
    elif user_score == 0:
        return "Blackjack, you win."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win."
    elif user_score == computer_score:
        return "It's a draw."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."
        


def blackjack(game_ended, user_cards, computer_cards):
    print(logo)

    # deal starting hand
    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    while not game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        comp_first_card = computer_cards[0]

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card {comp_first_card}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_ended = True
        else:
            user_wants_card = input(
                "Do you want another card? Type 'y' or 'n': ").lower()
            if user_wants_card == 'y':
                user_cards.append(deal_card(cards))
            else:
                game_ended = True
                while computer_score < 17:
                    computer_cards.append(deal_card(cards))
                    computer_score = calculate_score(computer_cards)

    if game_ended:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    result = compare(user_score, computer_score)
    print(result)


while new_game:
    if input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
        user_cards = []
        computer_cards = []
        clear()
        blackjack(game_ended, user_cards, computer_cards)

    else:
        new_game = False
