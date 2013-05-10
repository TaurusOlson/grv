#!/usr/bin/env python


"""
grv
~~~

A script for generating random values with the command line.

So far only uniform distribution is supported.

"""

import random
import sys
import os


def generate_random(start=0, stop=1):
    """Generate a random value between start and stop

    r = generate_random(start, stop)

    Parameters
    ----------
    start : int
        The lower bound of the range (optional)

    stop : int
        The upper bound of the range (optional)

    Returns
    -------
    A generator returning a random value between start and stop

    """
    while True:
        yield random.random() * (stop - start) + start


def usage():
    """Display a help message"""
    script = os.path.basename(__file__)
    print """%s -- Generate random numbers

Usage:
    Generate one number between 0 and 1:
    %s

    Generate one number between min and max:
    %s <min> <max>

    Generate n numbers between min and max:
    %s <min> <max> <n>""" % ((script, ) * 4)


n = 1

# Usage: generate_random
if len(sys.argv) == 1:
    r = generate_random()

# Usage: generate_random <start> <stop>
elif 3 <= len(sys.argv) < 5:
    start = float(sys.argv[1])
    stop = float(sys.argv[2])
    r = generate_random(start, stop)

    # Usage: generate_random <start> <stop> <n>
    if len(sys.argv) == 4:
        n = int(sys.argv[3])
else:
    usage()
    sys.exit()


if __name__ == '__main__':
    for i in range(n):
        print r.next()
