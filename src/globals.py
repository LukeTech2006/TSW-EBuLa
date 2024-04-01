import pygame, queue, os

#event queue und pygame-font-dings
drawQueue = queue.Queue()
pygame.font.init()
n_font = pygame.font.SysFont('Arial', 24)
b_font = pygame.font.SysFont('Arial', 24, True)
big_font = pygame.font.SysFont('Arial', 28, True)

#datenpfade festlegen
dir_self = os.path.dirname(os.path.realpath(__file__)) + '\\'
dir_timetables = dir_self + 'timetables\\'
dir_icons = dir_self + 'icons\\'

#tastenschlüssel festlegen
key_next = ord('T')
key_prev = ord('G')
key_speed = ord('M')