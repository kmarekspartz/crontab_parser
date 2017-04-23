# crontab_parser

A crontab parser inspired by [https://crontab.guru](crontab.guru).

![https://travis-ci.org/zeckalpha/crontab_parser.svg?branch=master](Status at Travis CI)


## Building

    docker build . -t crontab-parser


## Usage

    echo '1 2 3 4 5 command to run' | docker run -i crontab-parser
