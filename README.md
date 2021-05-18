# Command Line Configurator Utility

This is a personal README which includes steps and utilities to set up a convenient development
environment on Windows and Linux. It includes a Python script to set up the command line and
development environment in a new Unix environment or for MinGW and git on Windows.

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

# Generating and signing commits with GPG

Follow [this guide](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work).

After generating a key, the secret key can be exported with the following command

```sh
gpg --output private.pgp --armor --export-secret-key <username/mail or key ID>
```

And then import this file with `gpa` or Kleopatra.

You can export the public key with the following command

```sh
gpg --output public.pgp --armor --export <username/mail or key ID>
```

This key can be uploaded to Github, Gitlab to allow verification of commits
