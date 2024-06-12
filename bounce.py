"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc

-------------------------------------------------

Author for the Brickout game is Christian Bender
That includes the classes Ball, Paddle, Brick, and BrickWall.

"""
 
import pygame

from ball import Ball
from platforms import *
from notes import *

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 700)
screen = pygame.display.set_mode(size)
 
x = 0
y = 0

camera_offset = [0, 0]

# The game objects ball
ball = Ball(screen,5,x,y)

group = PlatformGroup(screen)

Vx = 1
dt = 30
Vy = 0
g = 0.5

x -= 5
y += 5

for i in range(len(notes)):

    dt = notes[i]

    x = round(x + Vx*dt)
    y = round(y + (-Vy*0.8)*dt + g*dt*dt/2)

    Vy = (-Vy*0.8) + g*dt


    group.add(50, 5, x - 5, y)


 
pygame.display.set_caption("Brickout-game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
   
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    ball.update(group)


    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    camera_offset = ball.getPosition() 
    camera_offset[0] -= 350
    camera_offset[1] -= 350

    # --- Drawing code should go here
    ball.draw(camera_offset)

    group.draw(camera_offset)
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()