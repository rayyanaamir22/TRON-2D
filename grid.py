"""
The Grid. A Digital Frontier.
"""

class Grid:
    def __init__(self, width, height):
        """
        Initialize the grid with a specified width and height.
        
        Args:
            width (int): Width of the grid in pixels.
            height (int): Height of the grid in pixels.
        """
        self.width = width
        self.height = height
        self.occupied = {}  # Dictionary mapping (x, y) tuples to colors

    def is_within_bounds(self, position):
        """
        Check if a position is within the grid boundaries.
        
        Args:
            position (tuple): (x, y) coordinates to check.
        
        Returns:
            bool: True if within bounds, False otherwise.
        """
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def update_ribbon(self, position, colour):
        """
        Update the grid by marking a position as occupied with a ribbon.
        
        Args:
            position (tuple): (x, y) coordinates to update.
            color (tuple): RGB color of the ribbon.
        """
        if self.is_within_bounds(position):
            self.occupied[position] = colour

    def is_occupied(self, position):
        """
        Check if a position is occupied or out of bounds.
        
        Args:
            position (tuple): (x, y) coordinates to check.
        
        Returns:
            bool: True if occupied or out of bounds, False otherwise.
        """
        if not self.is_within_bounds(position):
            return True  # Out of bounds is treated as occupied (causes crash)
        return position in self.occupied

    def clear(self):
        """
        Clear all occupied positions for a new game.
        """
        self.occupied.clear()