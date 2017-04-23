import calendar


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

    time_descriptions = {
        '*': 'every',
        '1': 'the first',
        '45': 'not a good approach',
        '23': 'not at all',
        '0': 'zero points'
    }

    def describe_time(self, field, unit) -> str:
        return f"{self.time_descriptions[field]} {unit}"

    def describe_minute(self) -> str:
        return self.describe_time(self.minute, 'minute')

    def describe_hour(self) -> str:
        return self.describe_time(self.hour, 'hour')

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
        if self.month == '*':
            return ''.join([
                'day ',
                self.day_of_month,
                ' of every month'
            ])
        return ''.join([
            self.describe_month(),
            " ",
            self.day_of_month
        ])

    def describe_days_and_months(self) -> str:
        if self.is_every_day():
            return ''
        if self.day_of_month == '*' and self.month == '*':
            return " of " + self.describe_day_of_week()
        if self.day_of_month == '*':
            return ''.join([
                " of every ",
                self.describe_day_of_week(),
                " in ",
                self.describe_month()
            ])
        if self.day_of_week == '*':
            return " of " + self.describe_date()
        return ''.join([
            " of ",
            self.describe_day_of_week(),
            ", ",
            self.describe_date()
        ])

    def describe(self) -> str:
        return ''.join([
            "Run `",
            self.describe_command(),
            "` on ",
            self.describe_minute(),
            " of ",
            self.describe_hour(),
            self.describe_days_and_months()
        ])
