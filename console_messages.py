from colorama import Fore, Back

def welcome_message():
    """
    Prints the welcome message to
    the console with colours added
    from colorama
    """
    print(Fore.RED + f'\n    Welcome to EXO!\n')
    print(Fore.BLUE + " The game of X's and O's\n    Also known as...\n")
    print('       ' + Fore.YELLOW + Back.BLUE + ' T | I | C ' + Back.RESET)
    print('       ' + Fore.YELLOW + Back.BLUE + '-----------' + Back.RESET)
    print('       ' + Fore.YELLOW + Back.BLUE + ' T | A | C ' + Back.RESET)
    print('       ' + Fore.YELLOW + Back.BLUE + '-----------' + Back.RESET)
    print('       ' + Fore.YELLOW + Back.BLUE + ' T | O | E ' + Back.RESET)
    return ''


def winner_message():
    print(Fore.GREEN + '\n          Holy Smokes you won!')
    print(Fore.GREEN + '       Check out your score below')
    print(
        Fore.GREEN + ' How many times do you think you can win?' + Fore.RESET
        )
    return ''


def loser_message():
    print(Fore.RED + '             Oh No! You lost!')
    print(
        Fore.RED + 
        ' Keep trying, im sure you will win next time' + 
        Fore.RESET
        )


def tie_message():
    print(Fore.YELLOW + "        Well... It's a TIE!")
    print(Fore.YELLOW + " You're both winners in my eyes <3" + Fore.RESET)
