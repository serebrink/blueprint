"""
Integration tests for AngleHelper application.

Tests complete workflows and interactions between components.
"""

import unittest
import tempfile
import os
import json
from models.drawing import Drawing
from models.line import Line
from utils.serialization import convert_tuples_to_lists, convert_lists_to_tuples


class TestIntegration(unittest.TestCase):
    """Integration test cases for AngleHelper."""
    
    def test_complete_drawing_workflow(self):
        """Test the complete workflow: create drawing → add lines → serialize → deserialize → verify."""
        # Step 1: Create a drawing
        drawing = Drawing(name="Integration Test Drawing")
        drawing.grid_enabled = True
        drawing.grid_size = 25
        
        # Step 2: Add some lines
        line1 = Line(start_point=(0, 0), end_point=(100, 100), color="#FF0000", width=2.5)
        line2 = Line(start_point=(50, 50), end_point=(150, 150), color="#00FF00", width=1.5)
        
        drawing.add_line(line1)
        drawing.add_line(line2)
        
        # Step 3: Serialize to JSON-compatible format
        drawing_dict = drawing.to_dict()
        drawing_json = convert_tuples_to_lists(drawing_dict)
        
        # Step 4: Save to temporary file
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='w') as temp_file:
            temp_path = temp_file.name
            json.dump(drawing_json, temp_file)
        
        try:
            # Step 5: Load from file
            with open(temp_path, 'r') as f:
                loaded_data = json.load(f)
            
            # Step 6: Deserialize
            loaded_data_converted = convert_lists_to_tuples(loaded_data)
            loaded_drawing = Drawing.from_dict(loaded_data_converted)
            
            # Step 7: Verify integrity
            self.assertEqual(loaded_drawing.name, drawing.name)
            self.assertEqual(loaded_drawing.grid_enabled, drawing.grid_enabled)
            self.assertEqual(loaded_drawing.grid_size, drawing.grid_size)
            self.assertEqual(len(loaded_drawing.lines), len(drawing.lines))
            
            # Verify lines are identical
            for i, (original_line, loaded_line) in enumerate(zip(drawing.lines, loaded_drawing.lines)):
                self.assertEqual(original_line.start_point, loaded_line.start_point)
                self.assertEqual(original_line.end_point, loaded_line.end_point)
                self.assertEqual(original_line.color, loaded_line.color)
                self.assertEqual(original_line.width, loaded_line.width)
                
                # Verify line length calculation
                self.assertAlmostEqual(original_line.length(), loaded_line.length(), places=6)
                
        finally:
            # Cleanup
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_line_operations_workflow(self):
        """Test line creation, modification, and removal workflow."""
        drawing = Drawing("Line Operations Test")
        
        # Create lines
        line1 = Line((0, 0), (10, 10))
        line2 = Line((20, 20), (30, 30))
        line3 = Line((40, 40), (50, 50))
        
        # Add lines
        drawing.add_line(line1)
        drawing.add_line(line2)
        drawing.add_line(line3)
        
        self.assertEqual(len(drawing.lines), 3)
        
        # Remove a line
        drawing.remove_line(line2)
        self.assertEqual(len(drawing.lines), 2)
        self.assertNotIn(line2, drawing.lines)
        
        # Clear all lines
        drawing.clear()
        self.assertEqual(len(drawing.lines), 0)
        
        # Add lines again
        drawing.add_line(line1)
        drawing.add_line(Line((100, 100), (200, 200), color="#0000FF"))
        
        self.assertEqual(len(drawing.lines), 2)
        
        # Verify serialization still works
        drawing_dict = drawing.to_dict()
        self.assertEqual(len(drawing_dict['lines']), 2)
    
    def test_grid_settings_workflow(self):
        """Test grid settings preservation through serialization."""
        # Create drawing with custom grid settings
        drawing = Drawing("Grid Test")
        drawing.grid_enabled = False
        drawing.grid_size = 30
        
        # Add a line
        drawing.add_line(Line((0, 0), (10, 10)))
        
        # Serialize and deserialize
        drawing_dict = drawing.to_dict()
        drawing_json = convert_tuples_to_lists(drawing_dict)
        
        # Simulate file I/O
        temp_data = json.dumps(drawing_json)
        loaded_data = json.loads(temp_data)
        
        loaded_data_converted = convert_lists_to_tuples(loaded_data)
        loaded_drawing = Drawing.from_dict(loaded_data_converted)
        
        # Verify grid settings preserved
        self.assertEqual(loaded_drawing.grid_enabled, False)
        self.assertEqual(loaded_drawing.grid_size, 30)
        self.assertEqual(loaded_drawing.name, "Grid Test")
        self.assertEqual(len(loaded_drawing.lines), 1)


if __name__ == '__main__':
    unittest.main()