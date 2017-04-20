#!/usr/bin/env python

from __future__ import print_function

import time
from queue import Queue
from threading import Thread

from websites import WEBSITE_LIST
from utils import check_website


NUM_WORKERS = 4
task_queue = Queue()


def worker():
    """ Constantly check the queue for addresses. """
    while True:
        address = task_queue.get()
        check_website(address)

        task_queue.task_done()


def main():
    start_time = time.time()

    threads = [Thread(target=worker) for _ in xrange(NUM_WORKERS)]
    [task_queue.put(item) for item in WEBSITE_LIST]
    [thread.start() for thread in threads]
    task_queue.join()

    end_time = time.time()

    print("Time for ThreadedSquirrel: %ssecs" % (end_time - start_time))


if __name__ == '__main__':
    main()
