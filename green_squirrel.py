#!/usr/bin/env python

from __future__ import print_function

import time

from gevent.pool import Pool
from gevent import monkey

from websites import WEBSITE_LIST
from utils import check_website


NUM_WORKERS = 4


monkey.patch_socket()


def main():
    start_time = time.time()

    pool = Pool(NUM_WORKERS)
    for address in WEBSITE_LIST:
        pool.spawn(check_website, address)

    pool.join()

    end_time = time.time()

    print("Time for GreenSquirrel: %ssecs" % (end_time - start_time))


if __name__ == '__main__':
    main()
