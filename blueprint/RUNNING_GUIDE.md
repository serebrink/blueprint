# Blueprint Running Guide

## Quick Start

### From VS Code (Recommended)

1. **Open the project** in VS Code
2. **Select Python interpreter**:
   - Bottom-left corner shows current interpreter
   - Click and select `./venv/bin/python`
3. **Debug**:
   - Select "Debug AngleHelper with Venv" configuration
   - Press F5 or click the debug button

### From Terminal

```bash
# Navigate to project root
cd /path/to/anglehelper

# Activate virtual environment
source venv/bin/activate

# Run the application
python -m anglehelper.main
```

## Common Commands

### Installation
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running
```bash
# Run application
python -m anglehelper.main

# Run with offscreen platform (no display)
QT_QPA_PLATFORM=offscreen python -m anglehelper.main

# Run with Wayland
QT_QPA_PLATFORM=wayland python -m anglehelper.main
```

### Testing
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_line.py -v

# Run with coverage
python -m pytest tests/ --cov=anglehelper --cov-report=term-missing
```

### Development
```bash
# Format code
black anglehelper/ tests/

# Lint code
flake8 anglehelper/ tests/

# Type check
mypy anglehelper/
```

## Troubleshooting

### PyQt6 not found
```bash
# Check if installed
pip show PyQt6

# Install if missing
pip install PyQt6==6.7.0

# Verify in Python
python -c "import PyQt6; print('PyQt6 available')"
```

### Qt platform errors
```bash
# Try different platforms
QT_QPA_PLATFORM=offscreen python -m anglehelper.main
QT_QPA_PLATFORM=wayland python -m anglehelper.main
QT_QPA_PLATFORM=xcb python -m anglehelper.main

# Install missing dependencies (Ubuntu/Debian)
sudo apt install libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-util1
```

### VS Code issues
```bash
# Check selected interpreter
code --list-extensions | grep Python

# Set interpreter manually
"python.pythonPath": "${workspaceFolder}/venv/bin/python"

# Restart VS Code after changes
code .
```

## Project Structure

```
anglehelper/
├── .vscode/                # VS Code configuration
│   ├── launch.json        # Debug configurations
│   └── settings.json      # Workspace settings
├── anglehelper/            # Python package
│   ├── __init__.py        # Package initialization
│   ├── main.py            # Entry point
│   ├── models/            # Data models
│   ├── views/             # UI components
│   ├── utils/             # Utilities
│   └── tests/            # Test suite
├── venv/                   # Virtual environment
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── .gitignore             # Git ignore rules
├── CONTRIBUTING.md        # Contribution guidelines
├── pyproject.toml         # Project configuration
└── README.md              # Project documentation
```

## Key Files

- **Entry point**: `anglehelper/main.py`
- **Main window**: `anglehelper/views/main_window.py`
- **Drawing area**: `anglehelper/views/drawing_area.py`
- **Models**: `anglehelper/models/line.py`, `anglehelper/models/drawing.py`
- **File I/O**: `anglehelper/utils/file_io.py`

## Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `QT_QPA_PLATFORM` | Qt platform backend | `offscreen`, `wayland`, `xcb` |
| `VIRTUAL_ENV` | Virtual environment path | `/path/to/venv` |

## Best Practices

1. **Always use virtual environment**
2. **Activate before running** (`source venv/bin/activate`)
3. **Use module syntax** (`python -m anglehelper.main`)
4. **Check interpreter** in VS Code status bar
5. **Run tests frequently** (`python -m pytest tests/`)

## Support

For issues, check:
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development setup
- [Troubleshooting section](#troubleshooting) - Common issues
- [VS Code Setup](#vs-code-setup-and-debugging) - IDE configuration

Need help? Open an issue or check the [documentation](README.md).