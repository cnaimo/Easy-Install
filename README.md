# Easy-Install
A short script to automate shell comands for painlessly installing multiple packages on Linux

# Contact
Questions? Feel free to reach out via my LinkedIn on my profile page. I'm also seeking employment in data science/finance!

# Concept
This project was created after having spent many hours installing various libraries and packages into Linux via terminal and waiting for commands to complete. Instead of entering commands line by line into the terminal and waiting, this Python script reads commands out of a text file and executes them one by one. Once a sudo command is called, enter your password and it is set for all remaining sudo commands.

# Usage
Clone this repository
```
git clone https://github.com/cnaimo/Easy-Install.git
cd Easy-Install
```

Create a text file with the desired shell commands to be executed. Optional comments can be added Python style with '#'.
An example command file is included (sample_installs.txt). Run easy_install.py, select your command file, and enter sudo passowrd if requested (required only once). Additional information is outputted to a logging file. 

```
Python3 easy_install.py
What instruction file would you like to run today?
YOUR-INSTRUCTION-FILE.txt
```

Always double check your list of commands before running them! 




