from pico2d import *
import random
import math
TUK_WIDTH, TUK_HEIGHT = 1200, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
diagonal_up = load_image('left_up.png')
diagonal_down = load_image('left_down.png')
mouse = load_image('hand_arrow.png')
def handle_events():
    global running, mx, my, click
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my =  event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click.append((event.x, TUK_HEIGHT - 1 - event.y))
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx, my = TUK_WIDTH // 2, TUK_HEIGHT // 2
dx, dy = 0, 0
frame = 0
hide_cursor()
distance = 0
click = []
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse.draw(mx, my)
    if len(click) > 0:
        # 캐릭터의 방향 설정
        click_x, click_y = click[0]
        dx = click_x - x
        dy = click_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:
            dx /= distance
            dy /= distance
        if dx < 0 and dy > 0:  # 좌상
            diagonal_up.clip_draw(frame * 27, 0, 27, 32, x, y, 60, 90)
        elif dx < 0 and dy < 0:  # 좌하
            diagonal_down.clip_draw(frame * 28, 0, 28, 32, x, y, 60, 90)
        elif dx > 0 and dy > 0:  # 우상
            diagonal_up.clip_composite_draw(frame * 27, 0, 27, 32, 0, 'h', x, y, 60, 90)
        elif dx > 0 and dy < 0:  # 우하
            diagonal_down.clip_composite_draw(frame * 28, 0, 28, 32, 0, 'h', x, y, 60, 90)
        for click_x, click_y in click:
            mouse.draw(click_x, click_y)
        if distance <= 1:
            click.pop(0)


    update_canvas()
    frame = (frame + 1) % 3
    x += dx
    y += dy

    if distance <= 1:
        pass
   
    handle_events()
close_canvas()




