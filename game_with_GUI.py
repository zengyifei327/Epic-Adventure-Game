import tkinter as tk
from tkinter import simpledialog
from simple_game import (
    make_board,
    make_character,
    print_map,
    describe_current_location,
    get_user_choice,
    validate_move,
    move_character,
    check_for_foes,
    guessing_game,
    is_alive,
    check_if_goal_attained,
    print_win
)


class GameGUI:
    def __init__(self, master):
        self.message_text = None
        self.start_button = None
        self.map_frame = None
        self.master = master
        self.map_size = (0, 0)
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.map_frame = tk.Frame(self.master)
        self.map_frame.pack()

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.message_text = tk.Text(self.master, height=10, width=50)
        self.message_text.pack()

    def update_message(self, message):
        self.message_text.insert(tk.END, message + "\n")
        self.message_text.see(tk.END)  # Scroll to the bottom

    def update_map(self, board, character):
        for widget in self.map_frame.winfo_children():
            widget.destroy()

        for row, col in board:
            room_content = board[(row, col)]
            label_text = f"({row}, {col})\n{room_content}"
            label = tk.Label(self.map_frame, text=label_text, width=15, height=2, borderwidth=1, relief="solid")
            label.grid(row=row, column=col, padx=2, pady=2)

        character_label_text = (f"Character\n({character['X-coordinate']}, {character['Y-coordinate']})\nHP:"
                                f" {character['Current HP']}")
        character_label = tk.Label(self.map_frame, text=character_label_text, width=15, height=2, borderwidth=1,
                                   relief="solid")
        character_label.grid(row=character['Y-coordinate'], column=character['X-coordinate'], padx=2, pady=2)

    def start_game(self):
        self.get_map_size_from_user()

        board = make_board(*self.map_size)
        character = make_character()

        print_map(board, character)
        describe_current_location(board, character)

        while True:
            direction = get_user_choice()
            valid_move = validate_move(board, character, direction)

            if valid_move:
                move_character(character, direction)
                describe_current_location(board, character)
                print_map(board, character)
                there_is_a_challenger = check_for_foes()

                if there_is_a_challenger:
                    guessing_game(character)
                    user_alive = is_alive(character)
                    if not user_alive:
                        self.update_message("Oops, you died. Game over! (o;TωT)o")
                        break

                achieved_goal = check_if_goal_attained(board, character)
                if achieved_goal:
                    print_win()
                    self.update_message("Congratulations, you won the game!")
                    break

            else:
                self.update_message("You cannot go to that direction! Please choose again.")

    def get_map_size_from_user(self):
        user_input = simpledialog.askstring("Map Size", "Enter the number of rows and columns (e.g., 3 3):")
        if user_input:
            try:
                rows, columns = map(int, user_input.split())
                if rows > 0 and columns > 0:
                    self.map_size = (rows, columns)
                else:
                    self.update_message("Please enter positive integers for rows and columns.")
                    self.get_map_size_from_user()
            except ValueError:
                self.update_message("Invalid input. Please enter integers for rows and columns.")
                self.get_map_size_from_user()


def main():
    root = tk.Tk()
    root.title("Epic Adventure")
    GameGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()
