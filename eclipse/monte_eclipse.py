#!/bin/bash
import argparse
import os
import sys

import numpy

from itertools import count, izip, repeat, product

class Ship(object):
    def __init__(self, name, hull=1, count=1, accuracy=0, shields=0, guns=[(1,1)], speed=4):
        self.name = name
        self.hull = hull
        self.count = count
        self.shields = shields
        self.speed = speed
        self.guns = guns

class Interceptor(Ship):
    def __init__(self, count, **kwargs):
        return Ship.__init__("Interceptor", hull=1, count=count, accuracy=0, shields=0, guns=[(1,1)], speed=3)

class Cruiser(Ship):
    def __init__(self, count, **kwargs):
        return Ship.__init__("Interceptor", hull=2, count=count, accuracy=1, shields=0, guns=[(1,1)], speed=2)

class Dreadnought(Ship):
    def __init__(self, count, **kwargs):
        return Ship.__init__("Dreadnought", hull=2, count=count, accuracy=1, shields=0, guns=[(2,1)], speed=1)

def find

def simulate(defender, attacker, attacking_ship):
    if attacker

def main(args):
    parser = argparse.ArgumentParser()
    options = parser.parse_args(args)
    simulate([Interceptor(1), Cruiser(1)], [Dreadnought(2)])

if __name__ == "__main__":
    main(sys.argv[1:])
