from collections import deque
import random
import os


def get_desktop_path():
    potential_paths = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop"),
        os.path.join(os.path.expanduser("~"), "Documents", "Desktop")
    ]
    for path in potential_paths:
        if os.path.exists(path):
            return path
    return None


desktop_path = get_desktop_path()


class PersonalAssistant:
    def __init__(self):
        self.tasks = []
        self.jokes = [
            "What is the name of a fish that knows Python? Python.",
            "What should a programmer say before leaving home? sudo, I'm leaving.",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why do Java developers wear glasses? Because they can’t C#.",
            "How do you comfort a JavaScript bug? You console it.",
            "Why do programmers hate nature? It has too many bugs.",
            "Why do programmers prefer using the terminal? Because it's where they feel most 'command'-ing."
        ]
        self.recent_jokes = deque(maxlen=3)

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, identifier):
        if identifier.isdigit():
            index = int(identifier) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        elif identifier in self.tasks:
            self.tasks.remove(identifier)
            print(f"Task '{identifier}' removed from the list.")
        else:
            print(f"Task '{identifier}' not found in the list.")

    def show_tasks(self):
        if self.tasks:
            print("Task list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("The task list is empty.")

    def tell_joke(self):
        available_jokes = [joke for joke in self.jokes if joke not in self.recent_jokes]
        if not available_jokes:
            self.recent_jokes.clear()
            available_jokes = self.jokes

        joke = random.choice(available_jokes)
        self.recent_jokes.append(joke)
        print(joke)

    def find_notepads_on_desktop(self):
        if not desktop_path:
            print("Desktop path not found.")
            return []
        notepad_files = [f for f in os.listdir(desktop_path) if f.endswith(".txt")]
        if notepad_files:
            print("Found notepad files on desktop:")
            for index, file in enumerate(notepad_files, start=1):
                print(f"{index}. {file}")
            return notepad_files
        else:
            print("No notepad files found on the desktop.")
            return []

    def open_notepad(self, file_name):
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        file_path = os.path.join(desktop_path, file_name)

        if os.path.isfile(file_path):
            os.system(f'notepad {file_path}')
            print(f"Opened notepad: {file_path}")
        else:
            print(f"File '{file_name}' not found.")

    def read_notepad(self, file_name):
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        file_path = os.path.join(desktop_path, file_name)

        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print("File content:")
                print(content)
        else:
            print(f"File '{file_name}' not found.")

    def edit_notepad(self, file_name):
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        file_path = os.path.join(desktop_path, file_name)

        if os.path.isfile(file_path):
            new_content = input("Enter the new content for the file: ")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print("File content updated.")
        else:
            print(f"File '{file_name}' not found.")


if __name__ == "__main__":
    assistant = PersonalAssistant()


    def get_valid_choice():
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a task")
            print("2. Remove a task")
            print("3. Show all tasks")
            print("4. Hear a joke")
            print("5. Find notepad files on desktop")
            print("6. Open notepad")
            print("7. Read notepad")
            print("8. Edit notepad")
            print("9. Exit")
            choice = input("Enter the number of your choice: ").strip()
            if choice in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                return choice
            print("Invalid choice. Please enter a number between 1 and 9.")


    while True:
        choice = get_valid_choice()

        if choice == "1":
            task = input("Enter the task to add: ").strip()
            if task:
                assistant.add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            task = input("Enter the task name or number to remove: ").strip()
            if task:
                assistant.remove_task(task)
            else:
                print("Task identifier cannot be empty.")
        elif choice == "3":
            assistant.show_tasks()
        elif choice == "4":
            assistant.tell_joke()
        elif choice == "5":
            assistant.find_notepads_on_desktop()
        elif choice == "6":
            file_name = input("Enter the notepad file name to open: ").strip()
            assistant.open_notepad(file_name)
        elif choice == "7":
            file_name = input("Enter the notepad file name to read: ").strip()
            assistant.read_notepad(file_name)
        elif choice == "8":
            file_name = input("Enter the notepad file name to edit: ").strip()
            assistant.edit_notepad(file_name)
        elif choice == "9":
            print("Goodbye!")
            break
