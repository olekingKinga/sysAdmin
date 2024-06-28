import os 
import subprocess

def install_or_remove_packages():
    iOrR = ""
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
    if iOrR == "I": # Checks whether the user want wants to install or remove packages 
        iOrR = "install"
    elif iOrR == "R":
        iOrR = "remove"
             
    # Part 2
    print("Enter a list of packages to install")
    print("The list should be seperated by spaces, for example: ") # Describe how input should be like
    print(" package1 package2 package3")
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program.")
    packages = input().lower().split()
    if packages == "default": # Installs the default list of packages for the script if the user specifies default
        packages = defaultPackages
        
    if iOrR == "install":
        os.system("sudo apt-get install -y " + packages) # Calls the Linux command *sudo apt-get install * with the packages that you specified 
    
    elif iOrR == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            choice = input().upper() # Changes the user input into uppercase so that it can be compared 
            if choice == "Y":
                os.system("sudo apt-get --purge " + iOrR + " " + packages) # Calls the Linux command * sudo apt-get --purge remove* with the packages that you specified
                break
            elif choice == "N":
                os.system("sudo apt-get " + iOrR + " " + packages) # Calls the Linux command * sudo apt-get remove * with the packages that you specified
                break
        os.system("sudo apt autoremove") # Calls the Linux cmd * sudo apt autoremove *, which removes any old package files (if they exist)



install_or_remove_packages()      
        
    