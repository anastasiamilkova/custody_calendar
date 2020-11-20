import datetime
from defines import *


class CalendarEngine:
    def __init__(self, start_date, end_date, parent, calendar={}):
        self.start_date = start_date
        self.end_date = end_date
        self.parent = parent
        self.calendar = calendar

    def change_date(self, start_date, end_date=None):
        self.start_date = start_date
        if end_date:
            self.end_date = end_date

    def fill_calendar(self, weekdays):
        current_date = self.start_date
        while self.end_date.month != current_date.month or \
                self.end_date.day != current_date.day or \
                self.end_date.year != current_date.year:
            self.calendar[current_date] = weekdays[current_date.weekday()]
            current_date += datetime.timedelta(days=1)

    def check_day(self, date):
        if date in self.calendar:
            if self.calendar[date] == self.parent:
                return self.calendar[date]
            else:
                return self.calendar[date]
        else:
            return KEY_ERROR

    def get_parent_calendar(self, choice_parent=None):
        if choice_parent:
            parent = choice_parent
        else:
            parent = self.parent
        res_calendar = {}
        for key in self.calendar:
            if self.calendar[key] == parent:
                res_calendar[key] = parent

        return res_calendar

    def get_parent_percent(self):
        parents = {"Mom": 0, "Dad": 0}
        for key in self.calendar:
            if self.calendar[key] == "Mom":
                parents["Mom"] += 1
            elif self.calendar[key] == "Dad":
                parents["Dad"] += 1
        return {
            "Mom": round((parents["Mom"] / (parents["Mom"] + parents["Dad"])) * 100),
            "Dad": round((parents["Dad"] / (parents["Mom"] + parents["Dad"])) * 100)
        }
