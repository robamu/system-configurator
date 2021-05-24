#!/usr/bin/env python3
import os
import enum
import webbrowser


MINIMIZE_TO_DOCK_CMD = "gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'"

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


class PromptType(enum.Enum):
    from enum import auto
    INSTALL = auto()
    ACTIVATE = auto()
    INTENT = auto()
    CUSTOM = auto()


def main():
    if prompt_yes_no("Minimize to Dock", PromptType.ACTIVATE):
        os.system(MINIMIZE_TO_DOCK_CMD)
    if prompt_yes_no("Spotify"):
        os.system("sudo snap install spotify")
    if prompt_yes_no("Discord"):
        os.system("sudo snap install discord")
    if prompt_yes_no("PyCharm Professional"):
        os.system("sudo snap install pycharm-professional --classic")
    if prompt_yes_no("Visual Studio Code"):
        os.system("sudo snap install --classic code")
    if prompt_yes_no("Python for VS Code"):
        os.system("code --install-extension ms-python.python")
    if prompt_yes_no("Eclipse"):
        print("Please use installer..")
        webbrowser.open("https://www.eclipse.org/downloads/packages/installer")
    if prompt_yes_no("add user to the dialout group", PromptType.INTENT):
        os.system("sudo adduser $USER dialout")
    if prompt_yes_no("ubuntu-restricted-extras and ubuntu-restricted-addons"):
        os.system("sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons")
    if prompt_yes_no("pip and gdebi"):
        os.system("sudo apt-get install gdebi python3-pip")
    if prompt_yes_no("branch display in terminal", PromptType.ACTIVATE):
        append_show_git_branch_setting()
    if prompt_yes_no("Docker"):
        install_docker()


def install_docker():
    # Add dependencies
    os.system(
        "sudo apt-get install apt-transport-https lsb-release ca-certificates"
        "gnupg curl"
    )
    # Add GPG key
    os.system(
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | "
        "sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg"
    )
    # Add package source
    os.system(
        "echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] "
        "https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | "
        "sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"
    )
    # Install docker engine
    os.system("sudo apt-get update")
    os.system("sudo apt-get install docker-ce docker-ce-cli containerd.io")
    if prompt_yes_no("add user to the docker group", PromptType.INTENT):
        os.system("sudo groupadd docker")
        os.system("sudo usermod -aG docker $USER")


def append_show_git_branch_setting():
	with open(os.path.join(os.path.expanduser('~'), '.bashrc'), "r+") as file:
		file.seek(0, os.SEEK_END)
		file.write("\n")
		file.write(SETTING_STRING)
		file.write("\n")
		print(".bashrc manipulated successfully to show git branch in terminal")


def prompt_yes_no(info_string: str, prompt_type: PromptType = PromptType.INSTALL):
    if prompt_type == PromptType.INSTALL:
        input_text = f"Do you want to install {info_string}? [y/n]: "
    elif prompt_type == PromptType.ACTIVATE:
        input_text = f"Do you want to activate {info_string}? [y/n]: "
    elif prompt_type == PromptType.INTENT:
        input_text = f"Do you want to {info_string}? [y/n]: "
    else:
        input_text = info_string
    while True:
        yes_or_no = input(input_text)
        if yes_or_no.lower() in ["y", "yes", "1"]:
            return True
        else:
            return False


if __name__ == "__main__":
    main()

