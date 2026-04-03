"""
Drawing model for AngleHelper application.

Represents a complete drawing containing multiple lines and other elements.
"""

from typing import List
from .line import Line


class Drawing:
    """A drawing containing multiple lines and other elements.
    
    Attributes:
        lines (List[Line]): List of Line objects in the drawing
        name (str): Name of the drawing
        grid_enabled (bool): Whether grid is enabled
        grid_size (int): Size of grid cells in pixels
    """
    
    def __init__(self, name="Untitled Drawing"):
        """Initialize a Drawing instance.
        
        Args:
            name: Name of the drawing (default: "Untitled Drawing")
        """
        self.lines: List[Line] = []
        self.name = name
        self.grid_enabled = True
        self.grid_size = 20
    
    def add_line(self, line):
        """Add a line to the drawing.
        
        Args:
            line: Line object to add to the drawing
        """
        self.lines.append(line)
    
    def remove_line(self, line):
        """Remove a line from the drawing.
        
        Args:
            line: Line object to remove from the drawing
        """
        if line in self.lines:
            self.lines.remove(line)
    
    def clear(self):
        """Remove all lines from the drawing."""
        self.lines.clear()
    
    def __repr__(self):
        """Return string representation of the Drawing.
        
        Returns:
            String representation showing drawing name and line count
        """
        return f"Drawing(name='{self.name}', lines={len(self.lines)})"
    
    def to_dict(self):
        """Convert drawing to dictionary for serialization.
        
        Returns:
            Dictionary representation of the drawing
        """
        return {
            'name': self.name,
            'lines': [line.to_dict() for line in self.lines],
            'grid_enabled': self.grid_enabled,
            'grid_size': self.grid_size
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Drawing instance from dictionary.
        
        Args:
            data: Dictionary containing drawing data
            
        Returns:
            Drawing instance
        """
        drawing = cls(name=data.get('name', 'Untitled Drawing'))
        drawing.grid_enabled = data.get('grid_enabled', True)
        drawing.grid_size = data.get('grid_size', 20)
        
        for line_data in data.get('lines', []):
            drawing.add_line(Line.from_dict(line_data))
        
        return drawing