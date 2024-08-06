import random
from os import system, name

import game_data
import ascii_art


def display_logos(logo_type="logo"):
    """Displays the game logo or the 'vs' graphic."""
    if logo_type == 'logo':
        print(ascii_art.logo)
    else:
        print(ascii_art.vs)


def pick_an_option():
    """
    Returns a random IG account data from game_data.
    """
    return random.choice(game_data.data)


def display_option(option, option_data):
    """Displays the option data in a formatted way."""
    name = option_data['name']
    description = option_data['description']
    country = option_data['country']
    if option == 'a':
        return print(f"Compare A: {name}, {description}, from {country}.")
    else:
        return print(f"Against B: {name}, {description}, from {country}.")


def is_guess_correct(a_followers, b_followers, user_answer):
    """
    Returns True or False based on user's guess.

    :param a_followers: Follower count of option A.
    :param b_followers: Follower count of optiob B.
    :param user_answer: User guess ('a' or 'b').
    :return: Boolean indicating if the guess is correct.
    """
    return (a_followers > b_followers and user_answer == 'a') or (a_followers < b_followers and user_answer == 'b')


def get_user_input():
    """Gets and validates the user's input ('a' or 'b')."""
    while True:
        user_input = str(input("Who has more followers? Type 'A' or 'B': ")).casefold()
        if user_input in ['a', 'b']:
            return user_input
        else:
            print("Please provide a valid answer")


def clear_screen():
    """
    Clears the console screen.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def higher_lower_game():
    """Main game function for the Higher/Lower game."""
    score = 0
    option_a_data = pick_an_option()
    game_continue = True

    while game_continue:

        option_b_data = pick_an_option()

        while option_a_data == option_b_data:
            option_b_data = pick_an_option()

        clear_screen()
        display_logos('logo')
        if score:
            print(f"You're right! Current score: {score}")
        display_option('a', option_a_data)
        display_logos('vs')
        display_option('b', option_b_data)

        user_input = get_user_input()
        a_followers = option_a_data['follower_count']
        b_followers = option_b_data['follower_count']

        if is_guess_correct(a_followers, b_followers, user_input):
            score += 1
            option_a_data = option_b_data
        else:
            game_continue = False
            clear_screen()
            display_logos('logo')
            print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == "__main__":
    higher_lower_game()
