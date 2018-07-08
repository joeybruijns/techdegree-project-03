import sys
import csv
import re

from utility import clear_screen
from entries import create_entry
from search import search_by_date, search_by_time, exact_search, regex_search


def new_search():
    """Asks the user if he/she wants
    to search for more entries or return to main menu
    """
    while True:
        user_input = input("[S]earch for More | [R]eturn to Main Menu ")
        if user_input.upper() == "S":
            search_entry()
        elif user_input.upper() == "R":
            start_screen()
        else:
            print("Try again!")


def open_file():
    """Opens the csv file and returns a list """
    with open('entries.csv', newline='') as csvfile:  # reads the csv file
        fieldnames = ["Date", "Task", "Time", "Notes"]
        entries = csv \
            .DictReader(csvfile, fieldnames=fieldnames, delimiter=',')
        return list(entries)


def search_entry():
    """Provides the user with a list of options to
    search the csv file and calls the appropriate search functions
    """
    clear_screen()
    print("Search for an Existing Entry:")
    print('''
    [A] Search by Date
    [B] Amount of Time
    [C] Exact Search
    [D] Regex Pattern
    [E] Return to Main Menu
    ''')

    while True:
        rows = open_file()
        user_input = input("How Do You Want To Search? ")

        if user_input.upper() == "A":  # Search by date
            clear_screen()
            print("All Existing Dates:")
            for row in rows:
                print(row["Date"])

            while True:
                search_date = input("Enter a Date from the List Above: ")
                if re.search(r'(\d\d/\d\d/\d\d\d\d)', search_date):
                    break
                print("Please, Enter a valid date!")
            search_by_date(search_date, rows)
            new_search()

        elif user_input.upper() == "B":  # search by time
            clear_screen()
            print("All Logged Time in Minutes:")
            for row in rows:
                print(row["Time"])

            while True:
                amount_of_time = input("Enter Time from the List Above: ")
                try:
                    int(amount_of_time)
                except ValueError:
                    print("Please enter a valid number!")
                else:
                    search_by_time(amount_of_time, rows)
                    new_search()

        elif user_input.upper() == "C":  # search by exact search
            clear_screen()
            try:
                user_input = \
                    str(input("Enter a String for Exact Search: "))
            except ValueError:
                print("Please, Enter a String of Characters")
            else:
                exact_search(user_input, rows)
                new_search()

        elif user_input.upper() == "D":  # search by regex pattern
            clear_screen()
            print("Enter a Regex Pattern! Example: \d{3}\s\d{3}")
            regex_input = input("Enter Pattern: ")
            regex_search(regex_input, rows)
            new_search()

        elif user_input.upper() == "E":  # return to main menu
            clear_screen()
            start_screen()

        else:
            print("Please, Enter a Valid Choice!")
            pass


def start_screen():
    """Runs the start screen and provides the user with the
    options to create a new entry, search for entries or quit
    """
    clear_screen()
    print("WorkLog | Track Your Time")
    print('''
    [A] Create New Entry
    [B] Search Entries
    [C] Quit Program
    ''')

    while True:
        user_input = input("What Would You Like To Do? ")

        if user_input.upper() == "A":
            create_entry()
            start_screen()
        elif user_input.upper() == "B":
            search_entry()
            start_screen()
        elif user_input.upper() == "C":
            print("Thanks! See You Next Time!")
            sys.exit()
        else:
            print("Please Enter A, B or C!")
            pass


start_screen()
