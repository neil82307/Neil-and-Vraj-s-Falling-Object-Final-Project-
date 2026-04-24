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
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

 px = SCREEN_WIDTH // 2
    py = SCREEN_HEIGHT - PLAYER_SIZE - 10
    speed = 6
    player_color = random.choice(COLORS)

    blocks = []
    spawn_timer = 0
    block_speed = 4

    score = 0
    alive = True

 while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                  pygame.quit()
                sys.exit()

  keys = pygame.key.get_pressed()
  if alive:
            if keys[pygame.K_LEFT] and px > 0:
                px -= speed
            if keys[pygame.K_RIGHT] and px < SCREEN_WIDTH - PLAYER_SIZE:
                px += speed
            if keys[pygame.K_UP] and py > 0:
                py -= speed
            if keys[pygame.K_DOWN] and py < SCREEN_HEIGHT - PLAYER_SIZE:
                py += speed

spawn_timer += 1
        if spawn_timer > 25:
