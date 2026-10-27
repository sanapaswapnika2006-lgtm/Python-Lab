
contacts = {}

while True:
    print("\n--- Phonebook Manager ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")

        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            contacts[name] = {
                "phone": phone,
                "email": email
            }
            print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email

            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        if not contacts:
            print("Phonebook is empty.")
        else:
            print("\nAll Contacts:")
            for name, details in contacts.items():
                print(name, "-", details)

            print("\nContact Names:", list(contacts.keys()))
            print("Contact Details:", list(contacts.values()))

            # List comprehension for searching by phone number
            phones = [
                name for name, details in contacts.items()
                if details["phone"]
            ]
            print("Contacts with phone numbers:", phones)

    elif choice == "6":
        print("Exiting Phonebook Manager.")
        break

    else:
        print("Invalid choice! Try again.")
