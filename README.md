# aliases-helper

Python script to set up aliases in a new Unix environment or for MinGW and git on Windows
The flag `TEST_MODE` can be used to generate test files first before overwriting existing
`.bash_aliases` files.

# Windows

On Windows, a `.bash_aliases` file will be created both for `MinGW64` and `git`.
Currently, the user needs to take care of enabling use of the `bash_aliases` file in the 
`.bashrc` file of MinGW64 by uncommenting the respective lines.
