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
        print("3. Save Notes to File")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title, content = input("Enter note title: "), input("Enter note content: ")
            notebook.controller.add_note()

        elif choice == "2":
            notebook.controller.view_notes()

        elif choice == "3":
            notebook.save_notes()

        elif choice == "4":
            notebook.save_notes()
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


        if __name__ == "__main__":
    main()
