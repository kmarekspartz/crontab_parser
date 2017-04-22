import unittest

from crontab_parser.cron_line import CronLine


class TestCronLine(unittest.TestCase):
    def test_splits_into_fields(self) -> None:
        line = "*  *   *  *  * command to run"
        split_line = line.split()
        minute, hour, day_of_month, month, day_of_week, *command = split_line
        cl = CronLine(line)
        self.assertEqual(minute, cl.minute)
        self.assertEqual(hour, cl.hour)
        self.assertEqual(day_of_month, cl.day_of_month)
        self.assertEqual(month, cl.month)
        self.assertEqual(day_of_week, cl.day_of_week)
        self.assertEqual(command, cl.command)

    def test_describe_every(self) -> None:
        line = "*  *   *  *  * command to run"
        description = "Run `command to run` on every minute of every hour of" \
            " every day of every month on any day of the week"
        cl = CronLine(line)
        self.assertEqual(description, cl.describe())

    def test_describe_interpolates_and_normalizes_command(self) -> None:
        line = "*  *   *  *  * other     command   to     run"
        description = "Run `other command to run` on every minute of every" \
            " hour of every day of every month on any day of the week"
        cl = CronLine(line)
        self.assertEqual(description, cl.describe())

    def test_describe_first_minute(self) -> None:
        line = "1  *   *  *  * command to run"
        description = "Run `command to run` on the first minute of every" \
            " hour of every day of every month on any day of the week"
        cl = CronLine(line)
        self.assertEqual(description, cl.describe())

    def test_describe_first_minute_of_the_first_hour(self) -> None:
        line = "1  1   *  *  * command to run"
        description = "Run `command to run` on the first minute of the first" \
            " hour of every day of every month on any day of the week"
        cl = CronLine(line)
        self.assertEqual(description, cl.describe())


if __name__ == '__main__':
    unittest.main()
