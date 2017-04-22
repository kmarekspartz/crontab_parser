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
        '1': 'the first'
    }

    def describe_time(self, field, unit) -> str:
        return f"{self.time_descriptions[field]} {unit}"

    def describe_minute(self) -> str:
        return self.describe_time(self.minute, 'minute')

    def describe_hour(self) -> str:
        return self.describe_time(self.hour, 'hour')

    def describe(self) -> str:
        return ''.join([
            "Run `",
            self.describe_command(),
            "` on ",
            self.describe_minute(),
            " of ",
            self.describe_hour(),
            " of every day of every month on any day of the week"
        ])
