#!/usr/bin/env python3
import os

MINIMIZE_TO_DOCK_CMD = "gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'"

def main():
    os.system(MINIMIZE_TO_DOCK_CMD)
    os.system("sudo snap install spotify")
    os.system("sudo snap install discord")
	os.system("sudo snap install --classic code")
    os.system("sudo adduser $USER dialout")
    os.system("sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons")
    os.system("sudo apt-get python3-pip")


if __name__ == "__main__":
    main()

