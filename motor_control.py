"""
Move things.
"""
import RPi.GPIO as gpio

XY_MOTOR_PIN = 7
POLAR_MOTOR_PIN = 11

gpio.setmode(gpio.BOARD)
# gpio.setup([XY_MOTOR, POLAR_MOTOR] , gpio.OUT)

# class GPIOOutputPin:
#     """
#     Class for managing contexts
#     """
#     def __init__(self, pin: int) -> None:
#         self.pin = pin
#         return
#     def __enter__(self):
#         gpio.setup(self.pin, gpio.OUT)
#         return self
#     def __exit__(self, exc_type, exc_value, traceback) -> None:
#         gpio.cleanup(self.pin)
#         return

# class Motor(GPIOOutputPin):
class Motor:
    def __init__(self, pin: int) -> None:
        # super().__init__(pin)
        self.pin = pin
        self.position = None
        self.bounds = None
        gpio.setup(self.pin, gpio.OUT)
        
        return
        
    # class ExceptionWithCleanup(KeyboardInterrupt):
    #     def __init__(self, message: str):
    #         super().__init__(message)
    #         gpio.cleanup()

    def step(self, increment: bool | int):
        gpio.output(self.pin, gpio.HIGH if increment else gpio.LOW)
    
    def __del__(self) -> None:
        gpio.cleanup()
        return
    
class XYMotor(Motor):
    def __init__(self, pin: int):
        super().__init__(pin)
        return

class PolarMotor(Motor):
    def __init__(self, pin: int):
        super().__init__(pin)
        self.bounds = (0.0, 90.0)
        return
