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
            bx = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
            by = -BLOCK_SIZE
            color = random.choice(COLORS)
            blocks.append([bx, by, color])
            spawn_timer = 0



        if alive:
            for b in blocks:
                b[1] += block_speed

        for b in blocks:
            if (px < b[0] + BLOCK_SIZE and
                px + PLAYER_SIZE > b[0] and
                py < b[1] + BLOCK_SIZE and
                py + PLAYER_SIZE > b[1]):

                if b[2] != player_color:
                    alive = False
                else:
                    score += 1
                    blocks.remove(b)
                    if score % 5 == 0:
                        block_speed += 1

        blocks = [b for b in blocks if b[1] < SCREEN_HEIGHT]

        screen.fill(BG)
        pygame.draw.rect(screen, player_color, (px, py, PLAYER_SIZE, PLAYER_SIZE))

        for b in blocks:
            pygame.draw.rect(screen, b[2], (b[0], b[1], BLOCK_SIZE, BLOCK_SIZE))

        screen.blit(font.render("Score: " + str(score), True, TXT), (6, 6))

        if not alive:
            msg = font.render("You lost. Close window to exit.", True, TXT)
            r = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(msg, r)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
