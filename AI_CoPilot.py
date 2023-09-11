import subprocess
Sorry, I didn't realize that I'm already in a repository. I am unable to commit any changes to your code. However, here's the optimized version of your Python script:

```python

AVAILABLE_COMMANDS = {
    "run": "Run the main.py program",
    "help": "Show available commands",
    "exit": "Quit the chatbot"
}


def run_program():
    try:
        subprocess.run(["python", "main.py"])
    except FileNotFoundError:
        print("Error: Unable to find the main.py file.")
    except Exception as e:
        print(f"An error occurred while running the program.\n{e}")


def handle_command(command):
    lower_command = command.lower()
    if lower_command in AVAILABLE_COMMANDS:
        if lower_command == "run":
            run_program()
        elif lower_command == "help":
            print("Available commands:")
            for cmd, description in AVAILABLE_COMMANDS.items():
                print(f" - {cmd}: {description}")
        elif lower_command == "exit":
            print("Goodbye!")
            exit()
        return
    print("Invalid command. Type 'help' to see available commands.")


while True:
    user_input = input(">>> ")
    handle_command(user_input)
```

I hope this helps optimize your script. Let me know if you have any further questions!
