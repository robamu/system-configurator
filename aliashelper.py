"""
Python utility to set up common and useful aliases
"""
import os
import sys

ALIASES_FILENAME = ".bash_aliases"
GENERIC_ALIASES = \
    f"alias gits='git status'\n" \
    f"alias gita='git add'\n" \
    f"alias gitaa='git add .'\n" \
    f"alias gitc='git commit'\n" \
    f"alias gitc='git commit'\n" \
    f"alias gitd='git diff'\n" \
    f"alias gitds='git diff --staged'\n" \
    f"alias gitm='git merge'\n" \
    f"alias gitpl='git pull'\n" \
    f"alias gitl='git log'\n" \
    f"alias gitpu='git push'\n" \
    f"alias gitrmu='git remote update --prune'\n\n" \
    f"alias ..='cd ..'\n" \
    f"alias ...='cd ../..'\n" \
    f"alias ....='cd ../../..'\n"
SOURCE_ALIAS = f"alias salias='cd ~ && source {ALIASES_FILENAME}'\n"
SHORTCUT_ALIAS_INCOMP = f"alias shortcut='cd ~ && "
EDITOR_SELECTION = {
    0: "gedit",
    1: "vim",
    2: "nano",
    3: "custom"
}

TEST_MODE = True
TEST_FILENAME = "test_aliases.txt"


def main():
    if sys.platform.startswith("win32"):
        # This is the path for git
        os.chdir(os.getenv('userprofile'))
    elif sys.platform.startswith("linux"):
        os.chdir("~")
    if os.path.isfile(".bash_aliases"):
        print(f"{ALIASES_FILENAME} file already exists")
        sys.exit(0)
    aliases_string_buf = GENERIC_ALIASES
    shortcut_alias = ""
    if sys.platform.startswith("win32"):
        notepad_alias = "alias notepad=\"/c/Program\ Files\ \(x86\)/Notepad++/notepad++.exe\"\n"
        aliases_string_buf += "\n" + notepad_alias
        shortcut_alias = SHORTCUT_ALIAS_INCOMP + f"notepad {ALIASES_FILENAME}\n"
    elif sys.platform.startswith("linux"):
        unix_editor = prompt_unix_editor()
        shortcut_alias = SHORTCUT_ALIAS_INCOMP + f"{unix_editor} {ALIASES_FILENAME}\n"
    else:
        print("Unknown OS")
    aliases_string_buf += shortcut_alias

    if not TEST_MODE:
        target_file = ALIASES_FILENAME
        with open(target_file, "w") as file:
            file.write(aliases_string_buf)
    else:
        target_file = TEST_FILENAME
        with open(target_file, "w") as file:
            file.write(aliases_string_buf)

    print(f"Generated {target_file} in {os.getcwd()}")


if __name__ == "__main__":
    main()


def prompt_unix_editor() -> str:
    print("Please enter editor by ID: ")
    while True:
        for key, value in EDITOR_SELECTION:
            print(f"{key}: {value}")
        editor_id = input("Please enter editor by ID: ")
        if not editor_id.isdigit():
            continue
        editor_id = int(editor_id)
        if editor_id == 3:
            custom_editor = input("Enter custom editor")
            confirm = input(f"Confirm selection: {custom_editor}")
            if confirm in ["y", "yes", "1"]:
                return custom_editor
        elif 0 < editor_id < 3:
            return EDITOR_SELECTION[editor_id]
