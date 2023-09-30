from pico2d import*

WIDTH, HEIGHT = 1100, 600
open_canvas(WIDTH, HEIGHT)

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global arrowX, arrowY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            arrowX = event.x
            arrowY = HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                pass

running = True
frameX, frameY = 0, 3
boyX, boyY = WIDTH//2, HEIGHT//2
arrowX, arrowY = 0, 0

hide_cursor()
while(running):
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    arrow.draw(arrowX, arrowY)
    character.clip_draw(frameX * 100, frameY * 100, 100, 100, boyX, boyY)
    update_canvas()
    handle_events()

close_canvas()