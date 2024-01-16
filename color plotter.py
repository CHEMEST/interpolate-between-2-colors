import pygame
# from Utilities.colors import *
import math
import sys

# Initialize & set up Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Intense Pygame")
clock = pygame.time.Clock()

class TrailCircle:
    def __init__(self, x, y, size, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

def interpolate_color(start_color, end_color, factor):
    r = int(start_color[0] + factor * (end_color[0] - start_color[0]))
    g = int(start_color[1] + factor * (end_color[1] - start_color[1]))
    b = int(start_color[2] + factor * (end_color[2] - start_color[2]))
    return r, g, b

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 25)
running = True
trail_circles = []
angle = 0
colors = [black, green] # EDIT COLORS HERE

colorValue = 0
start_color = colors[colorValue]
end_color = colors[len(colors) - colorValue - 1]


rotated_color = start_color
radius = 10
x = 0
smoothnessFactor = (radius / 4)
y = radius
speed = 0.03 # should probably stay between 0.5 & 2 but doesn't have any actual limits I think
trailSpeed = (radius / 1.2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pass
    trail_circles.append(TrailCircle(x, y, radius, rotated_color))
    if x < width:
        x += trailSpeed - smoothnessFactor
    else:
        x = 0
        y += (radius * 2)

    # Game logic goes here
    angle += speed
    factor = (math.sin(math.radians(angle)) + 1) / 2
    # rotated_color = interpolate_colors(colors, factor)
    rotated_color = interpolate_color(start_color, end_color, factor)
    # if factor > 0.999 and colorValue < len(colors) - 1:
    #     angle = 0
    #     colorValue += 1
    #     start_color = colors[colorValue]
    #     end_color = colors[len(colors) - colorValue - 1]

    # Clear the screen
    screen.fill(white)
    for tCirc in trail_circles:
        tCirc.draw()
    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(480)

# Quit Pygame
pygame.quit()
sys.exit()
