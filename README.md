# crontab_parser

A crontab parser inspired by [https://crontab.guru](crontab.guru).

![Status at Travis CI](https://travis-ci.org/zeckalpha/crontab_parser.svg?branch=master)


## Building

    docker build . -t crontab-parser


## Usage

    echo '1 2 3 4 5 command to run' | docker run -i crontab-parser

## TODO

At present this does not do validation or boundary checking, nor does it support
syntax such as:

- 5,10,15
- 5-10
- \*/5
- JAN-DEC / MON-SUN
- @yearly / @annually / @monthly / @weekly / @daily / @hourly / @reboot
- H
- a second field
- L
- W
- ?
- 5#3
- %
- Comments
- Escaping backticks in commands
