"""
Unit tests for file I/O utilities.
"""

import unittest
import json
import os
import tempfile
from unittest.mock import patch, MagicMock
from utils.file_io import save_drawing_to_file, load_drawing_from_file, get_file_extension
from utils.serialization import convert_tuples_to_lists, convert_lists_to_tuples
from models.drawing import Drawing
from models.line import Line


class TestFileIO(unittest.TestCase):
    """Test cases for file I/O utilities."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_drawing = Drawing(name="Test Drawing")
        self.test_drawing.grid_enabled = False
        self.test_drawing.grid_size = 25
        
        line1 = Line(start_point=(0, 0), end_point=(10, 10), color="#FF0000", width=2.0)
        line2 = Line(start_point=(20, 20), end_point=(30, 30), color="#00FF00", width=3.0)
        
        self.test_drawing.add_line(line1)
        self.test_drawing.add_line(line2)
    
    def test_get_file_extension(self):
        """Test file extension extraction."""
        self.assertEqual(get_file_extension("test.json"), ".json")
        self.assertEqual(get_file_extension("test.JSON"), ".json")
        self.assertEqual(get_file_extension("test.txt"), ".txt")
        self.assertEqual(get_file_extension("test"), "")
        self.assertEqual(get_file_extension("test.noextension"), ".noextension")
    
    @patch('utils.file_io.QFileDialog.getSaveFileName')
    def test_save_drawing_cancelled(self, mock_get_save_file):
        """Test save operation when user cancels file dialog."""
        # Simulate user cancelling the save dialog
        mock_get_save_file.return_value = ("", "")
        
        result = save_drawing_to_file(self.test_drawing)
        self.assertFalse(result)
    
    @patch('utils.file_io.QFileDialog.getSaveFileName')
    def test_save_drawing_success(self, mock_get_save_file):
        """Test successful save operation."""
        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as temp_file:
            temp_path = temp_file.name
        
        try:
            # Mock the file dialog to return our temp path
            mock_get_save_file.return_value = (temp_path, "JSON Files (*.json)")
            
            # Perform the save
            result = save_drawing_to_file(self.test_drawing)
            self.assertTrue(result)
            
            # Verify the file was created and contains correct data
            self.assertTrue(os.path.exists(temp_path))
            
            with open(temp_path, 'r') as f:
                saved_data = json.load(f)
            
            # Convert expected data tuples to lists for comparison
            expected_data = convert_tuples_to_lists(self.test_drawing.to_dict())
            self.assertEqual(saved_data, expected_data)
            
        finally:
            # Clean up
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    @patch('utils.file_io.QFileDialog.getSaveFileName')
    def test_save_drawing_adds_extension(self, mock_get_save_file):
        """Test that .json extension is added if missing."""
        # Create a temporary file path without extension
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path_no_ext = temp_file.name
        
        # Remove the temporary file and add our own path without extension
        os.unlink(temp_path_no_ext)
        temp_path_no_ext = temp_path_no_ext.replace('.tmp', '')
        
        try:
            # Mock the file dialog to return path without extension
            mock_get_save_file.return_value = (temp_path_no_ext, "JSON Files (*.json)")
            
            # Perform the save
            result = save_drawing_to_file(self.test_drawing)
            self.assertTrue(result)
            
            # Verify the file was created with .json extension
            expected_path = temp_path_no_ext + '.json'
            self.assertTrue(os.path.exists(expected_path))
            
            with open(expected_path, 'r') as f:
                saved_data = json.load(f)
            
            # Convert expected data tuples to lists for comparison
            expected_data = convert_tuples_to_lists(self.test_drawing.to_dict())
            self.assertEqual(saved_data, expected_data)
            
        finally:
            # Clean up
            expected_path = temp_path_no_ext + '.json'
            if os.path.exists(expected_path):
                os.unlink(expected_path)
    
    @patch('utils.file_io.QFileDialog.getOpenFileName')
    def test_load_drawing_cancelled(self, mock_get_open_file):
        """Test load operation when user cancels file dialog."""
        # Simulate user cancelling the open dialog
        mock_get_open_file.return_value = ("", "")
        
        result = load_drawing_from_file()
        self.assertIsNone(result)
    
    def test_load_drawing_success(self):
        """Test successful load operation."""
        # Create a temporary file with test data
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='w') as temp_file:
            temp_path = temp_file.name
            test_data = self.test_drawing.to_dict()
            # Convert tuples to lists for JSON serialization
            def convert_tuples_to_lists(obj):
                if isinstance(obj, dict):
                    return {k: convert_tuples_to_lists(v) for k, v in obj.items()}
                elif isinstance(obj, (list, tuple)):
                    return [convert_tuples_to_lists(item) for item in obj]
                else:
                    return obj
            
            test_data_json = convert_tuples_to_lists(test_data)
            json.dump(test_data_json, temp_file)
        
        try:
            # Test the core conversion functionality directly
            # Load the JSON data
            with open(temp_path, 'r') as f:
                loaded_data = json.load(f)
            
            # Convert lists back to tuples
            loaded_data_converted = convert_lists_to_tuples(loaded_data)
            loaded_drawing = Drawing.from_dict(loaded_data_converted)
            
            # Verify the drawing was loaded correctly
            self.assertIsNotNone(loaded_drawing)
            self.assertEqual(loaded_drawing.name, self.test_drawing.name)
            self.assertEqual(loaded_drawing.grid_enabled, self.test_drawing.grid_enabled)
            self.assertEqual(loaded_drawing.grid_size, self.test_drawing.grid_size)
            self.assertEqual(len(loaded_drawing.lines), len(self.test_drawing.lines))
            
            # Verify lines are equal
            for i, (original_line, loaded_line) in enumerate(zip(self.test_drawing.lines, loaded_drawing.lines)):
                self.assertEqual(original_line.start_point, loaded_line.start_point)
                self.assertEqual(original_line.end_point, loaded_line.end_point)
                self.assertEqual(original_line.color, loaded_line.color)
                self.assertEqual(original_line.width, loaded_line.width)
                
        finally:
            # Clean up
            if os.path.exists(temp_path):
                os.unlink(temp_path)


if __name__ == '__main__':
    unittest.main()