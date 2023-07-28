class NoteView:
    def display_message(self, message):
        print(message)

    def get_note_details(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        return title, content

    def display_notes(self, notes):
        if not notes:
            print("No notes found.")
        else:
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.title}\n{note.content}\n")
class NoteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_note(self):
        title, content = self.view.get_note_details()
        self.model.add_note(title, content)
        self.view.display_message("Note added successfully.")

    def view_notes(self):
        notes = self.model.get_notes()
        self.view.display_notes(notes)
from models import Note
from views import NoteView
from controllers import NoteController
from utils import save_notes_to_file, load_notes_from_file


class ENotebook:
    def __init__(self):
        self.notes = load_notes_from_file("notes.txt")
        self.view = NoteView()
        self.controller = NoteController(self, self.view)

    def add_note(self, title, content):
        self.notes.append(Note(title, content))

    def get_notes(self):
        return self.notes

    def save_notes(self):
        save_notes_to_file("notes.txt", self.notes)
        self.view.display_message("Notes saved to file.")


def main():
    notebook = ENotebook()

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            title, content = input("Enter note title: "), input("Enter note content: ")
            notebook.controller.add_note()

        elif choice == "2":
            notebook.controller.view_notes()

        elif choice == "3":
            notebook.save_notes()
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "main":
    main()
