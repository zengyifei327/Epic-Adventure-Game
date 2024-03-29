# This Python script implements a text-based adventure game where the player navigates through
# a game board filled with different rooms. The player character can move in four directions
# (up, down, left, right) and encounters challenges along the way, such as guessing games.
# The goal of the game is to reach the bottom right corner of the board while staying alive.
import random


def print_game_intro():
    """
    Print the introduction for the Epic Adventure game.

    The function displays an ASCII art title followed by an introduction
    to the game, explaining the player's journey and objectives.
    """
    print(r"""
 _____ ____ ___ ____                                      
| ____|  _ \_ _/ ___|                                     
|  _| | |_) | | |                                         
| |___|  __/| | |___                                      
|_____|_|__|___\____|______ _   _ _____ _   _ ____  _____ 
   / \  |  _ \ \   / / ____| \ | |_   _| | | |  _ \| ____|
  / _ \ | | | \ \ / /|  _| |  \| | | | | | | | |_) |  _|  
 / ___ \| |_| |\ V / | |___| |\  | | | | |_| |  _ <| |___ 
/_/   \_\____/  \_/  |_____|_| \_| |_|  \___/|_| \_\_____|
    """)

    print("Welcome to Epic Adventure!")
    print("In this game, you will embark on an epic journey through mystical lands and treacherous dungeons.")
    print("You will encounter formidable foes, cunning puzzles, and hidden treasures along the way.")
    print("Your quest is to conquer the challenges and emerge victorious as the ultimate hero.")
    print("Prepare yourself for an unforgettable adventure!")
    print("To play the game, follow these instructions:")
    print("1. Enter the size of the map (rows and columns) when prompted.")
    print("2. Navigate through the rooms to reach the bottom right corner.")
    print("3. Beware of challenges and obstacles along the way.")
    print("4. Keep an eye on your character's health (HP) to survive.")
    print("5. Reach the destination while staying alive to win the game!")
    print("Let the journey begin!\n")


def get_map_size_from_user():
    """
    Prompt the user to enter the size of the map (rows and columns).

    :return: A tuple containing the number of rows and columns entered by the user
    """
    while True:
        try:
            rows = int(input("Enter the number of rows for the map: "))
            columns = int(input("Enter the number of columns for the map: "))
            if rows > 0 and columns > 0:
                return rows, columns
            else:
                print("Please enter positive integers for rows and columns.")
        except ValueError:
            print("Invalid input. Please enter integers for rows and columns.")


def make_board(rows, columns):
    """
    Make a game board with specific rows and columns.

    :param rows: a positive integers equal to or greater than 2
    :param columns: a positive integers equal to or greater than 2
    :precondition: rows must be a positive integer equal to or greater than 2
    :precondition: columns must be a positive integer equal to or greater than 2
    :postcondition: make a game board with specific rows and columns
    :return: a dictionary that contains rows * columns keys, where each key is a tuple
    that contains a set of coordinates, and each value is a string
    """
    rooms = ['Empty room', 'Garden', 'Living room']
    return {(row, column): random.choice(rooms) for row in range(rows) for column in range(columns)}


