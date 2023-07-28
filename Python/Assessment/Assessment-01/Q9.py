def save_note_to_file(file_name, note):
    with open(file_name, "w") as file:
        file.write(f"{note.title}\n{note.content}")
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}\n{self.content}\n"

    def save_to_file(self):
        file_name = f"{self.title.lower().replace(' ', '_')}.txt"
        save_note_to_file(file_name, self)
from models import Note
from views import NoteView
from controllers import NoteController
from utils import save_note_to_file, load_notes_from_file


class ENotebook:
    def __init__(self):
        self.notes = load_notes_from_file("notes")
        self.view = NoteView()
        self.controller = NoteController(self, self.view)

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        note.save_to_file()

    def get_notes(self):
        return self.notes


def main():
    notebook = ENotebook()

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            title, content = input("Enter note title: "), input("Enter note content: ")
            notebook.controller.add_note(title, content)

        elif choice == "2":
            notes = notebook.get_notes()
            notebook.view.display_notes(notes)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
