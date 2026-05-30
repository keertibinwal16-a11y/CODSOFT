contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    elif choice == "2":
        if contacts:
            print("\n--- Contact List ---")
            for name, details in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
        else:
            print("No contacts found!")

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in contacts:
            details = contacts[search]
            print(f"\nName: {search}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
        else:
            print("Contact not found!")

    elif choice == "4":
        update = input("Enter contact name to update: ")

        if update in contacts:
            phone = input("Enter new Phone Number: ")
            email = input("Enter new Email: ")
            address = input("Enter new Address: ")

            contacts[update] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        delete = input("Enter contact name to delete: ")

        if delete in contacts:
            del contacts[delete]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice! Please try again.")
