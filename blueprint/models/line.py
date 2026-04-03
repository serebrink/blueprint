"""
Line model for AngleHelper application.

Represents a line segment between two points in 2D space.
"""

class Line:
    """A line segment defined by start and end points.
    
    Attributes:
        start_point (tuple): (x, y) coordinates of the start point
        end_point (tuple): (x, y) coordinates of the end point
        color (str): Line color in hex format
        width (float): Line width in pixels
    """
    
    def __init__(self, start_point=(0, 0), end_point=(0, 0), color="#000000", width=1.0):
        """Initialize a Line instance.
        
        Args:
            start_point: Tuple of (x, y) coordinates for start point
            end_point: Tuple of (x, y) coordinates for end point
            color: Line color in hex format (default: black)
            width: Line width in pixels (default: 1.0)
        """
        self.start_point = start_point
        self.end_point = end_point
        self.color = color
        self.width = width
    
    def __repr__(self):
        """Return string representation of the Line.
        
        Returns:
            String representation showing start and end points
        """
        return f"Line(start_point={self.start_point}, end_point={self.end_point})"
    
    def length(self):
        """Calculate the length of the line.
        
        Returns:
            Float representing the length of the line
        """
        x1, y1 = self.start_point
        x2, y2 = self.end_point
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def to_dict(self):
        """Convert line to dictionary for serialization.
        
        Returns:
            Dictionary representation of the line
        """
        return {
            'start_point': self.start_point,
            'end_point': self.end_point,
            'color': self.color,
            'width': self.width
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Line instance from dictionary.
        
        Args:
            data: Dictionary containing line data
            
        Returns:
            Line instance
        """
        return cls(
            start_point=tuple(data['start_point']),
            end_point=tuple(data['end_point']),
            color=data.get('color', '#000000'),
            width=data.get('width', 1.0)
        )