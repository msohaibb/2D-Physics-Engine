import math
from time import sleep

g = -9.8
time = 0


def main(initial_v, theta, height):
    initial_y = math.sin(math.radians(theta)) * initial_v
    initial_x = math.cos(math.radians(theta)) * initial_v
    seconds = 0
    while height > 0:
        height = find_delta_y(initial_y, seconds, height)
        x_displacement = find_delta_x(initial_x, seconds)
        print("At t = " + str(seconds) + " seconds, the x value is " + str(x_displacement) + ", and the y value is " + str(height) + ".")
        seconds += 1
        sleep(1)


def find_delta_y(initial_y, sec, height):
    return initial_y * sec + (g / 2) * math.pow(sec, 2) + height


def find_delta_x(initial_x, sec):
    return initial_x * sec


startingVelocity = float(input("What is the initial velocity of the projective?"))
angle = float(input("What angle was the projectile launched at?"))
height = float(input("What was the starting height of the object"))

main(startingVelocity, angle, height)

