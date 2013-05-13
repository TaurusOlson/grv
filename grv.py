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
import argparse

def uniform(domain=None):
    """Generate a random value in the given domain using a uniform distribution

    Usage
    -----

    r = uniform(domain)
    r.next()

    Parameters
    ----------
    domain : list
        The domain on which the values are taken

    Returns
    -------
    A generator returning a random value within the chosen domain

    """
    if domain:
        start = domain[0]
        stop = domain[1]
    else:
        start = 0
        stop = 1

    while True:
        yield random.random() * (stop - start) + start


def normal(parameters=None):
    """Generate a random value in the given domain using a normal distribution

    Usage
    -----

    r = normal(parameters)
    r.next()

    Parameters
    ----------
    domain : list
        The domain on which the values are taken

    Returns
    -------
    A generator returning a random value between start and stop

    """
    if parameters:
        mu = parameters[0]
        sigma = parameters[1]
    else:
        mu = 0
        sigma = 1

    while True:
        yield random.gauss(mu, sigma)


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


# The argument parser
parser = argparse.ArgumentParser(description="Generate random values")
parser.add_argument("parameters", type=float, nargs="*", help="a distribution")
parser.add_argument("--uniform", dest="accumulate", action="store_const",
                    const=uniform, default=uniform)
parser.add_argument("--normal", dest="accumulate", action="store_const",
                    const=normal, default=normal)

args = parser.parse_args()


if __name__ == '__main__':
    n = 1
    r = args.accumulate(args.parameters)
    if len(args.parameters) == 3:
        n = int(args.parameters[2])

    for i in range(n):
        print r.next()
