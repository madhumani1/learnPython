import pygame
import random
import sys


CELL_SIZE = 20
WIDTH = 640
HEIGHT = 480
FPS = 10


def place_apple(snake):
    cols = WIDTH // CELL_SIZE
    rows = HEIGHT // CELL_SIZE
    while True:
        x = random.randrange(0, cols) * CELL_SIZE
        y = random.randrange(0, rows) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)


def draw_text(surface, text, size, color, pos):
    font = pygame.font.SysFont(None, size)
    rendered = font.render(text, True, color)
    surface.blit(rendered, pos)


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    snake = [(CELL_SIZE * 5, CELL_SIZE * 5),
             (CELL_SIZE * 4, CELL_SIZE * 5),
             (CELL_SIZE * 3, CELL_SIZE * 5)]
    direction = 'RIGHT'
    apple = place_apple(snake)
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != 'DOWN':
                    direction = 'UP'
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != 'UP':
                    direction = 'DOWN'
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_r and game_over:
                    return True  # restart
                elif event.key == pygame.K_q and game_over:
                    pygame.quit()
                    sys.exit()

        if not game_over:
            head_x, head_y = snake[0]
            if direction == 'UP':
                head_y -= CELL_SIZE
            elif direction == 'DOWN':
                head_y += CELL_SIZE
            elif direction == 'LEFT':
                head_x -= CELL_SIZE
            elif direction == 'RIGHT':
                head_x += CELL_SIZE

            # Wrap around boundaries (toroidal playfield)
            head_x %= WIDTH
            head_y %= HEIGHT

            new_head = (head_x, head_y)

            # Only self-collision ends the game now
            if new_head in snake:
                game_over = True

            snake.insert(0, new_head)

            if new_head == apple:
                score += 1
                apple = place_apple(snake)
            else:
                snake.pop()

        # Draw
        screen.fill((0, 0, 0))
        # apple
        pygame.draw.rect(screen, (200, 0, 0), (apple[0], apple[1], CELL_SIZE, CELL_SIZE))
        # snake
        for i, part in enumerate(snake):
            color = (0, 200, 0) if i == 0 else (0, 150, 0)
            pygame.draw.rect(screen, color, (part[0], part[1], CELL_SIZE, CELL_SIZE))

        draw_text(screen, f'Score: {score}', 30, (255, 255, 255), (10, 10))

        if game_over:
            draw_text(screen, 'Game Over', 64, (255, 50, 50), (WIDTH // 2 - 140, HEIGHT // 2 - 40))
            draw_text(screen, 'Press R to restart or Q to quit', 28, (200, 200, 200), (WIDTH // 2 - 170, HEIGHT // 2 + 30))

        pygame.display.flip()
        clock.tick(FPS)


def main():
    while True:
        restart = game_loop()
        if not restart:
            break


if __name__ == '__main__':
    main()
