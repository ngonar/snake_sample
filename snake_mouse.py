import pygame
import asyncio

"""
Task :
1. wall collision
2. randomize food 
3. scoring
4. tail addition
5. maps ( level )
6. menu ( retry, new game, options )
"""

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CIRCLE_RADIUS = 15
SPEED = 10

# Colors
RED = (255, 0, 0)

# Global variables
circle_x = SCREEN_WIDTH / 2
circle_y = SCREEN_HEIGHT / 2

circle_color = RED
running = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("KidWe Snake")
clock = pygame.time.Clock()

snake_body = []

async def main():
    global circle_x, circle_y,  circle_color, running

    target_x = 0
    target_y = 0
    speed_x = SPEED
    speed_y = SPEED

    # initial position
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), CIRCLE_RADIUS)

    while running:

        # Check for events
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                target_x, target_y = pygame.mouse.get_pos()

                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, circle_color, (target_x, target_y), CIRCLE_RADIUS)

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
                if pygame.key.name(event.key) == "left":
                    circle_x -= SPEED
                elif event.key == pygame.K_RIGHT:
                    circle_x += SPEED
                elif event.key == pygame.K_UP:
                    circle_y -= SPEED
                elif event.key == pygame.K_DOWN:
                    circle_y += SPEED

                # Draw the circle
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, circle_color, (circle_x, circle_y), CIRCLE_RADIUS)

        pygame.display.flip()


# This is the program entry point
asyncio.run(main())