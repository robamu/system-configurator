# Command Line Configurator Utility

Python script to set up the command line and development environment in a new Unix environment or
for MinGW and git on Windows.

# Windows

1. Install [Notepad++](https://notepad-plus-plus.org/downloads/)
2. Install [MSYS2](https://www.msys2.org/)
3. Install [git for Windows](https://git-scm.com/download/win)
4. Install [gpg4win](https://www.gpg4win.org/)
5. Install [VS Code](https://code.visualstudio.com/)

On Windows, a `.bash_aliases` file will be created both for `MinGW64` and `git`.
Currently, the user needs to take care of enabling use of the `bash_aliases` file in the 
`.bashrc` file of MinGW64 by uncommenting the respective lines.

# Ubuntu


1. Install git, vim-gtk3 and GPA

```sh
sudo apt-get install git vim-gtk3 gpa
```

2. Install VS Code

```sh
sudo snap install --classic code
```
