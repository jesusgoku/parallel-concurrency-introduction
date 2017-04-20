#!/usr/bin/env python

from __future__ import print_function, generators

import os
import time
import threading
import multiprocessing


NUM_WORKERS = 4


def get_process_thread_info():
    return "PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name
    )


def only_sleep():
    """ Do nothing, wait for a timer to expire. """
    print(get_process_thread_info())
    time.sleep(1)


def crunch_numbers():
    """ Do some computations. """
    print(get_process_thread_info())
    x = 0
    while x < 10000000:
        x += 1


def timeit(message="Time it"):
    def decorator(method):
        def timed(*args, **kwargs):
            start_time = time.time()
            method(*args, **kwargs)
            end_time = time.time()

            print(message, "=", end_time - start_time)
        return timed
    return decorator


@timeit("Serial time")
def run_task_in_serial(task, workers):
    """ Run tasks serially. """
    for _ in xrange(workers):
        task()


@timeit("Threads time")
def run_task_in_threads(task, workers):
    """ Run tasks using threads. """
    threads = [threading.Thread(target=task) for _ in xrange(workers)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


@timeit("Parallel time")
def run_task_in_processes(task, workers):
    """ Run tasks using processes. """
    processes = [multiprocessing.Process(target=task) for _ in xrange(workers)]
    [process.start() for process in processes]
    [process.join() for process in processes]


def main():
    run_task_in_serial(only_sleep, NUM_WORKERS)
    run_task_in_threads(only_sleep, NUM_WORKERS)
    run_task_in_processes(only_sleep, NUM_WORKERS)

    run_task_in_serial(crunch_numbers, NUM_WORKERS)
    run_task_in_threads(crunch_numbers, NUM_WORKERS)
    run_task_in_processes(crunch_numbers, NUM_WORKERS)


if __name__ == '__main__':
    main()
