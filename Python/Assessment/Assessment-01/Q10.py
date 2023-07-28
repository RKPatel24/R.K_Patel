def save_notes_to_file(file_name, notes):
    with open(file_name, "w") as file:
        for note in notes:
            file.write(f"{note.title}\n{note.content}\n---\n")
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
        note = Note(title, content)
        self.notes.append(note)
        self.controller.save_notes()

    def get_notes(self):
        return self.notes

    def delete_note_by_index(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            self.controller.save_notes()
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
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title, content = input("Enter note title: "), input("Enter note content: ")
            notebook.controller.add_note(title, content)

        elif choice == "2":
            notes = notebook.get_notes()
            notebook.view.display_notes(notes)

        elif choice == "3":
            try:
                index = int(input("Enter the index of the note to delete: "))
                if notebook.delete_note_by_index(index):
                    print("Note deleted successfully.")
                else:
                    print("Invalid note index.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "4":
            notebook.controller.save_notes()
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()