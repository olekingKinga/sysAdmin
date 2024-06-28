# function to remove user from the system 
# tested and working 

import os # Import the OS module from the Py std library

def remove_user(): # define the function
    confirm = 'N'
    while confirm != 'Y':
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r --force " + username)

remove_user() 