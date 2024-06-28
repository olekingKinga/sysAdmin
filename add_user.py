# Script to add a new user to the Linux Account 
# Correct
import os #Import the os module to access interactive system() class 

def new_user(): # define and initialize the python funtion
    confirm = "N" # define and initialize a variable 
    while confirm != "Y": # run a condition check against defined variable
        username = input("Enter the name of the user to add: ")  # request user to insert his/her name
        print("Use the username '" + username + "'? (Y/N)") # pull given name and direct user with kind of input to provide next 
        confirm = input().upper() # convert user input into upper case if not
        
    os.system("sudo adduser --force-badname " + username) # use module os and system() function in it to run the bash command

new_user() # call the function