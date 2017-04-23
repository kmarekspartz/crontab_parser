import calendar
import time


class CronLine(object):
    def __init__(self, line: str) -> None:
        split_line = line.split()
        minute, hour, day_of_month, month, day_of_week, *command = split_line
        self.minute = minute
        self.hour = hour
        self.day_of_month = day_of_month
        self.month = month
        self.day_of_week = day_of_week
        self.command = command

    def describe_command(self) -> str:
        return ' '.join(self.command)

    def describe_minute(self) -> str:
        if self.minute == '*':
            return 'every minute'
        return 'minute ' + self.minute

    def describe_hour(self) -> str:
        if self.hour == '*':
            return 'every hour'
        return 'hour ' + self.hour

    def describe_month(self) -> str:
        try:
            month_int = int(self.month)
            return calendar.month_name[month_int]
        except ValueError:
            return 'every month'

    def describe_day_of_week(self) -> str:
        try:
            day_of_week_int = int(self.day_of_week) % 7
            return calendar.day_name[day_of_week_int - 1]
        except ValueError:
            return 'any day of the week'

    def is_every_day(self) -> bool:
        return all([
            self.day_of_month == '*',
            self.month == '*',
            self.day_of_week == '*'
        ])

    def describe_date(self) -> str:
        if self.day_of_month == '*' and self.month == '*':
            return ''
        if self.day_of_month == '*':
            return 'in ' + self.describe_month()
        if self.month == '*':
            return ''.join([
                'day ',
                self.day_of_month,
                ' of every month'
            ])
        return ''.join([
            self.describe_month(),
            ' ',
            self.day_of_month
        ])

    def describe_days_and_months(self) -> str:
        if self.is_every_day():
            return ''
        if self.day_of_month == '*' and self.month == '*':
            return ' on ' + self.describe_day_of_week()
        if self.day_of_week == '*' and self.day_of_month == '*':
            return ' ' + self.describe_date()
        if self.day_of_week == '*':
            return ' on ' + self.describe_date()
        if self.day_of_month == '*':
            return ''.join([
                ' on every ',
                self.describe_day_of_week(),
                ' in ',
                self.describe_month()
            ])
        if self.day_of_week == '*':
            return ' on ' + self.describe_date()
        return ''.join([
            ' on ',
            self.describe_day_of_week(),
            ', ',
            self.describe_date()
        ])

    def describe_time(self) -> str:
        if self.minute == '*' and self.hour == '*':
            return 'at ' + self.describe_minute()
        if self.minute == '*' or self.hour == '*':
            return ''.join([
               'at ',
               self.describe_minute(),
               ' of ',
               self.describe_hour()
            ])
        return 'at ' + time.strftime(
            '%H:%M',
            (0, 1, 2, int(self.hour), int(self.minute), 5, 6, 7, 8)
        )

    def describe(self) -> str:
        return ''.join([
            'Run `',
            self.describe_command(),
            '` ',
            self.describe_time(),
            self.describe_days_and_months()
        ])
