import math
import time


def projectilemotion(power, angle, howlong):
    power = power
    aimangle = math.radians(angle)

    y_vel = -(power*math.sin(aimangle))
    x_vel = power*math.cos(aimangle)
    y_pos = 480
    x_pos = 0
    y_accel = 2
    x_accel = 0
    print(y_vel)

    return y_pos, x_pos, y_vel, x_vel
