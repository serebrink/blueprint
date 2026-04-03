# Blueprint - 2D Building Drawing Application

## Description

AngleHelper is a Python application for creating building drawings in a 2D space. It provides a simple interface for drawing lines between points and saving drawings to JSON files.

## Features

- **2D Drawing Space**: Central canvas for creating building drawings
- **Line Drawing Tool**: Toolbox on the left side for drawing lines
- **File Operations**: Save and load drawings as JSON files
- **Grid Support**: Optional grid with snap-to-grid functionality
- **Extensible Architecture**: Designed for future expansion with additional drawing elements

## Requirements

- Python 3.7+
- PyQt5 5.15.9+

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
python -m pytest tests/
```

### Code Style

Follow PEP 8 guidelines and include docstrings for all public classes and methods.

## Future Enhancements

- Additional drawing elements (rectangles, circles, arcs)
- Layers and layer management
- Measurement tools
- Export to other formats (DXF, SVG)
- Undo/Redo functionality
- Customizable UI themes

## License

MIT License

## Author

Johan Serebrink