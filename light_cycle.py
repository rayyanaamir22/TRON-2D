"""
LightCycle object to represent a user's motorcycle on the grid.
"""

# frameworks
from collections import deque
import pygame

# utils
from colours import *

class LightCycle(pygame.sprite.Sprite):
    def __init__(
            self, 
            name: str,
            x, 
            y, 
            initial_dx, 
            initial_dy,
            colour: tuple = white,
            ribbon_length: int = 100,
        ) -> None:
        pygame.sprite.Sprite.__init__(self)
        
        # render
        self.image = pygame.Surface([20, 20])
        self.colour = colour
        self.image.fill(self.colour)

        # physics
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = 10
        self.dx = initial_dx
        self.dy = initial_dy

        # semantics
        self.name = name
        self.alive = True
        self.points = 0
        self.ribbon_length = ribbon_length
        self.ribbon = deque(maxlen=self.ribbon_length)
        
    
    def update_position(self, grid):
        """
        Move the cycle, update the ribbon, and adjust the grid accordingly.
        Returns the removed position (if any) for collision logic if needed.
        """
        # if ribbon is full, remove the oldest position from the grid
        removed = None
        if len(self.ribbon) == self.ribbon.maxlen:
            removed = self.ribbon[0]
            grid.remove_ribbon_position(removed)

        # move and add new position to ribbon and grid
        self.rect.x += self.dx
        self.rect.y += self.dy
        new_pos = (self.rect.x, self.rect.y)
        self.ribbon.append(new_pos)
        grid.add_ribbon_position(new_pos)
        
        return removed
    
    def change_direction(self, dx, dy):
        """
        Change the direction the LightCycle is moving in.
        """
        self.dx = dx
        self.dy = dy
    
    def reset(self, x, y, initial_dx, initial_dy):
        """
        Reset this LightCycle for the start of a new game.
        """

        # speed, pos
        self.rect.x, self.rect.y = x, y
        self.dx = initial_dx
        self.dy = initial_dy

        # empty the ribbon
        self.ribbon.clear()
    
    def draw_ribbon(self, window):
        """
        Modify the light ribbon
        """
        if len(self.ribbon) > 1:
            # convert positions to center points
            points = [(x+10, y+10) for x, y in self.ribbon]
            pygame.draw.lines(window, self.colour, False, points, 3)
        # still draw the cycle head
        pygame.draw.rect(window, self.colour, (self.rect.x, self.rect.y, 20, 20))