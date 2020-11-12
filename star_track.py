#!/usr/bin/python3
"""
Control servos to track celestial objects.
"""
from argparse import ArgumentParser
import sys
import time

from .track_object import begin_track

# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(7,GPIO.OUT)
# GPIO.setup(11,GPIO.OUT)

# GPIO.cleanup()

def parse_args() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        type=str,
    )
    return parser.parse_args()

def main():
    args = parse_args()
    begin_track(args.obj)

    return 0

if __name__ == '__main__':
    sys.exit(main())

