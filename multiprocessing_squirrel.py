#!/usr/bin/env python

from __future__ import print_function

import time
import socket
import multiprocessing

from websites import WEBSITE_LIST
from utils import check_website


NUM_WORKERS = 4


def main():
    start_time = time.time()

    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        results = pool.map_async(check_website, WEBSITE_LIST)
        results.wait()

    end_time = time.time()

    print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - start_time))


if __name__ == '__main__':
    main()
