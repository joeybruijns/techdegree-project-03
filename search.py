import re

from utility import clear_screen


def print_entry(item):
    """Format for printing entries"""
    print('Date: ', item["Date"])
    print('Task: ', item["Task"])
    print('Time Spent: ', item["Time"])
    print('Notes: ', item["Notes"], '\n')


def search_by_date(search_date, row):
    """search the csv by date"""
    clear_screen()
    found = False
    for item in row:
        if item["Date"] == search_date:
            print_entry(item)
            found = True
    if found is False:
        print("No Entries Found..")


def search_by_time(integer, row):
    """search the csv by time"""
    clear_screen()
    found = False
    for item in row:
        if item["Time"] == str(integer):
            print_entry(item)
            found = True
    if found is False:
        print("No Entries Found..")


def exact_search(string, row):
    """search the csv with exact search (string)"""
    clear_screen()
    found = False
    for item in row:
        if string.lower() in item["Task"].lower() \
                or string.lower() in item["Notes"].lower():
            print_entry(item)
            found = True
    if found is False:
        print("No Entries Found..")


def regex_search(regex, row):
    clear_screen()
    """search the csv with a regex pattern"""
    found = False
    for item in row:
        if re.search(r'{}'.format(regex), item["Notes"]) \
                or re.search(r'{}'.format(regex), item["Task"]):
            print_entry(item)
            found = True
    if found is False:
        print("No Entries Found..")
