# Blueprint - 2D Building Drawing Application

## Description

AngleHelper is a Python application for creating building drawings in a 2D space. It provides a simple interface for drawing lines between points and saving drawings to JSON files.

## Features

- **2D Drawing Space**: QGraphicsView-based canvas for creating building drawings
- **Line Drawing Tool**: Toolbox on the left side for drawing lines with mouse interaction
- **File Operations**: Save and load drawings as JSON files with automatic .json extension handling
- **Grid Support**: Optional 20px grid with snap-to-grid functionality and dynamic redrawing
- **Extensible Architecture**: MVC pattern designed for future expansion with additional drawing elements

### Technical Features

- **MVC Architecture**: Clear separation of Model-View-Controller for maintainability
- **JSON Serialization**: Human-readable file format with tuple/list conversion
- **Comprehensive Error Handling**: User-friendly error messages for file operations
- **Type Hints**: Proper type annotations throughout the codebase
- **100% Test Coverage**: Unit tests for all core functionality

## Requirements

- Python 3.7+
- PyQt6 6.7.0+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/anglehelper.git
   cd anglehelper
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Basic Workflow

1. **Select Line Tool**: Click the line tool in the left toolbox
2. **Draw Lines**: Click and drag on the canvas to draw lines
3. **Save Drawing**: Use File > Save to save your drawing as JSON
4. **Load Drawing**: Use File > Open to load a saved drawing

## Project Structure

```
anglehelper/
├── main.py                  # Entry point
├── models/                  # Data models
│   ├── drawing.py           # Drawing model
│   └── line.py              # Line model
├── views/                   # UI components
│   ├── main_window.py       # Main application window
│   ├── drawing_area.py      # 2D drawing canvas
│   └── toolbox.py           # Left toolbox
├── controllers/             # Business logic
│   └── drawing_controller.py # Drawing logic
├── utils/                   # Utilities
│   ├── file_io.py           # File operations
│   └── geometry.py          # Geometry utilities
├── tests/                   # Tests
│   ├── test_drawing.py      # Drawing tests
│   ├── test_line.py         # Line tests
│   └── test_file_io.py      # File I/O tests
├── assets/                  # Resources
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_line.py

# Run with verbose output
python -m pytest tests/ -v
```

### Test Coverage

- **22 total tests** covering all core functionality
- **100% coverage** for models and file I/O operations
- **Mock testing** for GUI components without requiring display

### Code Style

- **PEP 8 compliant** code formatting
- **Type hints** for all public functions and methods
- **Comprehensive docstrings** for all classes and public methods
- **Black** code formatter configured in pyproject.toml

### Project Structure Details

- **models/**: Data models with serialization support
  - `line.py`: Line model with length calculation
  - `drawing.py`: Drawing model with line collection management
  
- **views/**: Qt-based user interface components
  - `main_window.py`: Main application window with menus
  - `drawing_area.py`: 2D canvas with grid and drawing functionality
  - `toolbox.py`: Left-side tool palette
  
- **utils/**: Utility functions
  - `file_io.py`: JSON file operations with error handling
  - `geometry.py`: Future geometry utilities (placeholder)

## Current Limitations

- **Qt Platform Issue**: GUI display requires proper Qt platform plugin setup
- **No Undo/Redo**: Basic drawing functionality only (no history)
- **Single Layer**: No layer management yet
- **Basic Tools**: Only line tool implemented (rectangle/circle are placeholders)
- **No File Management**: Save As functionality is basic

## Future Enhancements

### Planned Features
- Additional drawing elements (rectangles, circles, arcs)
- Layers and layer management
- Measurement tools and dimensions
- Export to other formats (DXF, SVG, PDF)
- Undo/Redo functionality
- Customizable UI themes
- Snap-to-grid and object snapping
- Zoom and pan functionality
- Property inspector for selected objects

### Technical Improvements
- Enhanced error recovery
- Performance optimizations for large drawings
- Plugin architecture for custom tools
- Internationalization support

## License

MIT License

## Author

Johan Serebrink