"""
run_game
done - create_board - done
done - validate_input
done - update_board
done - check_if_empty
done - check_for_winner -
done - check_game_over > we have a winner
done -computer_random_move
almost done - play_again - has bug, wont accept capitals!
for loop - score keeping
"""
import random


board = [' ' for i in range(9)]
winning_combos = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Winning rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Winning columns
    (0, 4, 8), (2, 4, 6)  # Winning diagonals
    ]
player_x = 'X'
player_o = 'O'
computer_score = 0
player_score = 0


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


def score_display(player_name):
    print(f'\n          SCORE BOARD')
    print(f'    Computer   |     {player_name}')
    print('-------------------------------')
    print('               |')
    print('       ' + str(computer_score) + '       |       ' + str(player_score) + '\n')


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


def update_board(chosen_position, player_x_or_o):
    """
    Updates chosen position with either X or O
    """
    board[chosen_position - 1] = player_x_or_o


def reset_game_board():
    global board
    board = [' ' for i in range(9)]


def computer_random_choice():
    while True:
        random_position = random.randint(1, 9)
        if board[random_position - 1] == ' ':
            update_board(random_position, player_o)
            print(f"Your opponent chose {random_position}")
            break


def score_update(player):
    global player_score
    global computer_score
    if player == 'X':
        player_score += 1
    else:
        computer_score += 1

def winner_display(player):
    """
    Checks who the player is that won,
    calls the correct message
    to console, calls next game and
    updates score board
    """
    if player == 'X':
        message_file = 'winner.txt'
    else:
        message_file = 'loser.txt'
    print(get_message(message_file))
    create_board()


def play_again(player_name):
    """
    Asks player if they want to continue playing
    or to return the final score and Exit
    """
    score_display(player_name)
    while True:
        play_again_input = input("Do you want to play again?: (y/n)")
        print(play_again_input.lower())
        if play_again_input.lower() not in ('y', 'n'):
            print('Invalid value, please use lowercase y or n.....')
            continue

        if play_again_input == 'y':
            reset_game_board()
            return True
        elif play_again_input == 'n':
            print('They said no dude!')
            return False


def check_for_winner():
    """
    Checks winning combinations after player moves
    """
    print('Checking for winner...')
    for combo in winning_combos:
        zero, one, two = combo
        if board[zero] == board[one] == board[two] != ' ':
            print("We have a weener!")
            return True


def check_game_over(player):
    """
    Checks if game over - if winner announced or
    if board is full
    """
    print('checking for game over...')
    if check_for_winner():
        score_update(player)
        winner_display(player)
        return True
    elif ' ' not in board:
        print(get_message('tie.txt'))
        create_board()
        return True
    else:
        return False


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
        except ValueError:
            print('Hey, hey. were choosing numbers here! stay on track!')


def main():
    """
    This is the initial function that runs welcome message
    asks for user name
    then runs game and passes player name
    """
    welcome_message = get_message('welcome.txt')
    print(welcome_message)
    player = input('Hey Player! What is your name?: ')
    run_game(player)


main()
