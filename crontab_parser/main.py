from sys import stdin, stdout

from crontab_parser.cron_line import CronLine


def main(input_io=stdin, output_io=stdout) -> None:
    for line in input_io.readlines():
        output_io.write(CronLine(line).describe() + '\n')


if __name__ == '__main__':
    main()
