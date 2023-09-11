import subprocess


def run_program():
    try:
        subprocess.run(["python", "main.py"])
    except FileNotFoundError:
        print("Error: Unable to find the main.py file.")
    except Exception as e:
        print(f"An error occurred while running the program.\n{e}")


def handle_command(command):
    lower_command = command.lower()
    if lower_command == "run":
        run_program()
    elif lower_command == "help":
        print("Available commands:")
        print(" - run: Run the main.py program")
        print(" - help: Show available commands")
        print(" - exit: Quit the chatbot")
    elif lower_command == "exit":
        print("Goodbye!")
        exit()
    else:
        print("Invalid command. Type 'help' to see available commands.")


while True:
    user_input = input(">>> ")
    handle_command(user_input)
