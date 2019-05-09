import math
from time import sleep

g = -9.8


def main(initial_v, theta, height, time_interval):
    initial_y = math.sin(math.radians(theta)) * initial_v
    initial_x = math.cos(math.radians(theta)) * initial_v
    seconds = 0
    y_displacement = height
    while y_displacement >= 0:
        y_displacement = find_delta_y(initial_y, seconds, height)
        x_displacement = find_delta_x(initial_x, seconds)
        print("At t = " + str(seconds) + " seconds, the x value is " + str(x_displacement) + ", and the y value is " + str(y_displacement) + ".")
        seconds += time_interval
        sleep(time_interval)
    zero = (-initial_y - math.sqrt(math.pow(initial_y, 2) - (4 * (g / 2) * height)))/g
    print("The projectile hit the ground again at " + str(zero) + "seconds " + str(find_delta_x(initial_x, zero)) + "meters away from launch.")


def find_delta_y(initial_y, sec, initial_height):
    return initial_y * sec + (g / 2) * math.pow(sec, 2) + initial_height


def find_delta_x(initial_x, sec):
    return initial_x * sec


startingVelocity = float(input("What is the initial velocity of the projective?"))
angle = float(input("What angle was the projectile launched at?"))
starting_height = float(input("What was the starting height of the object"))

main(startingVelocity, angle, starting_height, 1)

