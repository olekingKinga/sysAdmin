import os 
import subprocess

#Function to add a user to a group 
# Part one
# Correct

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE, text=True).communicate()[0] # tuple ()
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output) #\r\n New line, a tab space
    chosenGroups = str(input("Groups: "))
    
    # Adding a user to a group - Part 2
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    
    print("Add To:")
    found = True
    groupString = ""
    
    # Adding a user to a group - Part 3
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp: # Confirming the grp is available / Exists
                found = True
                print("- Existing/Selected Group/s : " + grp)
                groupString = groupString + grp + ","
                
        if found == False:
            print("- New Group not existing : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
        
    #Adding a user to a group - Part 4 
    #The while loop exits if the user enters n, N, y, or Y. 
    #The input.upper() converts the user input to upper case.
     
    groupString = groupString[:-1] + " "
    confirm = ""
    while confirm != "Y" and confirm != "N":
        print("Ädd user '" + username + "' to these groups? (Y/N)")
        confirm = input().upper()
    if confirm == "N":
        print("User '" + username + "' not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + username)
        print("User '" + username + "' added")
    
    

add_user_to_group()