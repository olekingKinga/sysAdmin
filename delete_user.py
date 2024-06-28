# function to remove user from the system 
# tested and working 

import os # Import the OS module from the Py std library

def remove_user(): # define the function
    confirm = 'N' # Define a variable and initialize it
    while confirm != 'Y': # Start of loop condition 
        username = input("Enter the name of the user to remove: ") # request user for name 
        print("Remove the user : '" + username + "'? (Y/N)") # prompt use name for confirmation 
        confirm = input().upper() # Convert user input into upper case
    os.system("sudo userdel -r --force " + username) # use OS module and system() function to run command

remove_user()  # call the function