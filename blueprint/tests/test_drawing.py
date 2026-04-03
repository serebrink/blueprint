"""
Unit tests for Drawing model.
"""

import unittest
from models.drawing import Drawing
from models.line import Line


class TestDrawing(unittest.TestCase):
    """Test cases for Drawing model."""
    
    def test_initialization(self):
        """Test Drawing initialization with default values."""
        drawing = Drawing()
        self.assertEqual(drawing.name, "Untitled Drawing")
        self.assertEqual(len(drawing.lines), 0)
        self.assertTrue(drawing.grid_enabled)
        self.assertEqual(drawing.grid_size, 20)
    
    def test_custom_initialization(self):
        """Test Drawing initialization with custom name."""
        drawing = Drawing(name="Test Drawing")
        self.assertEqual(drawing.name, "Test Drawing")
        self.assertEqual(len(drawing.lines), 0)
    
    def test_add_line(self):
        """Test adding lines to drawing."""
        drawing = Drawing()
        line1 = Line(start_point=(0, 0), end_point=(10, 10))
        line2 = Line(start_point=(20, 20), end_point=(30, 30))
        
        drawing.add_line(line1)
        self.assertEqual(len(drawing.lines), 1)
        self.assertIn(line1, drawing.lines)
        
        drawing.add_line(line2)
        self.assertEqual(len(drawing.lines), 2)
        self.assertIn(line2, drawing.lines)
    
    def test_remove_line(self):
        """Test removing lines from drawing."""
        drawing = Drawing()
        line1 = Line(start_point=(0, 0), end_point=(10, 10))
        line2 = Line(start_point=(20, 20), end_point=(30, 30))
        
        drawing.add_line(line1)
        drawing.add_line(line2)
        self.assertEqual(len(drawing.lines), 2)
        
        drawing.remove_line(line1)
        self.assertEqual(len(drawing.lines), 1)
        self.assertNotIn(line1, drawing.lines)
        self.assertIn(line2, drawing.lines)
    
    def test_clear(self):
        """Test clearing all lines from drawing."""
        drawing = Drawing()
        line1 = Line(start_point=(0, 0), end_point=(10, 10))
        line2 = Line(start_point=(20, 20), end_point=(30, 30))
        
        drawing.add_line(line1)
        drawing.add_line(line2)
        self.assertEqual(len(drawing.lines), 2)
        
        drawing.clear()
        self.assertEqual(len(drawing.lines), 0)
    
    def test_repr(self):
        """Test string representation."""
        drawing = Drawing(name="Test Drawing")
        line = Line(start_point=(0, 0), end_point=(10, 10))
        drawing.add_line(line)
        
        self.assertEqual(repr(drawing), "Drawing(name='Test Drawing', lines=1)")
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        drawing = Drawing(name="Test Drawing")
        drawing.grid_enabled = False
        drawing.grid_size = 25
        
        line1 = Line(start_point=(0, 0), end_point=(10, 10), color="#FF0000", width=2.0)
        line2 = Line(start_point=(20, 20), end_point=(30, 30), color="#00FF00", width=3.0)
        
        drawing.add_line(line1)
        drawing.add_line(line2)
        
        expected_dict = {
            'name': 'Test Drawing',
            'lines': [
                {
                    'start_point': (0, 0),
                    'end_point': (10, 10),
                    'color': '#FF0000',
                    'width': 2.0
                },
                {
                    'start_point': (20, 20),
                    'end_point': (30, 30),
                    'color': '#00FF00',
                    'width': 3.0
                }
            ],
            'grid_enabled': False,
            'grid_size': 25
        }
        
        self.assertEqual(drawing.to_dict(), expected_dict)
    
    def test_from_dict(self):
        """Test creation from dictionary."""
        data = {
            'name': 'Loaded Drawing',
            'lines': [
                {
                    'start_point': [5, 5],
                    'end_point': [15, 15],
                    'color': '#0000FF',
                    'width': 1.5
                }
            ],
            'grid_enabled': True,
            'grid_size': 30
        }
        
        drawing = Drawing.from_dict(data)
        self.assertEqual(drawing.name, "Loaded Drawing")
        self.assertEqual(len(drawing.lines), 1)
        self.assertTrue(drawing.grid_enabled)
        self.assertEqual(drawing.grid_size, 30)
        
        line = drawing.lines[0]
        self.assertEqual(line.start_point, (5, 5))
        self.assertEqual(line.end_point, (15, 15))
        self.assertEqual(line.color, "#0000FF")
        self.assertEqual(line.width, 1.5)
    
    def test_from_dict_defaults(self):
        """Test creation from dictionary with missing values."""
        data = {
            'lines': [
                {
                    'start_point': [1, 1],
                    'end_point': [2, 2]
                }
            ]
            # Missing name, grid_enabled, grid_size
        }
        
        drawing = Drawing.from_dict(data)
        self.assertEqual(drawing.name, "Untitled Drawing")  # Default name
        self.assertEqual(len(drawing.lines), 1)
        self.assertTrue(drawing.grid_enabled)  # Default grid_enabled
        self.assertEqual(drawing.grid_size, 20)  # Default grid_size


if __name__ == '__main__':
    unittest.main()