#!/usr/bin/env python3
import os

MINIMIZE_TO_DOCK_CMD = "gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'"
INSTALL_SPOTIFY = True
INSTALL_DISCORD = True
INSTALL_EXTRA_PACKAGES = True
INSTALL_PIP = True
SHOW_GIT_BRANCH_TERMINAL = True

SETTING_STRING = \
    "# Show git branch name\n" \
    "color_prompt=yes\n" \
    "parse_git_branch() {\n" \
    "  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\\1)/'\n" \
    "}\n" \
    "if [ \"$color_prompt\" = yes ]; then\n" \
    r"  PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:" \
    r"\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '" "\n" \
    "else\n" \
    r"  PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ " "'\n" \
    "fi\n" \
    "unset color_prompt force_color_prompt\n"


def main():

    os.system(MINIMIZE_TO_DOCK_CMD)
    if INSTALL_SPOTIFY:
        os.system("sudo snap install spotify")
    os.system("sudo snap install discord")
    os.system("sudo snap install --classic code")
    os.system("sudo adduser $USER dialout")
    os.system("sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons")
    os.system("sudo apt-get python3-pip")

    if SHOW_GIT_BRANCH_TERMINAL:
        append_show_git_branch_setting()


def append_show_git_branch_setting():
	with open(os.path.join(os.path.expanduser('~'), '.bashrc'), "r+") as file:
		file.seek(0, os.SEEK_END)
		file.write("\n")
		file.write(SETTING_STRING)
		file.write("\n")
		print(".bashrc manipulated successfully to show git branch in terminal")


if __name__ == "__main__":
    main()

