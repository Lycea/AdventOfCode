#!/usr/bin/env python3
import re
import os
import sys
import time
import argparse
import requests

from itertools import chain
from bs4 import BeautifulSoup


def get_day_info(year, day, options):
    """ This will send GET requests to the AoC website.
    If you look at the response of the website,
    you'll see that the creator has put a notice
    as to ask to reduce the amount of automated request.
    Please respect this notice,
    and use this script sparingly."""
    get_question = options["get_question"]
    part = options["part"]
    session_id = options["session_id"]
    cookies = dict()
    
    cookies["session"] = session_id

    print(os.getcwd())

    # Get the input for the day
    question_url = f"https://adventofcode.com/{year}/day/{day}"
    input_url = question_url + "/input"
    
    response = requests.get(input_url, cookies=cookies)
    print(input_url)
    if response.status_code == 200:
        with open(f"{year}/Day_{day:02d}/input.txt", "w") as f:
            f.write(response.text)
    else:
        print(f"Failed to get input for day {day}, year {year}")
        print(f"Status code: {response.status_code}")
        print(f"Reason: {response.reason}")

    # Get the question for the day
    if get_question is True:
        if part == 2:
            response = requests.get(question_url, cookies=cookies)
        else:
            response = requests.get(question_url)
        if response.status_code == 200:
            with open(f"{year}/Day_{day:02d}/question.html", "w") as f:
                soup = BeautifulSoup(response.text, "html.parser")
                m = re.sub("<p>You can also(.|\s)*", "", str(soup.main))
                f.write(m + "</main>")
        else:
            print(f"Failed to get question for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")
    print("Done")
    os.chdir("..")


    

def main(args):
    args = vars(args)
    args["base_url"] = "https://adventofcode.com"
    year = args["year"]
    day =  args["day"]

    __location__ = f"{year}/{day}"
    args["output"] = __location__ 

    os.chdir(__location__)
    get_day_info(year, day, args)

    print("Finished getting info for day")


if __name__ == "__main__":
    cur_year = time.strftime("%Y")
    if time.strftime("%m") != "12":
        cur_year = str(int(cur_year) - 1)

    parser = argparse.ArgumentParser(
        prog="`Advent of Code` Year Grabber",
        description="Download selected `Advent of Code` days for a given year\
             or given years."
    )
    parser.add_argument(
        "year",
        dest="year",
        help="The year to get the day for."
    )
    parser.add_argument(
        "day",
        dest="day",
        help="Days to get. "
    )
    parser.add_argument(
        "-s",
        dest="session_id",
        default=os.getenv("SESSION_ID"),
        help="Your session ID from `adventofcode.com`.  Default is to use the SESSION_ID environment variable.",
    )
    parser.add_argument(
        "-q",
        dest="get_question",
        action="store_true",
        help="Will get the question for the day.",
    )
    parser.add_argument(
        "-p",
        dest="part",
        type=int,
        default=1,
        help="Will attempt to get the question for the day up to the given part. Defaults to 1",
    )
    parser.add_argument(
        "--sample-input",
        dest="sample_input",
        action="store_true",
    )

    args = parser.parse_args()

    main(args)
