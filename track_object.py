"""
Calculate things and then control servos.
"""
from astropy.coordinates import AltAz, EarthLocation, get_body, SkyCoord
from astropy.time import Time
import astropy.units as u
import numpy as np
from typing import List, Self, Tuple

from .motor_control import XYMotor, PolarMotor, XY_MOTOR_PIN, POLAR_MOTOR_PIN

LOCATION_FILE = '/home/nick/projects/star_track/location.txt'

class Track:
    def __init__(self, target: str) -> None:
        with open(LOCATION_FILE, 'r') as f:
            print(f"Reading location from {LOCATION_FILE}")
            longitude, latitude = f.readlines()
            self.longitude, self.latitude = (
                float(longitude.strip('\n')),
                float(latitude.strip('\n'))
            )
        
        self.frame = get_body(
            target,
            Time.now(),
            location=EarthLocation(
                lat=self.latitude * u.deg,
                lon=self.longitude * u.deg,
            ),
        )

        self.xy_steps: List[bool]
        self.polar_steps: List[bool]
        self.find_tracking_rate()

        return
    
    def find_tracking_rate(self) -> Self:
        """
        Make an array of coordinates to parse and send to motors.
        """
        # 0 no step, 1 step
        xy_steps = np.array([], dtype=int)
        polar_steps = np.array([], dtype=int)

        # cast to list of ones and zeros
        self.xy_steps = [step for step in xy_steps]
        self.polar_steps = [step for step in polar_steps]
        return self
    
    def begin_track(self, rate: float | None = None) -> Self:
        # attach to motors
        self.motor_xy = XYMotor(XY_MOTOR_PIN)
        self.motor_polar = PolarMotor(POLAR_MOTOR_PIN)
        # use .motor_.bounds to 
        try:
            for xy, polar in zip(self.xy_steps, self.polar_steps):
                self.motor_xy.step(xy)
                self.motor_polar.step(polar)
        except KeyboardInterrupt:
            print("Tracking interrupted by user.")
        finally:
            del self.motor_xy, self.motor_polar
        
        return self

def begin_track_by_name(name: str) -> None:
    track = Track(name)
    track.begin_track()
    return

def get_coordinates(name: str) -> Tuple[float, float]:
    return (0.0, 0.0)
