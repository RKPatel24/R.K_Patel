def setup_logger():
    logging.basicConfig(
        filename="notebook.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main():
    setup_logger()
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
            logging.info("Exiting program.")
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()