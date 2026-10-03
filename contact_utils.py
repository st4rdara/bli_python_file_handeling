import json

def load_contacts():
    """Load contacts from the JSON file."""
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Collect and add a new contact."""
    print("\nAdd a new contact")

    name = input("Full name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully.")


def view_contacts(contacts):
    """Display all saved contacts."""
    print("\nYour contacts:")

    if len(contacts) == 0:
        print("No contacts found.")
        return

    for contact in contacts:
        print("--------------------")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def search_contact(contacts):
    """Search for a contact by name."""
    search = input("\nSearch for contact by name: ")

    found = False

    for contact in contacts:
        if search.lower() in contact["name"].lower():
            print("--------------------")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("No contact found.")


def delete_contact(contacts):
    """Delete a selected contact."""
    name = input("\nEnter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            confirm = input("Are you sure you want to delete this contact? (y/n): ")

            if confirm.lower() == "y":
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")

            return

    print("Contact not found.")
