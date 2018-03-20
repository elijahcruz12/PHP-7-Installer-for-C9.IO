#!/usr/bin/python
from time import sleep
import os, sys, signal

from time import sleep
import os, sys, signal

def handler(signal, frame):
    print R + "Interrupted! Stopping..." + W
    sys.exit(1)

signal.signal(signal.SIGINT, handler)


# Global variables for color
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

installerHead = """
  ___________________
  PHP 7 Installer for c9.io!
  Script V1.0
  Installer created by Elijah Cruz
  
  Written in Python.
  
  -------------------
  Please before installing be sure you have
  stopped Apache...
  Also please make sure your command line is 
  "13 lines tall and 31 columns wide...
  
  In other words: Please make your command line 
  large as it will speed up the process.
    """
    
print G + installerHead
raw_input("Press Enter to continue...") # Waits for Enter

print O + "Updating Repositories..." + W
sleep(1.5)
os.system("sudo add-apt-repository ppa:ondrej/php -y")
os.system("sudo apt-get update -y")
print O + "Intalling PHP v7..." + W
sleep(1.5)
os.system("sudo apt-get install php7.0-curl php7.0-cli php7.0-dev php7.0-gd php7.0-intl php7.0-mcrypt php7.0-json php7.0-mysql php7.0-opcache php7.0-bcmath php7.0-mbstring php7.0-soap php7.0-xml php7.0-zip -y")

print O + "Moving File To Prevent Error..." + W
sleep(1.5)
os.system("sudo mv /etc/apache2/envvars /etc/apache2/envvars.bak")

print R + "Removing PHP v5..."
sleep(1.5)
os.system("sudo apt-get remove libapache2-mod-php5 -y")

print R + "Removing libapache2-mod-php5..."
sleep(1.5)
os.system("sudo apt-get remove libapache2-mod-php5 -y")

print G + "Installing libapache2-mod-php7..."
sleep(1.5)
os.system("sudo apt-get install libapache2-mod-php7.0 -y")

print O + "Moving Envars File Back..."
sleep(1.5)
os.system("sudo cp /etc/apache2/envvars.bak /etc/apache2/envvars")

print O + "Getting PHP Version..."
os.system("php -v")

print O + "PHP v7 is now installed."
