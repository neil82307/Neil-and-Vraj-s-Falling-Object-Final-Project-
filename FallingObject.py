import pygame
import random
import sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
PLAYER_SIZE = 30
BLOCK_SIZE = 30
FPS = 60

BG = (240, 240, 240)
TXT = (0, 0, 0)

COLORS = [
    (200, 30, 30),
      (30, 200, 30),
    (30, 30, 200)
]

def main():
    pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
