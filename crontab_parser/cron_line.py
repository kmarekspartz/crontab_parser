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
        if self.minute == '1':
            return 'the first minute'
        else:
            return 'gah!'  # FIXME

    def describe(self) -> str:
        return ''.join([
            "Run `",
            self.describe_command(),
            "` on ",
            self.describe_minute(),
            " of every hour of every day of every month on any day of the week"
        ])
