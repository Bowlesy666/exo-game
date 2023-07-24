"""
run_game
create_board - done
validate_input
update_board
check_if_empty - still need to do
check_for_winner
computer_random_move
play_again
for loop - score keeping
"""
import random


board = [' ' for i in range(9)]
player_x = 'X'
player_o = 'O'


def create_board():
    """
    Creates board to be displayed,
    each section will be numbered to help player
    selection area in centre of each section
    """
    print('1  |2  |3  ')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |   ')
    print('-----------')
    print('4  |5  |6  ')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |   ')
    print('-----------')
    print('7  |8  |9  ')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |   ')


def get_welcome_message(file):
    """
    Opens, reads, store as variable and close text file
    keeps run.py file cleaner
    returns data to be printed before game is run
    """
    data = open(file)
    file_data = data.read()
    data.close()
    return file_data


def update_board(chosen_position, player_x_or_o):
    """
    Updates chosen position with either X or O
    """
    board[chosen_position - 1] = player_x_or_o


def computer_random_choice():
    while True:
        random_position = random.randint(1, 9)
        if board[random_position - 1] == ' ':
            update_board(random_position, player_o)
            print(f"Your opponent chose {random_position}")
            break


def check_for_winner():
    """
    Checks winning combinations after player moves
    """
    print('Checking for winner...')


def check_game_over():
    """
    Checks if game over, if winner announced or
    if board is full
    """
    print('checking for game over...')


def run_game(player_name):
    """
    Runs the game tic-tac-toe displaying the board,
    receiving input from player and taking the computers turns

    """
    while True:
        print(f"\n\n{player_name} you're up!")
        create_board()
        player_input = int(input('Choose an empty space (1-9)'))
        try:
            if int(player_input) < 1:
                print('number is too little!')
            elif int(player_input) > 9:
                print('number is too big!')
            elif board[player_input - 1] != ' ':
                print('Position is already occupied! Try again...')
            else:
                update_board(int(player_input), player_x)
                check_game_over()

                computer_random_choice()
        except ValueError:
            print('Hey, hey. were choosing numbers here! stay on track!')


def main():
    """
    This is the initial function that runs welcome message
    asks for user name
    then runs game and passes player name
    """
    welcome_message = get_welcome_message('welcome.txt')
    print(welcome_message)
    player = input('Hey Player! What is your name?: ')
    run_game(player)


main()
