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
        self.assertDescription(
            "Run `command to run` on every minute of every hour of"
            " every day of every month on any day of the week",
            "*  *   *  *  * command to run"
        )

    def test_describe_interpolates_and_normalizes_command(self) -> None:
        self.assertDescription(
            "Run `other command to run` on every minute of every"
            " hour of every day of every month on any day of the week",
            "*  *   *  *  * other     command   to     run"
        )

    def test_describe_firsts(self) -> None:
        self.assertDescription(
            "Run `command to run` on the first minute of the first"
            " hour of the first day of January on Mondays",
            "1  1   1  1  1 command to run"
        )

    def assertDescription(self, description: str, line: str) -> None:
        cl = CronLine(line)
        self.assertEqual(description, cl.describe())


if __name__ == '__main__':
    unittest.main()
