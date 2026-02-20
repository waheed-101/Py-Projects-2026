''' Guest List Manager '''
# Description: A simple command-line application to manage
#              a guest list. Supports adding, removing, and
#              displaying guests with duplicate detection.


def display_menu():
    ''' Display the main menu options '''
    print("\n" + "=" * 40)
    print("        GUEST LIST MANAGER")
    print("=" * 40)
    print("1. Show All Guests")
    print("2. Add New Guest")
    print("3. Remove Guest")
    print("4. Guest Summary")
    print("5. Exit Program")
    print("-" * 40)


def show_all_guests(guest_list):
    ''' Display all guests in the list '''
    if not guest_list:
        print("\nError: ❌ No guests in your list yet!")
        return
    
    print(f"\n📋 Your Guest List ({len(guest_list)}) guests:")
    print("-" * 30)
    
    for idx, guest in enumerate(guest_list, 1):
        print(f"{idx:2d}. {guest}")


def add_new_guests(guest_list):
    ''' Add a new guest to the list '''
    while True:
        name = input("\n👤 Enter guest name: ").strip()
        
        if not name:
            print("Error: ⚠️ Name cannot be empty. Please try again.")
            continue

        # check for duplicates (case-insensitive)
        existing_guest = None
        for guest in guest_list:
            if guest.lower() == name.lower():
                existing_guest = guest
                break

        if existing_guest:
            print(f"Error: ⚠️ '{name}' already exists as '{existing_guest}'")
            choice = input("Add anyway? (y/n): ").lower().strip()
            if choice not in ['y', 'yes']:
                print("❌ Guest not added.")
                return
        guest_list.append(name)
        print(f"✅ '{name}' added successfully!")
        return
    

def remove_guest(guest_list):
    """Remove a guest from the list"""
    if not guest_list:
        print("\n❌ No guests to remove!")
        return
    
    show_all_guests(guest_list)
    
    try:
        choice = int(input(f"\nEnter number to remove (1-{len(guest_list)}): "))
        if 1 <= choice <= len(guest_list):
            removed = guest_list.pop(choice - 1)
            print(f"✅ '{removed}' removed successfully!")
        else:
            print(f"Error: ❌ Please enter a number between 1 and {len(guest_list)}")
    except ValueError:
        print("Error: ❌ Invalid input. Please enter a number.")

def show_summary(guest_list, host_name):
    """Show final summary of guests"""
    print("\n" + "="*50)
    print("           GUEST LIST SUMMARY")
    print("="*50)
    print(f"Host: {host_name}")
    print(f"Total Guests: {len(guest_list)}")
    
    if guest_list:
        print("\nGuest List:")
        for idx, guest in enumerate(guest_list, 1):
            print(f"  {idx}. {guest}")
    else:
        print("\nNo guests registered.")
    print("="*50)

def get_yes_no(prompt):
    """Get yes/no input from user"""
    while True:
        choice = input(prompt + " (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")

def main():
    ''' Main Program Loop '''
    print("🎉 Welcome to Guest List Manager!")
    host_name = input("What's your name? ").strip() or "Host"
    guests = []

    while True:
        display_menu()

        try:
            choice = input("Choose an option (1-5): ").strip()

            if choice == '1':
                show_all_guests(guests)
            
            elif choice == '2':
                add_new_guests(guests)

            elif choice == '3':
                remove_guest(guests)

            elif choice == '4':
                show_summary(guests, host_name)

            elif choice == '5':
                if get_yes_no("\nAre you sure you want to exit?"):
                    show_summary(guests, host_name)
                    print(f"\n👋 Goodbye {host_name}!\nThanks for using Guest List Manager!")
                    break
            else:
                print("Error: ❌ Invalid choice. Please select 1-5.")
        except KeyboardInterrupt:
            print("\n\nError: 👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: ❌ An error occurred: {e}")

if __name__ == "__main__":
    main()