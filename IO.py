from defines import *
import datetime


class IO:
    @staticmethod
    def not_parent(parent):
        if parent == "Mom":
            return "Dad"
        else:
            return "Mom"

    @staticmethod
    def check_days(days):
        for day in days:
            if day.lower() not in WEEKDAYS:
                return False
        return True

    @staticmethod
    def input_parent():
        parent = input("Are you Mom or Dad?: ")
        while True:
            if parent.lower() != "mom" and parent.lower() != "dad":
                parent = input("Incorrect input. Input Mom or Dad: ")
            else:
                return parent.capitalize()

    @staticmethod
    def input_days(parent):
        days = input(
            "Which days are yours(ex:Friday Monday Tuesday): ").split()

        while not IO.check_days(days):
            days = input(
                "Incorrect Input. Which days are yours (eg.:Friday Monday Tuesday): ").split()

        weekdays = [None] * 7
        for day in days:
            weekdays[WEEKDAYS.index(day.lower())] = parent

        for i in range(len(weekdays)):
            if weekdays[i] == None:
                weekdays[i] = IO.not_parent(parent)

        return weekdays

    @staticmethod
    def input_date():
        while True:
            try:
                date_entry = input('Enter a date in MM-DD-YYYY format: ')
                month, day, year = map(int, date_entry.split('-'))
                return datetime.date(year, month, day)
            except:
                print("Incorrect input.")
                continue

    @staticmethod
    def print_calendar(calendar):
        print('\n')
        for key in calendar:
            print(f"{key}: {calendar[key]}")
        print('\n')

    @staticmethod
    def print_pretty_text(text):
        print('\n')
        print(text)
        print('\n')

    @staticmethod
    def print_calendar_in_range(calendar, start_date, end_date):
        if (end_date - start_date).days <= 0:
            return DATE_ERROR
        else:
            print('\n')
            for key in calendar:
                if key < start_date:
                    continue
                elif key > end_date:
                    break
                else:
                    print(f"{key}: {calendar[key]}")
            print('\n')

    @staticmethod
    def get_start_end():
        start_date_list = list(
            map(int, input('Enter month, day and year: ').split()))
        end_date_list = list(
            map(int, input('Enter month, day and year: ').split()))
        start_date = {
            'month': start_date_list[0], 'day': start_date_list[1], 'year': start_date_list[2]}
        end_date = {
            'month': end_date_list[0], 'day': end_date_list[1], 'year': end_date_list[2]}
        return {'start': start_date, 'end': end_date}
