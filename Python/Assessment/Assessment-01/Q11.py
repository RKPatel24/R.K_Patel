class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}\n{self.content}\n"
# notebook.py

from utils import save_notes_to_file, load_notes_from_file
from note import Note


class ENotebook:
    def __init__(self):
        self.notes = load_notes_from_file("notes.txt")

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()

    def get_notes(self):
        return self.notes

    def delete_note_by_index(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            self.save_notes()
            return True
        return False

    def save_notes(self):
        save_notes_to_file("notes.txt", self.notes)
# views.py

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
# controllers.py

from notebook import ENotebook
from views import NoteView


class NoteController:
    def __init__(self):
        self.notebook = ENotebook()
        self.view = NoteView()

    def add_note(self):
        title, content = self.view.get_note_details()
        self.notebook.add_note(title, content)
        self.view.display_message("Note added successfully.")

    def view_notes(self):
        notes = self.notebook.get_notes()
        self.view.display_notes(notes)

    def delete_note(self):
        try:
            index = int(input("Enter the index of the note to delete: "))
            if self.notebook.delete_note_by_index(index):
                print("Note deleted successfully.")
            else:
                print("Invalid note index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
# main.py

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