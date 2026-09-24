#import os 
import subprocess

def update_environment():
    print("Updating package information...")
    subprocess.run(
        ["sudo", "apt-get", "update"])

    print("Upgrading installed packages...")
    subprocess.run(
        ["sudo", "apt-get", "upgrade", "-y"])

    print("Downloading and installing updates for all installed packages...")
    subprocess.run(
        ["sudo", "apt-get", "dist-upgrade"])
    
update_environment()