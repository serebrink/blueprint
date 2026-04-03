"""
File I/O utilities for AngleHelper application.

Handles saving and loading drawings to/from JSON files.
"""

import json
import os
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from models.drawing import Drawing
from utils.serialization import convert_tuples_to_lists, convert_lists_to_tuples


def save_drawing_to_file(drawing, parent=None):
    """Save a drawing to a JSON file.
    
    Args:
        drawing: Drawing object to save
        parent: Parent widget for file dialog (optional)
        
    Returns:
        True if save was successful, False otherwise
    """
    try:
        # Open file dialog to choose save location
        file_path, _ = QFileDialog.getSaveFileName(
            parent, 
            "Save Drawing", 
            "", 
            "JSON Files (*.json);;All Files (*)"
        )
        
        if not file_path:
            return False
        
        # Ensure .json extension
        if not file_path.endswith('.json'):
            file_path += '.json'
        
        # Convert drawing to dictionary and save as JSON
        drawing_data = drawing.to_dict()
        
        # Convert tuples to lists for JSON serialization
        drawing_data_json = convert_tuples_to_lists(drawing_data)
        with open(file_path, 'w') as f:
            json.dump(drawing_data_json, f, indent=2)
        
        return True
        
    except (IOError, OSError, json.JSONDecodeError) as e:
        error_message = f"Failed to save drawing: {str(e)}"
        if isinstance(e, IOError):
            error_message = f"I/O Error: {str(e)}"
        elif isinstance(e, OSError):
            error_message = f"OS Error: {str(e)}"
        elif isinstance(e, json.JSONDecodeError):
            error_message = f"JSON Error: {str(e)}"
        
        if parent:
            QMessageBox.critical(parent, "Save Error", error_message)
        return False
    except Exception as e:
        if parent:
            QMessageBox.critical(parent, "Save Error", f"Unexpected error: {str(e)}")
        return False


def load_drawing_from_file(parent=None):
    """Load a drawing from a JSON file.
    
    Args:
        parent: Parent widget for file dialog (optional)
        
    Returns:
        Drawing object if load was successful, None otherwise
    """
    try:
        # Open file dialog to choose file to load
        file_path, _ = QFileDialog.getOpenFileName(
            parent,
            "Open Drawing",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        
        if not file_path:
            return None
        
        # Load JSON file and create drawing
        with open(file_path, 'r') as f:
            drawing_data = json.load(f)
        
        # Convert lists back to tuples for our models
        drawing_data_converted = convert_lists_to_tuples(drawing_data)
        return Drawing.from_dict(drawing_data_converted)
        
    except (IOError, OSError, json.JSONDecodeError) as e:
        error_message = f"Failed to load drawing: {str(e)}"
        if isinstance(e, IOError):
            error_message = f"I/O Error: {str(e)}"
        elif isinstance(e, OSError):
            error_message = f"OS Error: {str(e)}"
        elif isinstance(e, json.JSONDecodeError):
            error_message = f"JSON Error: Invalid file format: {str(e)}"
        
        if parent:
            QMessageBox.critical(parent, "Load Error", error_message)
        return None
    except Exception as e:
        if parent:
            QMessageBox.critical(parent, "Load Error", f"Unexpected error: {str(e)}")
        return None


def get_file_extension(filename):
    """Get the file extension from a filename.
    
    Args:
        filename: The filename to process
        
    Returns:
        The file extension in lowercase, or empty string if no extension
    """
    _, ext = os.path.splitext(filename)
    return ext.lower()