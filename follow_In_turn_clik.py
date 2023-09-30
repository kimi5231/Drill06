from pico2d import*

WIDTH, HEIGHT = 1100, 600
open_canvas(WIDTH, HEIGHT)

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')
arrow = load_image('hand_arrow.png')

class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def handle_events():
    global running
    global arrowX, arrowY
    global arrowPos
    global move
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
                arrowPos.append(Arrow(event.x, HEIGHT - 1 - event.y))

def follow_hand_arrow():
    global boyX, boyY
    global j
    global move
    t = j/100
    boyX = (1 - t) * boyX + t * arrowPos[0].x
    boyY = (1 - t) * boyY + t * arrowPos[0].y
    if boyX == arrowPos[0].x and boyY == arrowPos[0].y:
        arrowPos.pop(0)
        move = False
        j = 0

running = True
move = False
frameX, frameY = 0, 3
boyX, boyY = WIDTH//2, HEIGHT//2
arrowX, arrowY = 0, 0
j = 0

arrowPos = []

hide_cursor()
while(running):
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    arrow.draw(arrowX, arrowY)
    character.clip_draw(frameX * 100, frameY * 100, 100, 100, boyX, boyY)
    for i in range(len(arrowPos)):
        arrow.draw(arrowPos[i].x, arrowPos[i].y)
        move = True
    if(move):
        follow_hand_arrow()
        j += 0.1
    update_canvas()
    handle_events()

close_canvas()