class NoteView:
    def display_message(self, message):
        print(message)

    def get_note_details(self):
        while True:
            title = input("Enter note title: ")
            if title.strip():
                break
            else:
                print("Invalid input. Note title cannot be empty. Please try again.")

        while True:
            content = input("Enter note content: ")
            if content.strip():
                break
            else:
                print("Invalid input. Note content cannot be empty. Please try again.")

        return title, content

    def display_notes(self, notes):
        if not notes:
            print("No notes found.")
        else:
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.title}\n{note.content}\n")
# controllers.py

from notebook import ENotebook
from views import NoteView


class NoteController:
    def __init__(self):
        self.notebook = ENotebook()
        self.view = NoteView()

    def add_note(self):
        while True:
            try:
                title, content = self.view.get_note_details()
                self.notebook.add_note(title, content)
                self.view.display_message("Note added successfully.")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("An unexpected error occurred. Please try again.")

    def view_notes(self):
        notes = self.notebook.get_notes()
        self.view.display_notes(notes)

    def delete_note(self):
        while True:
            try:
                index = int(input("Enter the index of the note to delete: "))
                if self.notebook.delete_note_by_index(index):
                    print("Note deleted successfully.")
                else:
                    print("Invalid note index. Please enter a valid index.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer index.")
            except Exception as e:
                print(f"Error: {e}")
                print("An unexpected error occurred. Please try again.")


from controllers import NoteController


def main():
    controller = NoteController()

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            controller.add_note()

        elif choice == "2":
            controller.view_notes()

        elif choice == "3":
            controller.delete_note()

        elif choice == "4":
            controller.notebook.save_notes()
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()