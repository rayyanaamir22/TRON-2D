'''
Name: Rayyan Aamir
Date: June 6, 2022
Program: TRON using Pygame
'''

# RUN IN TERMINAL

# Modules
import pygame

pygame.init() # Initialize

# Create window
window = pygame.display.set_mode((1000, 750)) # Window dimensions
pygame.display.set_caption('TRON') # Window title

# Set some colour variables
white = (255, 255, 255)
black = (0, 0, 0)
blue, red = (95, 250, 234), (250, 83, 67) # Teams

# Bike class
class Bike(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      self.image = pygame.Surface([20, 20]) # Bike dimensions
      self.image.fill(white) # Bike colour
      self.rect = self.image.get_rect() # Hitbox
      self.speed = 10 # Speed

# Create the bikes
bike1 = Bike() # Bike 1
bike1.rect.x, bike1.rect.y = 200, 730 # Initial coords

bike2 = Bike() # Bike 2
bike2.rect.x, bike2.rect.y = 800, 730 # Initial coords

allSprites = pygame.sprite.Group()
allSprites.add(bike1, bike2)

def refresh(): # Redraw the screen
    print('unfinished')

gameIsDone = False

while not gameIsDone:
    pygame.time.delay(100) # Millisecond delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit
            gameIsDone = True

    key = pygame.key.get_pressed()

    refresh()


pygame.quit()
