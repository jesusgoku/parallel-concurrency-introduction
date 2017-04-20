#!/usr/bin/env python

from __future__ import print_function

import time

from websites import WEBSITE_LIST
from utils import check_website


def main():
    start_time = time.time()

    for address in WEBSITE_LIST:
        check_website(address)

    end_time = time.time()

    print("Time for SerialSquirrel: %ssecs" % (end_time - start_time))


if __name__ == '__main__':
    main()
