#!/usr/bin/python3
"""
Control servos to track celestial objects.

This is the command line interface.
"""
from argparse import ArgumentParser, Namespace
import sys
from typing import Tuple

from .track_object import begin_track

def parse_args() -> Namespace:
    parser = ArgumentParser(prog='star_track')
    mutually_exclusive_args = parser.add_mutually_exclusive_group(required=True)
    mutually_exclusive_args.add_argument(
        '-n', '--name',
        dest='name',
        metavar='NAME',
        type=str,
        help='Name of the celestial object to track (e.g., "Mars", "Polaris")',
    )
    mutually_exclusive_args.add_argument(
        '-c', '--coords',
        dest='coords',
        metavar=('LAT', 'LON'),
        nargs=2,
        type=float,
        help='Pair of coordinates (latitude longitude) to track',
    )
    args = parser.parse_args()
    
    return args

def get_coordinates(name: str) -> Tuple[float, float]:
    return (0.0, 0.0)

def main():
    args = parse_args()
    if args.name:
        # convert name to a pair of coordinates
        right_ascension, declination = get_coordinates(args.name)
    else:
        right_ascension, declination = args.coords
    return begin_track(right_ascension, declination)

if __name__ == '__main__':
    sys.exit(main())
