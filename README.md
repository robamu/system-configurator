# Command Line Configurator Utility

This is a personal README which includes steps and utilities to set up a convenient development
environment on Windows and Linux. It includes a Python script to set up the command line and
development environment in a new Unix environment or for MinGW and git on Windows.

# Windows

1. Install [Notepad++](https://notepad-plus-plus.org/downloads/)
2. Install [Sublime Text](https://www.sublimetext.com/)
3. Install [MSYS2](https://www.msys2.org/)
4. Install [Windows Terminal](https://www.microsoft.com/de-de/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab)
5. Install [git for Windows](https://git-scm.com/download/win)
6. Install [VS Code](https://code.visualstudio.com/)
7. Install [Ninja](https://ninja-build.org/)
8. Install [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

On Windows, a `.bash_aliases` file will be created both for `MinGW64` and `git`.
Currently, the user needs to take care of enabling use of the `bash_aliases` file in the 
`.bashrc` file of MinGW64 by uncommenting the respective lines.

# Ubuntu

Python script to install various useful programs can be found in `Ubuntu` folder

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
