"""
Unit tests for Line model.
"""

import unittest
from models.line import Line


class TestLine(unittest.TestCase):
    """Test cases for Line model."""
    
    def test_initialization(self):
        """Test Line initialization with default values."""
        line = Line()
        self.assertEqual(line.start_point, (0, 0))
        self.assertEqual(line.end_point, (0, 0))
        self.assertEqual(line.color, "#000000")
        self.assertEqual(line.width, 1.0)
    
    def test_custom_initialization(self):
        """Test Line initialization with custom values."""
        line = Line(start_point=(10, 20), end_point=(30, 40), color="#FF0000", width=2.5)
        self.assertEqual(line.start_point, (10, 20))
        self.assertEqual(line.end_point, (30, 40))
        self.assertEqual(line.color, "#FF0000")
        self.assertEqual(line.width, 2.5)
    
    def test_length_calculation(self):
        """Test line length calculation."""
        line = Line(start_point=(0, 0), end_point=(3, 4))
        self.assertEqual(line.length(), 5.0)
        
        line2 = Line(start_point=(1, 1), end_point=(4, 5))
        self.assertAlmostEqual(line2.length(), 5.0, places=6)
    
    def test_repr(self):
        """Test string representation."""
        line = Line(start_point=(10, 20), end_point=(30, 40))
        self.assertEqual(repr(line), "Line(start_point=(10, 20), end_point=(30, 40))")
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        line = Line(start_point=(5, 10), end_point=(15, 20), color="#00FF00", width=3.0)
        expected_dict = {
            'start_point': (5, 10),
            'end_point': (15, 20),
            'color': '#00FF00',
            'width': 3.0
        }
        self.assertEqual(line.to_dict(), expected_dict)
    
    def test_from_dict(self):
        """Test creation from dictionary."""
        data = {
            'start_point': [100, 200],
            'end_point': [300, 400],
            'color': '#0000FF',
            'width': 4.5
        }
        line = Line.from_dict(data)
        self.assertEqual(line.start_point, (100, 200))
        self.assertEqual(line.end_point, (300, 400))
        self.assertEqual(line.color, "#0000FF")
        self.assertEqual(line.width, 4.5)
    
    def test_from_dict_defaults(self):
        """Test creation from dictionary with missing values."""
        data = {
            'start_point': [50, 60],
            'end_point': [70, 80]
            # Missing color and width
        }
        line = Line.from_dict(data)
        self.assertEqual(line.start_point, (50, 60))
        self.assertEqual(line.end_point, (70, 80))
        self.assertEqual(line.color, "#000000")  # Default color
        self.assertEqual(line.width, 1.0)  # Default width


if __name__ == '__main__':
    unittest.main()