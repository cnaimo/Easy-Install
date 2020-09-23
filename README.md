[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![HitCount](http://hits.dwyl.io/cnaimo/Easy-Install.svg)](http://hits.dwyl.io/cnaimo/Easy-Install) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/pull/) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)  


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
An example command file is included (sample_installs.txt). Run easy_install.py, select your command file, and enter sudo password if requested (required only once). Additional information is outputted to a logging file. 

```
python3 easy_install.py
What instruction file would you like to run today?
YOUR-INSTRUCTION-FILE.txt
```

Always double check your list of commands before running them! 




