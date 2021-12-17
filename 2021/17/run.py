import os, sys

#target area: x=20..30, y=-10..-5
#target area: x=85..145, y=-163..-108

def isInTargetArea(x,y):
    target_min_x = 85
    target_max_x = 145
    target_min_y = -163
    target_max_y = -108

    if x >= target_min_x and x <= target_max_x and y >= target_min_y and y <= target_max_y:
        return True
    return False

def step(x, y, vel_x, vel_y):
    new_x = x + vel_x
    new_y = y + vel_y
    new_vel_x = vel_x
    if vel_x > 0:
        new_vel_x -= 1
    elif vel_x < 0:
        new_vel_x += 1
    new_vel_y = vel_y - 1

    return new_x, new_y, new_vel_x, new_vel_y

count = 0
worked = []
# 1176 too low
for x_step in range(146):
    for y_step in range(-163, 1000, 1):
        x = 0
        y = 0
        vel_x = x_step
        vel_y = y_step

        max_y = 0

        for step_count in range(100000):
            x, y, vel_x, vel_y = step(x, y, vel_x, vel_y)
            if x > 145 or y < -163:
                break

            if y > max_y:
                max_y = y

            if isInTargetArea(x, y):
                count += 1
                worked.append((x_step, y_step))
#                print('Works {} {} {} {}'.format(max_y, x_step, y_step, step_count))
                break

print(count)
print(worked)
# 5588 too low
