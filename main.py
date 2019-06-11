from Projectile import Projectile
from time import sleep

startingVelocity = float(input("What is the initial velocity of the projective? "))
angle = float(input("What angle was the projectile launched at? "))
starting_height = float(input("What was the starting height of the object? "))

myProjectile = Projectile(startingVelocity, angle, starting_height, 1)

y_displacement = starting_height
seconds = 0
while myProjectile.secondly_motion(seconds)["y"] >= 0:
    myProjectile.secondly_motion(seconds)
    print("At t =", str(round(seconds, 2)), "seconds, x =", str(round(myProjectile.secondly_motion(seconds)["x"], 2)),"and y =", str(round(myProjectile.secondly_motion(seconds)["y"], 2)))
    seconds += 1
    sleep(1)
print("The ball hit the ground again at x =", round(myProjectile.find_delta_x(myProjectile.find_zero()), 2), "after", myProjectile.find_zero(), "seconds.")
