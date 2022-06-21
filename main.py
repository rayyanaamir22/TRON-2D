'''
Name: Rayyan Aamir
Date: June 21, 2022
Program: TRON using Pygame
'''

# RUN IN TERMINAL

# Modules
import pygame

pygame.init() # Initialize

# Create window
window = pygame.display.set_mode((1000, 750)) # Window dimensions
#pygame.display.set_caption('TRON') # Window title

# Set some colour variables
white = (255, 255, 255)
black = (0, 0, 0)
blue, red = (95, 250, 234), (250, 83, 67) # Teams

# Bike class
class Bike(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      self.image = pygame.Surface([20, 20]) # Bike dimensions
      self.rect = self.image.get_rect() # Hitbox
      self.speed = 10 # Speed
      self.points = 0 # Rounds won

# Create the bikes
bike1 = Bike() # Bike 1
bike1.image.fill(blue)
bike1.rect.x, bike1.rect.y = 500, 100 # Initial coords

bike2 = Bike() # Bike 2
bike2.image.fill(red)
bike2.rect.x, bike2.rect.y = 500, 700 # Initial coords

bikeSpeed = 10

allSprites = pygame.sprite.Group()
allSprites.add(bike1, bike2)

# Set default bike directions
x1Change = 0 # Bike 1 is going straight down
y1Change = bikeSpeed

x2Change = 0 # Bike 2 is going straight up
y2Change = -bikeSpeed 

def refresh(): # Redraw the screen
  # Background
  window.fill(black)

  # Title
  font = pygame.font.SysFont('lato', 50)
  title = font.render('TRON', False, white)
  titleRect = title.get_rect()
  titleRect.center = (500, 25)

  # Bike1 wins
  bike1Score = font.render(str(bike1.points), False, blue)
  bike1Rect = bike1Score.get_rect()
  bike1Rect.center = (50, 50)
  window.blit(bike1Score, bike1Rect)

  # Bike2 wins
  bike2Score = font.render(str(bike2.points), False, red)
  bike2Rect = bike2Score.get_rect()
  bike2Rect.center = (50, 700)
  window.blit(bike2Score, bike2Rect)

  window.blit(title, titleRect)
  allSprites.draw(window)
  pygame.display.update()


gameIsDone = False

while not gameIsDone:
    pygame.time.delay(50) # Millisecond delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit
            gameIsDone = True

    key = pygame.key.get_pressed()

    # The bikes are initially moving toward eachother. When the user presses a direction key, they will continue to move in that direction until a new direction is pressed.

    # Player 1 uses arrow keys
    if key[pygame.K_UP]: # P1 up
        x1Change = 0
        y1Change = -bikeSpeed
    if key[pygame.K_DOWN]: # P1 down
        x1Change = 0
        y1Change = bikeSpeed
    if key[pygame.K_RIGHT]: # P1 right
        x1Change = bikeSpeed
        y1Change = 0
    if key[pygame.K_LEFT]: # P1 left
        x1Change = -bikeSpeed
        y1Change = 0

    bike1.rect.x += x1Change
    bike1.rect.y += y1Change

    # Player 2 uses WASD
    if key[pygame.K_w]: # P2 up
        x2Change = 0
        y2Change = -bikeSpeed
    if key[pygame.K_s]: # P2 down
        x2Change = 0
        y2Change = bikeSpeed
    if key[pygame.K_d]: # P2 right
        x2Change = bikeSpeed
        y2Change = 0
    if key[pygame.K_a]: # P2 left
        x2Change = -bikeSpeed
        y2Change = 0

    bike2.rect.x += x2Change
    bike2.rect.y += y2Change

    # bike1 hits wall
    if bike1.rect.x > 1000 or bike1.rect.x < 0 or bike1.rect.y > 750 or bike1.rect.y < 0:
        # Reset initial coords for each bike
        bike1.rect.x, bike1.rect.y = 500, 100 
        bike2.rect.x, bike2.rect.y = 500, 700 
        # Reset bike directions for new round
        x1Change = 0
        y1Change = bikeSpeed
        x2Change = 0
        y2Change = -bikeSpeed

        bike2.points += 1 # bike2 wins the round

    # bike2 hits wall
    if bike2.rect.x > 1000 or bike2.rect.x < 0 or bike2.rect.y > 750 or bike2.rect.y < 0:
        # Reset initial coords for each bike
        bike1.rect.x, bike1.rect.y = 500, 100 
        bike2.rect.x, bike2.rect.y = 500, 700 
        # Reset bike directions for new round
        x1Change = 0
        y1Change = bikeSpeed
        x2Change = 0
        y2Change = -bikeSpeed

        bike1.points += 1 # bike1 wins the round
    

    # Bikes themselves collide
    if bike1.rect.colliderect(bike2.rect): # Considered a tie, no points awarded
        # Reset initial coords for each bike
        bike1.rect.x, bike1.rect.y = 500, 100 
        bike2.rect.x, bike2.rect.y = 500, 700 
        # Reset bike directions for new round
        x1Change = 0
        y1Change = bikeSpeed
        x2Change = 0
        y2Change = -bikeSpeed

    refresh()

pygame.quit()