def make_character():
    """
    Make a game character.

    :postcondition: make a game character with 3 attributes of 0 X-coordinate, 0 Y-coordinate and 5 current HP
    :return: a dictionary that contains the following key:value pairs: 'X-coordinate': 0, 'Y-coordinate': 0,
    'Current HP': 5.
    >>> player1 = make_character()
    >>> player1
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> player2 = make_character()
    >>> player2
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}


def print_map(board, character):
    """
    Print a map based on the provided game board, showing the character's position with an 'X' in red.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character with 'X-coordinate', 'Y-coordinate',
                      and 'Current HP' keys
    :precondition: board must be a dictionary where keys are tuples representing coordinates,
                   and values are strings representing room contents
    :precondition: character must be a dictionary containing the keys 'X-coordinate', 'Y-coordinate',
                   and 'Current HP', representing the character's coordinates and current HP
    :postcondition: print a map representing the game board to the console with the character's position marked with 'X'
    """
    max_row = max(coord[0] for coord in board.keys())
    max_col = max(coord[1] for coord in board.keys())

    col_widths = {col: max(len(str(board.get((row, col), ""))) for row in range(max_row + 1)) for col in
                  range(max_col + 1)}

    print("+" + "+".join("-" * (col_widths[col] + 2) for col in range(max_col + 1)) + "+")

    for row in range(max_row + 1):
        for col in range(max_col + 1):
            if (row, col) == (character['Y-coordinate'], character['X-coordinate']):
                print(f"|     😀     ".center(col_widths[col]), end="")
            else:
                print(f"| {board.get((row, col), 'Empty room'):{col_widths[col]}} ", end="")
        print("|")
        print("+" + "+".join("-" * (col_widths[col] + 2) for col in range(max_col + 1)) + "+")


def describe_current_location(board, character):
    """
    Print user's current location, HP and destination.

    :param board: a dictionary that contains each room in the game board
    :param character: a dictionary that contains character's location and HP
    :precondition: board must be a dictionary that contains rows * columns keys, where each key is a tuple
    that contains a set of coordinates, and each value is a string
    :precondition: character must be a dictionary that contains the following keys with a value:
    'X-coordinate', 'Y-coordinate' and 'Current HP'
    :postcondition: print user's current location, HP and destination to the screen
    >>> my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> my_character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> describe_current_location(my_board, my_character)
    Your current location is (0, 1), this room is Empty room, your current HP is 5. You need to reach (1, \
1) while remaining alive to win the game.

    >>> my_board = {(0, 0): 'Living room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> my_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4}
    >>> describe_current_location(my_board, my_character)
    Your current location is (0, 0), this room is Living room, your current HP is 4. You need to reach (1, \
1) while remaining alive to win the game.
    """
    board_list = list(board)
    destination = board_list[-1]
    current_location = (character['X-coordinate'], character['Y-coordinate'])
    current_room_status = board[current_location]
    current_hp = character['Current HP']
    print(f'Your current location is {current_location}, this room is {current_room_status}, your current HP '
          f'is {current_hp}. You need to reach {destination} while remaining alive to win the game.')


def get_user_choice():
    """
    Get user's choice for next move.

    :postcondition: get user's choice for next move(top, right, bottom or left) represented as a string with a digit
    :return: a string, '1', '2', '3' or '4'
    """
    user_choice_direction = input('Where you wish to go next? Please enter the number of following:\n1. Up\n2. Right\n'
                                  '3. Down\n4. Left\n')
    while user_choice_direction.strip() not in ('1', '2', '3', '4'):
        user_choice_direction = input('Your input in invalid, please try again. Enter the number of following:\n1. Up\n'
                                      '2. Right\n3. Down\n4. Left\n')

    return user_choice_direction


def validate_move(board, character, direction):
    """
    Check if user's move is valid.

    :param board: a dictionary that contains each room in the game board
    :param character: a dictionary that contains character's location and HP
    :param direction: a string, '1', '2', '3' or '4'
    :precondition: board must be a dictionary that contains rows * columns keys, where each key is a tuple
    that contains a set of coordinates, and each value is a string
    :precondition: character must be a dictionary that contains the following keys with a value:
    'X-coordinate', 'Y-coordinate' and 'Current HP'
    :precondition: direction must be a string, '1', '2', '3' or '4'
    :postcondition: check if user's move is valid
    :return: a Boolean, True if the move is valid, False if the move is invalid
    >>> my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> my_character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> my_direction = '1'
    >>> validate_move(my_board, my_character, my_direction)
    True

    >>> my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> my_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4}
    >>> my_direction = '4'
    >>> validate_move(my_board, my_character, my_direction)
    False
    """
    user_location = [character['X-coordinate'], character['Y-coordinate']]
    if direction == '1':
        user_location[1] -= 1
    elif direction == '2':
        user_location[0] += 1
    elif direction == '3':
        user_location[1] += 1
    else:
        user_location[0] -= 1

    if tuple(user_location) in board:
        return True
    else:
        return False


def move_character(character, direction):
    """
    Move user's location based on their choice.

    :param character: a dictionary that contains character's location and HP
    :param direction: a string, '1', '2', '3' or '4'
    :precondition: character must be a dictionary that contains the following keys with a value:
    'X-coordinate', 'Y-coordinate' and 'Current HP'
    :precondition: direction must be a string with a digit, '1', '2', '3' or '4'
    :postcondition: change the value of the key 'X-coordinate' or 'Y-coordinate' in the dictionary assigned to variable
    character
    >>> my_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> my_direction = '1'
    >>> move_character(my_character, my_direction)
    >>> my_character
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}

    >>> my_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> my_direction = '2'
    >>> move_character(my_character, my_direction)
    >>> my_character
    {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
    """
    if direction == '1':
        character['Y-coordinate'] -= 1
    elif direction == '2':
        character['X-coordinate'] += 1
    elif direction == '3':
        character['Y-coordinate'] += 1
    else:
        character['X-coordinate'] -= 1


def check_for_foes():
    """
    Check if user encounters a foe.

    :postcondition: user will have 25% chance to encounter a foe(25% chance random_number is 1)
    :return: a Boolean, True if user encounters a foe(random_number is 1), False if not(random_number is not 1)
    """
    random_number = random.randint(1, 4)
    if random_number == 1:
        return True
    else:
        return False


def guessing_game(character):
    """
    Play a guessing game with user.

    Ask user to guess an integer number between 1 and 5 inclusive, if user guessed wrong, decrement user's HP by 1.

    :param character: a dictionary that contains character's location and HP
    :precondition: character must be a dictionary that contains the following keys with a value:
    'X-coordinate', 'Y-coordinate' and 'Current HP'
    :postcondition: print the guessing result to the screen, if user guessed wrong, decrement the value associated
     with the key 'Current HP' in the dictionary by 1
    """
    secret_number = random.randint(1, 5)
    user_guess = int(input('You just encountered a challenge, let us play a guessing game!\n'
                           'If you lose, you will lose 1 HP. You will die if your HP reaches 0.\n'
                           'Guess the secret number, enter an integer number between 1 and 5 inclusive: '))
    if user_guess != secret_number:
        character['Current HP'] -= 1
        print(f'Wrong number! The correct number is {secret_number}.You lost 1 HP. '
              f'Your current HP is {character["Current HP"]}')
    else:
        print('You guessed it right, well done!')


def is_alive(character):
    """
    Check if user is still alive.

    User is alive when HP is greater than 0.

    :param character: a dictionary that contains character's location and HP
    :precondition: character must be a dictionary that contains the following keys with a value:
    'X-coordinate', 'Y-coordinate' and 'Current HP'
    :postcondition: check is user is still alive, user is alive when HP is greater than 0
    :return: a Boolean, True when HP is greater than 0, False when HP is 0
    >>> my_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> is_alive(my_character)
    True

    >>> my_character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 0}
    >>> is_alive(my_character)
    False
    """
    if character['Current HP'] > 0:
        return True
    else:
        return False


def check_if_goal_attained(board, character):
    """
    Check if user wins the game.

    User wins the game if they reach bottom right corner of the board.

    :param board: a dictionary that contains each room in the game board
    :param character: a dictionary that contains character's location and HP
    :precondition: board must be a dictionary that contains rows * columns keys, where each key is a tuple
    that contains a set of coordinates, and each value is a string
    :precondition: character must be a dictionary that contains the following keys with a value:
    'X-coordinate', 'Y-coordinate' and 'Current HP'
    :return: a Boolean, True if user reaches bottom right corner of the board, False if not
    >>> my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> my_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> check_if_goal_attained(my_board, my_character)
    True

    >>> my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> my_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    >>> check_if_goal_attained(my_board, my_character)
    False
    """
    board_list = list(board)
    destination = board_list[-1]
    current_location = (character['X-coordinate'], character['Y-coordinate'])
    if current_location == destination:
        return True
    else:
        return False


def print_win():
    """
    Print a congratulatory message and an ASCII art for winning the game.
    """
    print(r"""
                                     .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
     __   _____  _   _  __        _____ _   _ _ _ _ 
    \ \ / / _ \| | | | \ \      / /_ _| \ | | | | |
     \ V / | | | | | |  \ \ /\ / / | ||  \| | | | |
      | || |_| | |_| |   \ V  V /  | || |\  |_|_|_|
      |_| \___/ \___/     \_/\_/  |___|_| \_(_|_|_)
    """)


def game():
    """
    Run the game.
    """
    print_game_intro()
    rows, columns = get_map_size_from_user()
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    user_alive = True
    print_map(board, character)
    describe_current_location(board, character)

    while user_alive and not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)

        if valid_move:
            move_character(character, direction)
            print_map(board, character)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()

            if there_is_a_challenger:
                guessing_game(character)
                user_alive = is_alive(character)
                if not user_alive:
                    print('Oops, you died. Game over! (o;TωT)o')
                    break

            achieved_goal = check_if_goal_attained(board, character)

        else:
            print('You cannot go to that direction! Please choose again.')
            print_map(board, character)

    if user_alive:
        print_win()


def main():
    """
    Run the program.
    """
    game()


if __name__ == "__main__":
    main()