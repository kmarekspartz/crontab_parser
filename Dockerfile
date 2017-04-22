FROM python:3.6
WORKDIR /crontab_parser
ADD *.md ./
ADD build-requirements.txt .
RUN pip install -r build-requirements.txt
# ADD requirements.txt .
# RUN pip install -r requirements.txt
ADD crontab_parser crontab_parser
RUN flake8 .
RUN mypy .
ADD tests tests
RUN flake8 tests
RUN mypy tests
RUN python -m unittest
