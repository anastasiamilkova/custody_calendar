from CalendarEngine import *
from IO import *

'''
The co-parenting program allows to get information about the custody.
1. Get full calendar for 1 year.
2. Get full calendar for 1 month.
3. Get full calendar in some range.
4. Get one parent's days for 1 year.
5. Get one parent's for 1 month
6. Get one parent's days in some range.
7. Check one date.
8. Get Mom and Dad ratio.

'''

def main():

    parent = IO.input_parent()

    weekdays = IO.input_days(parent)

    start_date = datetime.date.today()
    calendar = CalendarEngine(start_date, start_date +
                              datetime.timedelta(730), parent)
    calendar.fill_calendar(weekdays)

    while True:
        print("1. Get full calendar for 1 year.")
        print("2. Get full calendar for 1 month.")
        print("3. Get full calendar in some range.")
        print("4. Get your days for 1 year.")
        print("5. Get your days for 1 month.")
        print("6. Get your days in some range.")
        print("7. Check one date.")
        print("8. Get Mom and Dad ratio.")
        print("9. Change days.")
        print("0. Quit.")
        choice = input("Choose the option(input a number): ")

        if choice == '0':
            break

        elif choice == '1':
            IO.print_calendar_in_range(
                calendar.calendar, start_date, start_date + datetime.timedelta(days=365))

        elif choice == '2':
            IO.print_calendar_in_range(
                calendar.calendar, start_date, start_date + datetime.timedelta(days=31))

        elif choice == '3':
            print("Input start date.")
            start_date = IO.input_date()
            print("Input end date.")
            end_date = IO.input_date()
            if IO.print_calendar_in_range(calendar.calendar, start_date, end_date) == DATE_ERROR:
                IO.print_pretty_text("Incorrect date range.")

        elif choice == '4':
            parent_days = calendar.get_parent_calendar()
            IO.print_calendar_in_range(
                parent_days, start_date, start_date + datetime.timedelta(days=365))

        elif choice == '5':
            parent_days = calendar.get_parent_calendar()
            IO.print_calendar_in_range(
                parent_days, start_date, start_date + datetime.timedelta(days=31))

        elif choice == '6':
            print("Input start date.")
            start_date = IO.input_date()
            print("Input end date.")
            end_date = IO.input_date()
            parent_days = calendar.get_parent_calendar()
            if IO.print_calendar_in_range(parent_days, start_date, end_date) == DATE_ERROR:
                IO.print_pretty_text("Incorrect date range.")

        elif choice == '7':
            print('Input date you want to check.')
            date = IO.input_date()
            res = calendar.check_day(date)
            if res == KEY_ERROR:
                print("Date is not in calendar. Something went wrong.")
            else:
                IO.print_pretty_text(f"It's {res}'s day.")

        elif choice == '8':
            IO.print_pretty_text(
                f"Mom's ratio is {calendar.get_parent_percent()['Mom']}%\n"
                f"Dad's ratio is {calendar.get_parent_percent()['Dad']}%")

        elif choice == '9':
            print('\n')
            weekdays = IO.input_days(parent)
            print()
            calendar.fill_calendar(weekdays)
            print('Changed successfully.\n')

        else:
            IO.print_pretty_text("Incorrect Input.")
            continue

if __name__ == '__main__':
    main()
