import unittest

from crontab_parser.cron_line import CronLine


class TestCronLine(unittest.TestCase):
    def test_can_be_constructed(self) -> None:
        CronLine("")


if __name__ == '__main__':
    unittest.main()
