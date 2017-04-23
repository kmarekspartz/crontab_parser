import unittest
from io import StringIO

from crontab_parser.main import main

test_input = "1  2   3  4  5 command    to    run\n" \
    "1  *   3  4  5 command to run\n" \
    "1  2   *  4  5 command to run\n" \
    "1  2   3  *  5 command to run\n" \
    "1  2   3  4  * command to run\n"

expected_output = "Run `command to run` at 02:01 on Friday, April 3\n" \
    "Run `command to run` at minute 1 of every hour on Friday, April 3\n" \
    "Run `command to run` at 02:01 on every Friday in April\n" \
    "Run `command to run` at 02:01 on Friday, day 3 of every month\n" \
    "Run `command to run` at 02:01 on April 3\n"


class TestMain(unittest.TestCase):
    def test_main(self) -> None:
        output_io = StringIO()
        main(input_io=StringIO(test_input), output_io=output_io)
        self.assertEqual(expected_output, output_io.getvalue())


if __name__ == '__main__':
    unittest.main()
