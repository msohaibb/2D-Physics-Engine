import math
from time import sleep

g = -9.8


class Projectile:
    def __init__(self, initial_v, theta, height, time_interval):
        self.initial_v = initial_v
        self.initial_y = initial_v * math.sin(math.radians(theta))
        self.initial_x = initial_v * math.cos(math.radians(theta))
        self.theta = theta
        self.height = height
        self.time_interval = time_interval
        self.seconds = 0
        self.position = {}

    def find_delta_y(self, sec):
        return self.initial_y * sec + (g / 2) * math.pow(sec, 2) + self.height

    def find_delta_x(self, sec):
        return self.initial_x * sec

    def find_zero(self):
        return round((-self.initial_y - math.sqrt(math.pow(self.initial_y, 2) - (4 * (g / 2) * self.height))) / g, 2)

    def motion(self):
        seconds = 0
        y_displacement = self.height
        while y_displacement >= 0:
            y_displacement = self.find_delta_y(seconds)
            x_displacement = self.find_delta_x(seconds)
            print("At t = " + str(round(seconds, 2)) + " seconds, the x value is " +
                  str(round(x_displacement, 2)) + ", and the y value is " + str(round(y_displacement, 2)) + ".")
            seconds += self.time_interval
            sleep(self.time_interval)
        zero = self.find_zero()
        print("The projectile hit the ground again at " + str(round(zero, 2)) + " seconds, x = " +
              str(round(self.find_delta_x(zero), 2)))

    def secondly_motion(self, second):
        self.seconds = second
        y_displacement = self.find_delta_y(self.seconds)
        x_displacement = self.find_delta_x(self.seconds)
        self.position = {"x": x_displacement, "y": y_displacement}
        return self.position

