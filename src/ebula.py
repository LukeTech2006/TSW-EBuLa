import pygame, time, csv, json, easygui, queue, sys, os, win32api

#pygame initialisieren
pygame.init()

#event queue und pygame-font-dings
drawQueue = queue.Queue()
n_font = pygame.font.SysFont('Arial', 24)
b_font = pygame.font.SysFont('Arial', 24, True)
big_font = pygame.font.SysFont('Arial', 28, True)

#helferfunktion zur dateiauswahl und übergabe in dict()
def loadFile() -> ...:
    global altn_name
    avail_tables = {}
    avail_profiles = {}
    for file in os.listdir('./src/timetables/'):                                                        #! FIXME: nicht hard coden!
        if file.endswith('.json'):
            table_json = json.load(open(f'./src/timetables/{file}', mode='r', encoding='UTF-8'))        #! FIXME: nicht hard coden!
            avail_tables[table_json['route']] = table_json['path']
            try: avail_profiles[table_json['route']] = table_json['speed_profiles']
            except KeyError: pass
        else: pass
    choice = easygui.choicebox('Fahrplan auswählen:', 'EBuLa Select', list(avail_tables.keys()))
    if choice == None: sys.exit(0)
    try: altn_name = avail_profiles[choice]
    except KeyError: pass
    pygame.display.set_caption(choice)
    return csv.DictReader(open(f'./src/timetables/{avail_tables[choice]}', mode='r', encoding='UTF-8')) #! FIXME: nicht hard coden!

#helferfunktion zur zeichnungsfunktion
def pushDrawQueue(source: pygame.Surface, dest: pygame.Rect) -> None:
    drawQueue.put([source, dest])
    return

def generateTable(page: int, altn: bool) -> None:
    global rows, drawQueue

    if altn:
        try: x = rows[0]['1b']
        except: altn = False
    speed_key = '1a' if not altn else '1b'

    try:
        for i in range(page * 15, (page * 15) + 15):
            if rows[i][speed_key] != '':
                lineSurf = pygame.Surface((188, 2))
                lineSurf.fill((255, 255, 255))
                drawQueue.put((lineSurf, (0, 124 + ((14 - (i % 15)) * 38))))
                font_obj = n_font.render(rows[i][speed_key], True, (255, 255, 255))
                font_width = font_obj.get_rect().width
                drawQueue.put((font_obj, (175 - font_width, 92 + ((14 - (i % 15)) * 38))))
            if rows[i]['Lage'] != '':
                font_obj = n_font.render(rows[i]['Lage'].replace('<l>',''), True, (255, 255, 255))
                font_width = font_obj.get_rect().width
                drawQueue.put((font_obj, (295 - font_width, 92 + ((14 - (i % 15)) * 38))))
                if rows[i]['Lage'].find('<l>') != -1:
                    lineSurf = pygame.Surface((110, 2))
                    lineSurf.fill((255, 255, 255))
                    drawQueue.put((lineSurf, (193, 124 + ((14 - (i % 15)) * 38))))
            if rows[i]['Betriebsstelle'] != '':
                text = rows[i]['Betriebsstelle']
                match text:
                    case '¥':
                        icon_obj = pygame.image.load('./src/icons/yen.png')                         #! FIXME: nicht hard coden!
                        drawQueue.put((icon_obj, (400, 89 + ((14 - (i % 15)) * 38))))
                    case _:
                        font_obj = n_font.render(text.replace('<V>',''), True, (255, 255, 255)) if text.find('<b>') < 0 else b_font.render(text.replace('<b>',''), True, (255, 255, 255))
                        drawQueue.put((font_obj, (450, 92 + ((14 - (i % 15)) * 38))))
                        if text.find('<V>') != -1:
                            icon_obj = pygame.image.load('./src/icons/brw.png')                         #! FIXME: nicht hard coden!
                            drawQueue.put((icon_obj, (400, 89 + ((14 - (i % 15)) * 38))))
    except IndexError: pass

    if altn:
        font_obj = big_font.render(altn_name['1b'], True, (0,0,0))
        drawQueue.put((font_obj, (15,720)))
        
key_next = ord('T')
key_prev = ord('G')
key_speed = ord('M')

#fahrplandaten laden
table = loadFile()
rows = list()
for row in table: rows.append(row)

#initialisieren mit hintergrund
screen_info = pygame.display.Info()
#screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h),pygame.NOFRAME)
#window = pygame.Surface((1024,768))
window = pygame.display.set_mode((1024,768),pygame.SCALED)
drawQueue.put((pygame.image.load('./src/background.png'), (0, 0)))                                  #! FIXME: nicht hard coden!

#uhr initialisieren
clock = pygame.time.Clock()

prev_pressed = win32api.GetKeyState(key_prev)
next_pressed = win32api.GetKeyState(key_next)
speed_pressed = win32api.GetKeyState(key_speed)

altn_speed = False
current_page = 0

#event-loop zum zeichnen
while True:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    drawQueue.put((pygame.image.load('./src/background.png'), (0, 0)))                          #! FIXME: nicht hard coden!
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