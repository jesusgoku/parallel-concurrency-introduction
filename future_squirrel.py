#!/usr/bin/env python

from __future__ import print_function

import time
import concurrent.futures

from websites import WEBSITE_LIST
from utils import check_website


NUM_WORKERS = 4


def main():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = {executor.submit(check_website, address) for address in WEBSITE_LIST}
        concurrent.futures.wait(futures)

    end_time = time.time()

    print("Time for FutureSquirrel: %ssecs" % (end_time - start_time))


if __name__ == '__main__':
    main()
