from contact_utils import (
    load_contacts,
    save_contacts,
    add_contact,
    view_contacts,
    search_contact,
    delete_contact
)


def display_menu():
    """Display the contact manager menu."""
    print("\n===== CONTACT MANAGER =====")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")


def main():
    """Run the contact manager application."""
    contacts = load_contacts()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
