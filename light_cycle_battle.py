"""
LightCycleBattle object encapsulating the a light cycle battle game.
"""

# frameworks
import pygame
from collections import defaultdict

# utils
from colours import *
from grid import Grid
from light_cycle import LightCycle


class LightCycleBattle:
    def __init__(
            self,
            width, 
            height, 
            cycles: list[LightCycle]
        ) -> None:
        """
        Initialize a battle with a grid and a list of light cycles.
        
        Args:
            width (int): Width of the grid in pixels.
            height (int): Height of the grid in pixels.
            cycles (list): List of LightCycle objects.
        """
        self.fps = 10
        self.grid = Grid(width, height)
        self.cycles = cycles  # list of LightCycle objects
        self.game_over = False
        self.winner = None

    def update(self):
        """
        Update the game state: move cycles, check collisions, determine game outcome.
        """
        if self.game_over:
            return

        active_cycles = [cycle for cycle in self.cycles if cycle.alive]
        if len(active_cycles) == 0:
            self.game_over = True
            return

        # calculate next positions for all active cycles
        next_positions = defaultdict(list)
        for cycle in active_cycles:
            next_pos = (cycle.rect.x + cycle.dx, cycle.rect.y + cycle.dy)
            next_positions[next_pos].append(cycle)

        # check for collisions
        for cycle in active_cycles:
            next_pos = (cycle.rect.x + cycle.dx, cycle.rect.y + cycle.dy)
            if self.grid.is_occupied(next_pos):
                # collision with ribbon or boundary
                cycle.alive = False
            elif len(next_positions[next_pos]) > 1:
                # head-on collision with another cycle
                for c in next_positions[next_pos]:
                    c.alive = False

        # move cycles that are still alive and update ribbons
        for cycle in active_cycles:
            if cycle.alive:
                # add current position to ribbon and grid before moving
                current_pos = (cycle.rect.x, cycle.rect.y)
                self.grid.update_ribbon(current_pos, cycle.colour)
                cycle.ribbon.append(current_pos)
                # move to next position
                cycle.update_position()

        # game over check
        active_cycles = [cycle for cycle in self.cycles if cycle.alive]
        if len(active_cycles) <= 1:
            self.game_over = True
            if len(active_cycles) == 1:
                self.winner = active_cycles[0]

    def draw(self, window):
        """
        Render the game state to the Pygame window.
        
        Args:
            window (pygame.Surface): The Pygame window to draw on.
        """
        window.fill(black)  # black background
        for cycle in self.cycles:
            if cycle.alive:
                cycle.draw_ribbon(window)
            else:
                # draw ribbon for crashed cycles up to their last position
                if len(cycle.ribbon) > 1:
                    points = [(x + 10, y + 10) for x, y in cycle.ribbon]
                    pygame.draw.lines(window, cycle.colour, False, points, 3)

        if self.game_over:
            font = pygame.font.Font(None, 36)
            if self.winner:
                text = font.render(f"{self.winner.colour} wins!", True, (255, 255, 255))
            else:
                text = font.render("Draw!", True, (255, 255, 255))
            window.blit(text, (window.get_width() // 2 - text.get_width() // 2,
                              window.get_height() // 2 - text.get_height() // 2))

    def handle_input(self, keys):
        """
        Handle player input to change cycle directions.
        
        Args:
            keys (dict): Pygame keys state dictionary.
        """
        # for now, hardcode controls for up to 2 players
        if len(self.cycles) >= 1:
            cycle = self.cycles[0]
            if cycle.alive:
                if keys[pygame.K_UP] and cycle.dy == 0:
                    cycle.change_direction(0, -cycle.speed)
                elif keys[pygame.K_DOWN] and cycle.dy == 0:
                    cycle.change_direction(0, cycle.speed)
                elif keys[pygame.K_LEFT] and cycle.dx == 0:
                    cycle.change_direction(-cycle.speed, 0)
                elif keys[pygame.K_RIGHT] and cycle.dx == 0:
                    cycle.change_direction(cycle.speed, 0)

        if len(self.cycles) >= 2:
            cycle = self.cycles[1]
            if cycle.alive:
                if keys[pygame.K_w] and cycle.dy == 0:
                    cycle.change_direction(0, -cycle.speed)
                elif keys[pygame.K_s] and cycle.dy == 0:
                    cycle.change_direction(0, cycle.speed)
                elif keys[pygame.K_a] and cycle.dx == 0:
                    cycle.change_direction(-cycle.speed, 0)
                elif keys[pygame.K_d] and cycle.dx == 0:
                    cycle.change_direction(cycle.speed, 0)
        
    def run(self):
        """
        Run the game loop for the battle, handling events, updates, and rendering.
        """
        pygame.init()
        window = pygame.display.set_mode((self.grid.width, self.grid.height))
        pygame.display.set_caption("TRON")
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_r:
                        # reset the game on 'R' key press
                        self.game_over = False
                        self.winner = None
                        self.grid.clear()
                        for i, cycle in enumerate(self.cycles):
                            # reset positions and directions (example starting points)
                            x = 100 if i == 0 else 500
                            y = 100 if i == 0 else 500
                            dx = 10 if i == 0 else -10
                            dy = 0
                            cycle.reset(x, y, dx, dy)
                            cycle.alive = True

            if not self.game_over:
                keys = pygame.key.get_pressed()
                self.handle_input(keys)
                self.update()

            self.draw(window)
            pygame.display.flip()
            clock.tick(self.fps)

        pygame.quit()