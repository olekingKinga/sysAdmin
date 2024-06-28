# Script to add a new user to the Linux Account 
# Correct
import os

def new_user(): 
    confirm = "N" # container / bag 
    while confirm != "Y": # condition
        username = input("Enter the name of the user to add: ")  # Bag username that store user input which is the name of the user
        print("Use the username '" + username + "'? (Y/N)") 
        confirm = input().upper()
        
    os.system("sudo adduser --force-badname " + username)

new_user()