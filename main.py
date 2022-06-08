'''
Name: Rayyan Aamir
Date: June 7, 2022
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
bike1.rect.x, bike1.rect.y = 900, 730 # Initial coords

bike2 = Bike() # Bike 2
bike2.rect.x, bike2.rect.y = 100, 730 # Initial coords

bikeSpeed = 10

allSprites = pygame.sprite.Group()
allSprites.add(bike1, bike2)

def refresh(): # Redraw the screen
  # Background
  window.fill(black)

  # Title
  font = pygame.font.SysFont('Comic Sans MS', 30)
  title = font.render('TRON', False, white)
  titleRect = title.get_rect()
  titleRect.center = (500, 25)

  window.blit(title, titleRect)
  allSprites.draw(window)
  pygame.display.update()

gameIsDone = False

while not gameIsDone:
    pygame.time.delay(100) # Millisecond delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit
            gameIsDone = True

    key = pygame.key.get_pressed()

    # Player 1 uses arrow keys
    if key[pygame.K_UP]: # P1 up
        bike1.rect.y -= bikeSpeed
    if key[pygame.K_DOWN]: # P1 down
        bike1.rect.y += bikeSpeed
    if key[pygame.K_RIGHT]: # P1 right
        bike1.rect.x += bikeSpeed
    if key[pygame.K_LEFT]: # P1 left
        bike1.rect.x -= bikeSpeed

    # Player 2 uses ASWD
    if key[pygame.K_w]: # P2 up
        bike2.rect.y -= bikeSpeed
    if key[pygame.K_s]: # P2 down
        bike2.rect.y += bikeSpeed
    if key[pygame.K_d]: # P2 right
        bike2.rect.x += bikeSpeed
    if key[pygame.K_a]: # P2 left
        bike2.rect.x -= bikeSpeed


    refresh()


pygame.quit()
