import csv
import datetime

from utility import clear_screen


def create_entry():
    """Collects user input: date, task name, time spent and notes.
    And writes it to a csv file
    """
    clear_screen()
    while True:  # collects a date
        try:
            input_date = input("Enter a date: (Format: DD/MM/YYYY) ")
            entry_day = int(input_date[:2])
            entry_month = int(input_date[3:5])
            entry_year = int(input_date[6:])
            datetime.date(entry_year, entry_month, entry_day)
            break
        except ValueError:
            print("Sorry, Not a Valid Date..")
    get_date = datetime\
        .date(entry_year, entry_month, entry_day).strftime("%d/%m/%Y")
    clear_screen()

    while True:  # collects task name
        get_task = input("Add Task Name: ")
        if get_task == "":
            print("Please, Add Task Name!")
        else:
            break
    clear_screen()

    while True:  # collects time in minutes
        try:
            get_time = int(input("Add Time Spent (in Minutes): "))
            break
        except ValueError:
            print("Please, Enter a Whole Number in Minutes!")
    clear_screen()

    # collects notes (optional)
    notes = input("Add Notes (Optional, Skip with <ENTER>): ")
    clear_screen()

    input("Task Added to Log, Nice! Press <ENTER> to Return to Main Menu ")

    with open('entries.csv', 'a', newline='') as csvfile:  # writes to file
        writer = csv.writer(csvfile)
        writer.writerow([get_date, get_task, get_time, notes])

    return get_date, get_task, get_time, notes
