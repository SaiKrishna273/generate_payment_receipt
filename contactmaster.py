contacts = []

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print("\nContact added successfully!\n")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("\nContact deleted successfully!\n")
            found = True
            break
    if not found:
        print("\nContact not found.\n")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    print()
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("No contact found with that keyword.\n")
    else:
        print()

def show_contacts():
    if not contacts:
        print("\nNo contacts available.\n")
    else:
        print("\nAll Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()


def menu():
    while True:
        print("=== ContactMaster Menu ===")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            show_contacts()
        elif choice == '5':
            print("\nThank you for using ContactMaster. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


menu()
