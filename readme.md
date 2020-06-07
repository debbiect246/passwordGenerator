# Password Generator

This app generates a password based on user preference.  Users can choose whether to have letters, special characters and/or numbers in a password.  

The entire project was built using django 3 and is an add on project following the bootcamp I participated in to help me improve my skills using django.

## Steps taken to complete this project

### Creating the django project

1. I created a folder in my local drive and named it passwordgeneratorproject.
2. I then went opened up the vscode editor and created a virtual environment by typing:
`pip install pipenv`
and then typing `pipenv shell` into the terminal.
3. Then I installed django by typing `pipenv install django`, this way django was installed inside my virtual environment.  A pipfile appeared showing that a virtual environment has been created.
4. I created a new django project inside my passwordgenerator project by typing `django-admin startproject passwordgeneratorproject .`  It was important that I put in the full stop at the end of the django-admin startproject so that the project was created inside my passwordgeneratorproject.
5. I ran the django server by typing `python manage.py runserver` and saw a messages saying *success you correctly installed django and a little rocket ship blasting off!*

### Setting up  a local and remote git repository

1. I typed `git init` to start a local repo.  I got a message from git to say that this had been successful.
2. I then created a repo in my git account after logging into github.
3. I then connected my project to the remote repo by typing `git remote add origin <https://github.com/the> id for my repo on github.
4. I then pushed my project so far to the remote repo by typing `git push -u origin master`, with a suitable commit message.  I looked in my github repo to ensure that my first commit had gone through.
