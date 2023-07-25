import random
from colorama import Fore, Back, Style, init
init(autoreset=True)
from console_messages import welcome_message, winner_message, loser_message, tie_message


WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Winning rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Winning columns
    (0, 4, 8), (2, 4, 6)  # Winning diagonals
    ]
PLAYER_X = Fore.GREEN + 'X' + Fore.RESET
PLAYER_O = Fore.CYAN + 'O' + Fore.RESET
location = [' ' for i in range(9)]
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
    print('      |   |   \n')


def score_display(player_name):
    """
    Prints an updated score board
    to the console
    """
    print(Fore.RED + f'\n          SCORE BOARD')
    print(
        Fore.CYAN + f'    Computer   ' + 
        Fore.RED + '|' + Fore.GREEN + f'     {player_name}'
        )
    print(Fore.RED + '-------------------------------')
    print(Fore.RED + '               |')
    middle = Fore.RED +  '       |       '
    print(
        Fore.CYAN + '       ' + str(computer_score) + 
        middle + Fore.GREEN + str(player_score) + '\n' + Fore.RESET
        )

score_display('David')

def get_player_name():
    """
    Asks for players name,
    validates if input is not empty
    returns name capitalized
    """
    while True:
        player_name = input('>> Hey Player! What is your name?: ')
        if player_name.strip() == '':
            print('\nPlease enter a valid name.\n')
            continue
        else:
            return player_name.capitalize()


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
            update_gameboard(random_position, PLAYER_O)
            print(
                Fore.CYAN + 
                f"\n Your opponent chose {random_position}" + 
                Fore.RESET)
            break


def score_update(player_identity):
    """
    Updates the score variables
    """
    global player_score
    global computer_score
    if player_identity == Fore.GREEN + 'X' + Fore.RESET:
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
    if player_identity == Fore.GREEN + 'X' + Fore.RESET:
        print(winner_message())
    else:
        print(loser_message())
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
    for combo in WINNING_COMBOS:
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
        print(tie_message())
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
            update_gameboard(int(player_location_input), PLAYER_X)
            if check_game_over(PLAYER_X):
                if play_again(player_name):
                    continue
                else:
                    break

            computer_random_choice()
            if check_game_over(PLAYER_O):
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
    print(welcome_message())
    player_name = get_player_name()
    run_game(player_name)


main()
