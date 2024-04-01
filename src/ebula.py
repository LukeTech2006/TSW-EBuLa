import pygame, time, sys, win32api
from util import *
from globals import *

#pygame initialisieren
pygame.init()

# Initialisieren mit hintergrund
screen_info = pygame.display.Info()
# screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h),pygame.NOFRAME)
# window = pygame.Surface((1024,768))
window = pygame.display.set_mode((1024,768),pygame.SCALED)
drawQueue.put((pygame.image.load(dir_self + 'background.png'), (0, 0)))

# Uhr Init
clock = pygame.time.Clock()

prev_pressed = win32api.GetKeyState(key_prev)
next_pressed = win32api.GetKeyState(key_next)
speed_pressed = win32api.GetKeyState(key_speed)

altn_speed = False
current_page = 0

#event-loop zum zeichnen aka Main loop
while True:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    drawQueue.put((pygame.image.load(dir_self + 'background.png'), (0, 0)))
    drawQueue.put((big_font.render(time.strftime('%d.%m.%Y'), True, (255, 255, 255)), (700,5)))
    drawQueue.put((big_font.render(time.strftime('%H:%M:%S'), True, (255, 255, 255)), (895,5)))
    generateTable(current_page, altn_speed)

    new_prev = max(win32api.GetKeyState(key_prev), 0)
    if new_prev != prev_pressed:
        current_page = max(0, current_page - 1)
        prev_pressed = new_prev
    
    new_next = max(win32api.GetKeyState(key_next), 0)
    if new_next != next_pressed:
        current_page = min(int(len(rows) / 15), current_page + 1)
        next_pressed = new_next
    
    new_speed = max(win32api.GetKeyState(key_speed), 0)
    if new_speed != speed_pressed:
        altn_speed = False if altn_speed else True
        speed_pressed = new_speed

    #jedes element der drawQueue zeichnen
    for _ in range(drawQueue.qsize()):
        try:
            shape = drawQueue.get()
            window.blit(shape[0], shape[1])
        except Exception as e: print(f'Zeichnungsfehler: {e}!')
    
    #screen.blit(window, ((screen_info.current_w - 1024) / 2, ((screen_info.current_h - 768) / 2)))
    pygame.display.flip()