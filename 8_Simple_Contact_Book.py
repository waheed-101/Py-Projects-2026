"""
Simple Contact Book - A beginner Python project
Manage your contacts with add, view, search, and delete features
"""

def view_contacts(contact_list):
    print("\n--- Your Contacts ---")

    if not contact_list:
        print("Your Contact Book is empty.")
    else:
        # enumerate is a handy function to get both the index and the item.
        for i, contact in enumerate(contact_list):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")



def add_contact(contact_list):
    print("\n--- Add a New Contact ---")

    name = input("Enter Contact Name: ").strip()
    phone = input("Enter Contact's Phone Number: ").strip()
    email = input("Enter Contact's Email: ").strip()

    if name and phone and email:
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        contact_list.append(new_contact)
        print(f"\nContact for '{name}' added successfully")
    
    else:
        print(f"\nError: All fields are Required."
              f"       Contact not added.")



def search_contact(contact_list):
    print("\n--- Search for a Contact ---")

    if not contact_list:
        print(f"Your Contact book is empty. Nothing to search.")
        return
    
    search_term = input("Enter the name to search for: ").strip().lower()

    found_contacts = []

    for contact in contact_list:
        if search_term in contact['name'].lower():
            found_contacts.append(contact)

    if not found_contacts:
        print(f"\nNo contact found matching '{search_term}'.")
    else:
        print("\n--- Found Contacts ---")
        for i, contact in enumerate(found_contacts):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def delete_contact(contact_list):
    print("\n--- Delete a Contact ---")

    if not contact_list:
        print("Your Contact Book is empty.")
        return
    
    view_contacts(contact_list) # Show all contacts

    try:
        index = int(input("\nEnter the contact number to delete: ")) - 1
        if 0 <= index < len(contact_list):
            deleted = contact_list.pop(index)
            print(f"\nContact '{deleted['name']}' deleted successfully.")
        else:
            print("\nError: Invalid contact number.")
    except ValueError:
        print("\nError: Please enter a valid number.")




Contacts = []

print("\nWelcome to Your Simple Contact Book\n")

while True:
    print("\nMain Menu: ")
    print("---------------------------")
    print("|1. View all Contacts     |")
    print("|2. Add a new Contact     |")
    print("|3. Search for a Contact  |")
    print("|4. Delete a Contact      |")
    print("|5. Exit                  |")
    print("---------------------------\n")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        view_contacts(Contacts)

    elif choice == '2':
        add_contact(Contacts)

    elif choice == '3':
        search_contact(Contacts)

    elif choice == '4':
        delete_contact(Contacts)

    elif choice == '5':
        print("\n 😊 Have a nice day 😊 \n")
        break

    else:
        print("\nError: Invalid choice.\n       Please enter a number between 1 and 5.")        

