class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}\n{self.content}\n"

class NoteView:
    def display_message(self, message):
        print(message)

    def get_note_details(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        return title, content

    def get_note_index(self):
        return int(input("Enter the index of the note: "))
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
        if not notes:
            self.view.display_message("No notes found.")
        else:
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note}")

    def delete_note(self):
        index = self.view.get_note_index()
        if self.model.delete_note_by_index(index):
            self.view.display_message("Note deleted successfully.")
        else:
            self.view.display_message("Invalid note index.")
def save_notes_to_file(file_name, notes):
    with open(file_name, "w") as file:
        for note in notes:
            file.write(f"{note.title}\n{note.content}\n---\n")

def load_notes_from_file(file_name):
    notes = []
    try:
        with open(file_name, "r") as file:
            data = file.read().split("---")

        for note_data in data:
            lines = note_data.strip().split("\n")
            if len(lines) >= 2:
                title, content = lines[0], "\n".join(lines[1:])
                notes.append(Note(title, content))
    except FileNotFoundError:
        print("File not found. Creating a new one...")
    return notes
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

    def delete_note_by_index(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            return True
        return False

    def save_notes(self):
        save_notes_to_file("notes.txt", self.notes)
        self.view.display_message("Notes saved to file.")


def main():
    notebook = ENotebook()

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Save Notes to File")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            title, content = input("Enter note title: "), input("Enter note content: ")
            notebook.controller.add_note()

        elif choice == "2":
            notebook.controller.view_notes()

        elif choice == "3":
            notebook.controller.delete_note()

        elif choice == "4":
            notebook.save_notes()

        elif choice == "5":
            notebook.save_notes()
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
