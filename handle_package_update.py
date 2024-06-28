import os 
import subprocess

def update_environment():
    os.system("sudo apt-get update") # Updates the package lists for packages that must be upgraded, $ also for new packages that were recently added to the repositories
    os.system("sudo apt-get upgrade") # Updates the current OS. NB/ This command does not upgrade the OS to a higher version. I.e, if you run the cmd on Debian V8, it will not get Debian V9.
    os.system("sudo apt-get dist-upgrade") # Downloads and installs updates for all installed packages 
    
update_environment()