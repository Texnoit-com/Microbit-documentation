'''Движение пикселя'''

import random

from microbit import (Image, accelerometer, button_a, display, running_time,
                      sleep)

MIN_X = -1024
MAX_X = 1024
WALL_MIN_SPEED = 400
PLAYER_MIN_SPEED = 200
WAALL_MAX_SPEED = 100
PLAYER_MAX_SPEED = 50
SPEED_MAX = 12
range_x = MAX_X - MIN_X

while True:

    template = Image('00000:'*5)
    s = template.set_pixel
    player_x = 2
    wall_y = -1
    hole = 0
    score = 0
    handled_this_wall = False
    wall_speed = WALL_MIN_SPEED
    player_speed = PLAYER_MIN_SPEED
    wall_next = 0
    player_next = 0

    while True:
        t = running_time()
        player_update = t >= player_next
        wall_update = t >= wall_next
        if not (player_update or wall_update):
            next_event = min(wall_next, player_next)
            delta = next_event - t
            sleep(delta)
            continue

        if wall_update:
            # расчет новой скорости
            speed = min(score, SPEED_MAX)
            wall_speed = WALL_MIN_SPEED + int((WAALL_MAX_SPEED - WALL_MIN_SPEED) * speed / SPEED_MAX)
            player_speed = PLAYER_MIN_SPEED + int((PLAYER_MAX_SPEED - PLAYER_MIN_SPEED) * speed / SPEED_MAX)

            wall_next = t + wall_speed
            if wall_y < 5:
                # замена препядствия
                use_wall_y = max(wall_y, 0)
                for wall_x in range(5):
                    if wall_x != hole:
                        s(wall_x, use_wall_y, 0)

        wall_reached_player = (wall_y == 4)
        if player_update:
            player_next = t + player_speed
            # найти новую координату x
            x = accelerometer.get_x()
            x = min(max(MIN_X, x), MAX_X)
            # отключить старую позицию (пиксель)
            s(player_x, 4, 0)
            x = ((x - MIN_X) / range_x) * 5
            x = min(max(0, x), 4)
            x = int(x + 0.5)

            if not handled_this_wall:
                if player_x < x:
                    player_x += 1
                elif player_x > x:
                    player_x -= 1
        if wall_update:
            # обновить положение стены
            wall_y += 1
            if wall_y == 7:
                wall_y = -1
                hole = random.randrange(5)
                handled_this_wall = False

            if wall_y < 5:
                # нарисовать новую стену
                use_wall_y = max(wall_y, 0)
                for wall_x in range(5):
                    if wall_x != hole:
                        s(wall_x, use_wall_y, 6)

        if wall_reached_player and not handled_this_wall:
            handled_this_wall = True
            if (player_x != hole):
                # столкновение! игра закончена!
                break
            score += 1

        if player_update:
            # включить новый пиксель
            s(player_x, 4, 9)

        display.show(template)

    display.show(template.SAD)
    sleep(1000)
    display.scroll("Score:" + str(score))

    while True:
        if (button_a.is_pressed() and button_a.is_pressed()):
            break
        sleep(100)
