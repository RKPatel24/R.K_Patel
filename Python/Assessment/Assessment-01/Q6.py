class NoteView:
    def display_message(self, message):
        print(message)

    def get_note_details(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        return title, content

    def display_notes(self, notes):
        # ... (unchanged)
class NoteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_note(self):
        title, content = self.view.get_note_details()
        self.model.add_note(title, content)
        self.view.display_message("Note added successfully.")

    def view_notes(self):
        # ... (unchanged)
    