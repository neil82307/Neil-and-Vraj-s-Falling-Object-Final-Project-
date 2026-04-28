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
    
    
    active_powerup = None
    powerup_timer = 0
    powerup_name = ""
    base_block_speed = 4
    powerup_activated_at = -1

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

        
        if active_powerup is not None:
            powerup_timer += 1
            if powerup_timer >= 5 * FPS:  # 5 seconds
                active_powerup = None
                powerup_timer = 0
                powerup_name = ""
        
        
        current_block_speed = block_speed
        if active_powerup == "slow_motion":
            current_block_speed = block_speed * 0.5

        if alive:
            for b in blocks:
                b[1] += current_block_speed

        for b in blocks:
            if (px < b[0] + BLOCK_SIZE and
                px + PLAYER_SIZE > b[0] and
                py < b[1] + BLOCK_SIZE and
                py + PLAYER_SIZE > b[1]):

                
                if active_powerup == "jackpot" or b[2] == player_color:
                    score += 1
                    blocks.remove(b)
                    if score % 5 == 0:
                        block_speed += 1
                    
                   
                    if score % 15 == 0 and active_powerup is None:
                    
                        if score % 30 == 0:
                            active_powerup = "jackpot"
                            powerup_name = "JACKPOT"
                        else:
                            active_powerup = "slow_motion"
                            powerup_name = "SLOW MOTION"
                        
                        powerup_timer = 0
                        powerup_activated_at = score
                else:
                    alive = False

        blocks = [b for b in blocks if b[1] < SCREEN_HEIGHT]

        screen.fill(BG)
        pygame.draw.rect(screen, player_color, (px, py, PLAYER_SIZE, PLAYER_SIZE))

        for b in blocks:
            block_color = b[2]
            if active_powerup == "jackpot":
                block_color = player_color
            pygame.draw.rect(screen, block_color, (b[0], b[1], BLOCK_SIZE, BLOCK_SIZE))

        screen.blit(font.render("Score: " + str(score), True, TXT), (6, 6))
        
        
        if active_powerup is not None:
            remaining_time = 5 - (powerup_timer // FPS)
            powerup_text = f"{powerup_name}: {remaining_time}s"
            powerup_msg = font.render(powerup_text, True, (255, 0, 0))
            r = powerup_msg.get_rect(center=(SCREEN_WIDTH // 2, 20))
            screen.blit(powerup_msg, r)

        if not alive:
            msg = font.render("You lost. Close window to exit.", True, TXT)
            r = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(msg, r)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()


