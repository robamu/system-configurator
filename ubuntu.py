#!/usr/bin/env python3
import os

MINIMIZE_TO_DOCK_CMD = "gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'"

def main():
    os.system(MINIMIZE_TO_DOCK_CMD)
    os.system("snap install spotify")
    os.system("snap install discord")
    os.system("sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons")


if __name__ == "__main__":
    main()

