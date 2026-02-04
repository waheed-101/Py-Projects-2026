# Password Authentication is the process of checking the identity of a user. 

''' The getpass module provides a function called getpass() that hides the password characters as you type them (for security)'''
import getpass

database = {
    "abdulwaheed": "yuyu12!@",
    "waheed": "123$%^",
    "waheedzama": "qwaszx12!@34"
}

username = input("Enter Your Username: ")

'''
This flag will track whether the user has successfully logged in
Default: We assume the user is NOT authenticated until proven otherwise.
'''
authenticated = False

# Check if username exists:
if username in database:
    attempts = 3
    while attempts > 0:
        password = getpass.getpass("Enter Your Password: ")
        if password == database[username]:
            authenticated = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong Password. {attempts} attempts remaining.")
            else:
                print(f"Too many failed attempts. Access denied.")
else:
    print(f"Username '{username}' not found.")

if authenticated:
    print(f"\nVerified: {username}")
else:
    print(f"\nNot Verified: {username}")