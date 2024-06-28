import os
import subprocess
"""
> Used together, these two Linux commands are a good way to maintain an up-to-date and clean environment. 
> Correct 
"""
def clean_environment():
    os.system("sudo apt-get autoremove") # Removes dependencies that were installed with applications & are no longer used by anything on the system. 
    os.system("sudo apt-get autoclean") # Cleans obsolete deb-packages 

clean_environment()