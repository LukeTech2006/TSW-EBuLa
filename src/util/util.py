import pygame, csv, json, easygui, os, sys
from globals import *

#helferfunktion zur dateiauswahl und übergabe in dict()
def loadFile() -> dict:
    global altn_name
    avail_tables = {}
    avail_profiles = {}
    for file in os.listdir(dir_timetables):
        if file.endswith('.json'):
            table_json = json.load(open(dir_timetables + file, mode='r', encoding='UTF-8'))
            avail_tables[table_json['route']] = table_json['path']
            try: avail_profiles[table_json['route']] = table_json['speed_profiles']
            except KeyError: pass
        else: pass
    choice = easygui.choicebox('Fahrplan auswählen:', 'EBuLa Select', list(avail_tables.keys()))
    if choice == None: sys.exit(0)
    try: altn_name = avail_profiles[choice]
    except KeyError: pass
    pygame.display.set_caption(choice)
    return csv.DictReader(open(dir_timetables + avail_tables[choice], mode='r', encoding='UTF-8'))

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
                        icon_obj = pygame.image.load(dir_icons + 'yen.png')
                        drawQueue.put((icon_obj, (400, 89 + ((14 - (i % 15)) * 38))))
                    case _:
                        font_obj = n_font.render(text.replace('<V>',''), True, (255, 255, 255)) if text.find('<b>') < 0 else b_font.render(text.replace('<b>',''), True, (255, 255, 255))
                        drawQueue.put((font_obj, (450, 92 + ((14 - (i % 15)) * 38))))
                        if text.find('<V>') != -1:
                            icon_obj = pygame.image.load(dir_icons + 'brw.png')
                            drawQueue.put((icon_obj, (400, 89 + ((14 - (i % 15)) * 38))))
    except IndexError: pass

    if altn:
        font_obj = big_font.render(altn_name['1b'], True, (0,0,0))
        drawQueue.put((font_obj, (15,720)))

#fahrplandaten laden
table = loadFile()
rows = list()
for row in table: rows.append(row)