# Python-Projects
This repository contains several Python applications of different level for educational/training purpose (for both Python and Git).

All of the applications will be written to be PEP8 compliant. 

- [Python-Projects](#python-projects)
  - [Basic level](#basic-level)
    - [Guess the number!](#guess-the-number)
    - [Email slicer](#email-slicer)
    - [Desktop notifier](#desktop-notifier)
  - [Intermediate level](#intermediate-level)
    - [Address book](#address-book)

## Basic level
### Guess the number!
This is a program which randomly chooses a number to guess and then the user will have a few chances to guess the number correctly. In each wrong attempt, the computer will give an hint to help the user to guess the number.

The user can choose the difficult of the game (simple or complex): this choise change the range of the number randomly generated and the number of attempts. 

### Email slicer
The email slicer is an handy program to get the username and domain name from an email address. It checks if the email provided by the user is valid or not (with a combination of if/elif conditions), with the related exceptions and hints for the user. 

### Desktop notifier 
A desktop notifier app runs on your system and it will be used to send you notifications after a specific interval of time.

The only dependence you need is pynotifier, which can be installed using the following command:

`$ pip install py-notifier`.

## Intermediate level
### Address book
This is an application that implement an address book with a CLI interface and a SQLite database to mantain all the information. The database is managed with SQLAlchemy ORM.
