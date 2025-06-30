import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        self.size = 800
        self.snake = [(400, 400), (420, 400), (440, 400)]
        self.direction = 'RIGHT'
        self.apple = self.get_random_apple()
        self.score = 0

    def get_random_apple(self):
        return (random.randint(0, 790) // 20 * 20, random.randint(0, 790) // 20 * 20)

    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'RIGHT':
            new_head = (head[0] + 20, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0] - 20, head[1])
        elif self.direction == 'UP':
            new_head = (head[0], head[1] - 20)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + 20)
        self.snake.insert(0, new_head)

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            return True
        if head[0] < 0 or head[0] > self.size or head[1] < 0 or head[1] > self.size:
            return True
        return False

    def check_apple(self):
        head = self.snake[0]
        if head == self.apple:
            self.score += 1
            self.apple = self.get_random_apple()
        else:
            self.snake.pop()

    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((self.size, self.size))
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'
            self.move_snake()
            self.check_apple()
            if self.check_collision():
                break
            screen.fill((0, 0, 0))
            for pos in self.snake:
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.apple[0], self.apple[1], 20, 20))
            pygame.display.flip()
            clock.tick(10)
        print(f'Game Over! Your score is {self.score}')