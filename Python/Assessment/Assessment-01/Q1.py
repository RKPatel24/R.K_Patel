import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class ENotebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def view_notes(self):
        if not self.notes:
            print("No notes found.")
        else:
            for index, note in enumerate(self.notes, start=1):
                print(f"{index}. {note.title}\n{note.content}\n")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
        else:
            print("Invalid note index.")

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            for note in self.notes:
                file.write(f"{note.title}\n{note.content}\n---\n")

    def load_from_file(self, file_name):
        if not os.path.exists(file_name):
            print("File not found.")
            return

        with open(file_name, "r") as file:
            data = file.read().split("---")

        for note_data in data:
            lines = note_data.strip().split("\n")
            if len(lines) >= 2:
                title, content = lines[0], "\n".join(lines[1:])
                self.add_note(title, content)

def main():
    notebook = ENotebook()
    file_name = "notes.txt"

    if os.path.exists(file_name):
        notebook.load_from_file(file_name)

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Save Notes to File")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            notebook.add_note(title, content)

        elif choice == "2":
            notebook.view_notes()

        elif choice == "3":
            index = int(input("Enter the index of the note to delete: "))
            notebook.delete_note(index)

        elif choice == "4":
            notebook.save_to_file(file_name)
            print("Notes saved to file.")

        elif choice == "5":
            notebook.save_to_file(file_name)
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
