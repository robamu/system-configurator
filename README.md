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

## PowerShell

1. Allow executing PowerShell scripts
   ```ps
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
   ```

2. You can create a `Microsoft.Powershell_profile.ps1` file in the `MicrosoftPowerShell`
   folder which will be loaded when opening PowerShell. An example file is provided in the
   `Windows/PowerShell` folder

3. It is recommended to install [posh-git](https://github.com/dahlbyk/posh-git) for better
   git integration

# Ubuntu

Python script to install various useful programs can be found in `Ubuntu` folder.
Install git first to clone the script

```sh
sudo apt-get install git
```

List of reconfigured settings:

1. Minimize to dock enabled

List of installed tools and applications:

1. `neovim`
2. Spotify
3. Discord
4. PyCharm Professional
5. VS Code
6. `cmake`
7. `ninja`
8. KeyPassXC
9. Sublime Text
10. Rust
11. ripgrep
12. find (fd)
13. exa

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

# Dual-Boot Configuration

You can disable the grub timeout by opening the `/etc/default/grub` file and setting
`GRUB_TIMEOUT` to `-1`.

In dual-boot configuration, Linux might mess with Windows times or vice-versa. You can fix this
by running following command

```sh
timedatectl set-local-rtc 1 --adjust-system-clock
```
