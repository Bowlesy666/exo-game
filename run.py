"""
colorama
validation for name input
txt files
"""
import random


location = [' ' for i in range(9)]
winning_combos = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Winning rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Winning columns
    (0, 4, 8), (2, 4, 6)  # Winning diagonals
    ]
player_x = 'X'
player_o = 'O'
computer_score = 0
player_score = 0


def display_gameboard():
    """
    Creates board to be displayed,
    each section will be numbered to help player
    selection area in centre of each section
    """
    print('   1  |2  |3  ')
    print('    ' + location[0] + ' | ' + location[1] + ' | ' + location[2])
    print('      |   |   ')
    print('   -----------')
    print('   4  |5  |6  ')
    print('    ' + location[3] + ' | ' + location[4] + ' | ' + location[5])
    print('      |   |   ')
    print('   -----------')
    print('   7  |8  |9  ')
    print('    ' + location[6] + ' | ' + location[7] + ' | ' + location[8])
    print('      |   |   ')


def score_display(player_name):
    """
    Prints an updated score board
    to the console
    """
    print(f'\n          SCORE BOARD')
    print(f'    Computer   |     {player_name}')
    print('-------------------------------')
    print('               |')
    middle = '       |       '
    print('       ' + str(computer_score) + middle + str(player_score) + '\n')


def get_message(file):
    """
    Opens, reads, store as variable and close text file
    keeps run.py file cleaner
    returns data to be printed
    """
    data = open(file)
    file_data = data.read()
    data.close()
    return file_data


def update_gameboard(chosen_position, player_x_or_o):
    """
    Updates chosen position with either X or O
    """
    location[chosen_position - 1] = player_x_or_o


def reset_gameboard():
    """
    Resets gameboard locations to
    blank spaces
    """
    global location
    location = [' ' for i in range(9)]


def computer_random_choice():
    """
    Gives computer random choice for
    location
    """
    while True:
        random_position = random.randint(1, 9)
        if location[random_position - 1] == ' ':
            update_gameboard(random_position, player_o)
            print(f"\n Your opponent chose {random_position}")
            break


def score_update(player_identity):
    """
    Updates the score variables
    """
    global player_score
    global computer_score
    if player_identity == 'X':
        player_score += 1
    else:
        computer_score += 1


def winner_display(player_identity):
    """
    Checks who the player is that won,
    calls the correct message
    to console, calls next game and
    updates score board
    """
    if player_identity == 'X':
        message_file = 'winner.txt'
    else:
        message_file = 'loser.txt'
    print(get_message(message_file))
    display_gameboard()


def play_again(player_name):
    """
    Asks player if they want to continue playing
    or to return the final score and Exit
    """
    score_display(player_name)
    while True:
        play_again_input = input(
            f">> {player_name}, do you want to play again?: (y/n) ")
        print(play_again_input.lower())
        if play_again_input.lower() not in ('y', 'n'):
            print(' Invalid value, please use lowercase y or n.....')
            continue

        if play_again_input == 'y':
            reset_gameboard()
            return True
        elif play_again_input == 'n':
            print('\n Thank you for playing EXO!')
            return False


def check_for_winner():
    """
    Checks winning combinations after player moves
    """
    for combo in winning_combos:
        zero, one, two = combo
        if location[zero] == location[one] == location[two] != ' ':
            return True


def check_game_over(player_name):
    """
    Checks if game over - if winner announced or
    if board is full
    """
    if check_for_winner():
        score_update(player_name)
        winner_display(player_name)
        return True
    elif ' ' not in location:
        print(get_message('tie.txt'))
        display_gameboard()
        return True
    else:
        return False


def run_game(player_name):
    """
    Runs the game tic-tac-toe displaying the board,
    receiving input from player and taking the computers turns

    """
    while True:
        print(f"\n {player_name} you're up!\n")
        display_gameboard()
        try:
            player_location_input = int(input('>> Choose an empty space(1-9)'))
        except ValueError:
            print('\n Hey, hey. were choosing numbers here! stay on track!')
            continue
        if int(player_location_input) < 1:
            print(' Number is too little! Try again...\n')
        elif int(player_location_input) > 9:
            print(' Number is too big! Try again...\n')
        elif location[player_location_input - 1] != ' ':
            print(' Position is already occupied! Try again...\n')
        else:
            update_gameboard(int(player_location_input), player_x)
            if check_game_over(player_x):
                if play_again(player_name):
                    continue
                else:
                    break

            computer_random_choice()
            if check_game_over(player_o):
                if play_again(player_name):
                    continue
                else:
                    break


def main():
    """
    This is the initial function that runs welcome message
    asks for user name
    then runs game and passes player name
    """
    print(get_message('welcome.txt'))
    player_name = input('>> Hey Player! What is your name?: ')
    run_game(player_name.capitalize())


main()
