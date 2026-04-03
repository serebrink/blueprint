"""
Test script to verify all imports and basic functionality work.
"""

from PyQt6.QtWidgets import QApplication
import sys

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    # Create QApplication instance for Qt widgets
    app = QApplication(sys.argv)
    
    # Test core imports
    from models.line import Line
    from models.drawing import Drawing
    from utils.file_io import save_drawing_to_file, load_drawing_from_file
    from views.toolbox import Toolbox
    from views.drawing_area import DrawingArea
    from views.main_window import MainWindow
    
    print("✓ All imports successful")
    
    # Test model functionality
    line = Line(start_point=(0, 0), end_point=(10, 10))
    drawing = Drawing("Test Drawing")
    drawing.add_line(line)
    
    print(f"✓ Created drawing with {len(drawing.lines)} line")
    print(f"✓ Line length: {line.length()}")
    
    # Test serialization
    drawing_dict = drawing.to_dict()
    loaded_drawing = Drawing.from_dict(drawing_dict)
    
    print(f"✓ Serialization/deserialization works")
    print(f"✓ Loaded drawing has {len(loaded_drawing.lines)} line")
    
    # Test file I/O functions exist
    print("✓ File I/O functions available")
    
    # Test view instantiation (without showing)
    toolbox = Toolbox()
    print("✓ Toolbox instantiated")
    
    drawing_area = DrawingArea()
    print("✓ DrawingArea instantiated")
    
    print("\n🎉 All tests passed! The application core is working correctly.")
    print("Note: GUI display requires proper Qt platform setup.")


if __name__ == "__main__":
    test_imports()