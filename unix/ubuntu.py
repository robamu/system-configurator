#!/usr/bin/env python3
import os
import enum
import webbrowser
from shutil import which, rmtree


MINIMIZE_TO_DOCK_CMD = (
    "gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'"
)

SETTING_STRING = (
    "# Show git branch name\n"
    "color_prompt=yes\n"
    "parse_git_branch() {\n"
    "  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\\1)/'\n"
    "}\n"
    'if [ "$color_prompt" = yes ]; then\n'
    r"  PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:"
    r"\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '"
    "\n"
    "else\n"
    r"  PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ "
    "'\n"
    "fi\n"
    "unset color_prompt force_color_prompt\n"
)

SETTING_STRING_BETTER = (
    "term_git_branch='/etc/term-git-branch'"
    "# Show git branch where applicable"
    "if [ -f  ${term_git_branch} ]; then"
    "    . ${term_git_branch}"
    "fi"
)


class PromptType(enum.Enum):
    from enum import auto

    INSTALL = auto()
    ACTIVATE = auto()
    INTENT = auto()
    CUSTOM = auto()


def main():
    if prompt_yes_no("xclip"):
        os.system("sudo apt-get install xclip")
    if prompt_yes_no("Minimize to Dock", PromptType.ACTIVATE):
        os.system(MINIMIZE_TO_DOCK_CMD)
    if prompt_yes_no("neovim"):
        install_neovim()
    if prompt_yes_no("zsh"):
        install_zsh()
    if prompt_yes_no("ripgrep (rg)"):
        install_ripgrep()
    if prompt_yes_no("find (fd)"):
        install_find()
    if prompt_yes_no("eza"):
        install_eza()
    if prompt_yes_no("bat"):
        install_bat()
    if prompt_yes_no("Rust"):
        install_rust()
    if prompt_yes_no("Spotify"):
        os.system("sudo snap install spotify")
    if prompt_yes_no("Discord"):
        os.system("sudo snap install discord")
    if prompt_yes_no("Visual Studio Code"):
        os.system("sudo snap install --classic code")
    if prompt_yes_no("Python for VS Code"):
        os.system("code --install-extension ms-python.python")
    if prompt_yes_no("add user to the dialout group", PromptType.INTENT):
        os.system("sudo adduser $USER dialout")
    if prompt_yes_no("ubuntu-restricted-extras and ubuntu-restricted-addons"):
        os.system(
            "sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons"
        )
    if prompt_yes_no("pip and gdebi"):
        os.system("sudo apt-get install gdebi python3-pip")
    if prompt_yes_no("cmake"):
        os.system("sudo apt-get install cmake")
    if prompt_yes_no("ninja"):
        os.system("sudo apt-get install ninja-build")
    if prompt_yes_no("KeyPassXC"):
        os.system("sudo snap install keepassxc")
    if prompt_yes_no("Sublime Text"):
        os.system(
            "wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | "
            "sudo apt-key add -"
        )
        os.system("sudo apt-get install apt-transport-https")
        os.system(
            'echo "deb https://download.sublimetext.com/ apt/stable/" | '
            "sudo tee /etc/apt/sources.list.d/sublime-text.list"
        )
        os.system("sudo apt-get update")
        os.system("sudo apt-get install sublime-text")
    if prompt_yes_no("branch display in terminal", PromptType.ACTIVATE):
        os.system("sudo cp scripts/term-git-branch /etc")
        append_show_git_branch_setting()
    # if prompt_yes_no("generate ssh key", PromptType.INTENT):
    #    generate_ssh_key()
    if prompt_yes_no("generate gpg key", PromptType.INTENT):
        generate_gpg_key()


def install_rust():
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")


def install_ripgrep():
    if which("cargo"):
        os.system("cargo install ripgrep --locked")
    else:
        os.system("sudo apt-get install ripgrep")


def install_eza():
    if which("cargo"):
        os.system("cargo install eza --locked")
    else:
        os.system("sudo apt-get install eza")


def install_find():
    if which("cargo"):
        os.system("cargo install fd-find --locked")
    else:
        os.system("sudo apt-get install fd-find")


def install_bat():
    if which("cargo"):
        os.system("cargo install bat --locked")
    else:
        os.system("sudo apt-get install bat")


def install_neovim():
    print("Installing neovim from sources..")
    os.system("git clone https://github.com/neovim/neovim.git")
    os.chdir("neovim")
    os.system("git checkout stable")
    os.system("make CMAKE_BUILD_TYPE=RelWithDebInfo")
    os.system("sudo make install")
    rmtree("neovim")
    print("Cloning neovim configuration")
    os.chdir("~/.config")
    os.system("git clone git@github.com:robamu/nvim-cfg.git nvim")


def generate_gpg_key():
    print("Existing GPG keys: ")
    os.system("gpg --list-keys")
    confirm = input("Do you want to generate a new gpg key? [y/n]: ")
    if confirm not in ["yes", "y", "1"]:
        return
    os.system("gpg --gen-key")
    print('GPG key generated, add it with "git config --global user.signkey <ID>"')
    print(
        'You can export the public key with "gpg --output public.pgp --armor --export <ID>"'
    )
    print(
        'You can export the private key with "gpg --output private.pgp --armor --export-secret-key <ID>"'
    )


def append_show_git_branch_setting():
    with open(os.path.join(os.path.expanduser("~"), ".bashrc"), "r+") as file:
        file.seek(0, os.SEEK_END)
        file.write("\n")
        file.write(SETTING_STRING_BETTER)
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


def generate_ssh_key():
    mail = ""
    while True:
        mail = input("Enter mail address used for ssh key: ")
        confirm = input(f"Confirm mail: {mail} [y/n]: ")
        if confirm in ["yes", "y", "1"]:
            break
    os.system(f"ssh-keygen -t ed25519 {mail}")
    print("SSH key generated, but still needs to be added with ssh-add")


def install_zsh():
    os.system("sudo apt-get install zsh")


if __name__ == "__main__":
    main()
