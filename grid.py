"""
The Grid. A Digital Frontier.
"""

class Grid:
    def __init__(self, width: int, height: int):
        """
        Initialize the grid with a specified width and height.
        
        Args:
            width (int): Width of the grid in pixels.
            height (int): Height of the grid in pixels.
        """
        self.width = width
        self.height = height
        self.occupied = set()  # set of occupied positions

    def is_within_bounds(self, position: tuple):
        """
        Check if a position is within the grid boundaries.
        
        Args:
            position (tuple): (x, y) coordinates to check.
        
        Returns:
            bool: True if within bounds, False otherwise.
        """
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_occupied(self, position: tuple):
        """
        Check if a position is occupied or out of bounds.
        
        Args:
            position (tuple): (x, y) coordinates to check.
        
        Returns:
            bool: True if occupied or out of bounds, False otherwise.
        """
        if not self.is_within_bounds(position):
            return True  # out of bounds is treated as occupied (causes crash)
        return position in self.occupied

    def add_ribbon_position(self, position):
        """
        Add a position to the occupied set.
        
        Args:
            position (tuple): (x, y) coordinates to add.
        """
        if self.is_within_bounds(position):
            self.occupied.add(position)

    def remove_ribbon_position(self, position):
        """
        Remove a position from the occupied set.
        
        Args:
            position (tuple): (x, y) coordinates to remove.
        """
        self.occupied.discard(position)  # Use discard to avoid KeyError if position not present

    def clear(self):
        """
        Clear all occupied positions for a new game.
        """
        self.occupied.clear()