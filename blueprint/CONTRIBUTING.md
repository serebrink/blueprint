# Contributing to Blueprint

Welcome to Blueprint! We appreciate your interest in contributing to this 2D building drawing application.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Development Setup

### Prerequisites
- Python 3.7+
- Git
- Virtual environment tool (venv, virtualenv, etc.)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/anglehelper.git
   cd anglehelper
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # For development
   ```

4. **Install pre-commit hooks:**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Coding Standards

### Python Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters
- Use descriptive variable and function names
- Follow `snake_case` for variables/functions, `CamelCase` for classes

### Type Hints
- Use Python type hints for all public functions and methods
- Use `Optional` and `Union` from `typing` module when needed
- Avoid `Any` type when possible

### Docstrings
- Follow [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Document all public classes, methods, and functions
- Include parameter types and descriptions
- Include return value types and descriptions

### Example
```python
class DrawingArea(QGraphicsView):
    """Drawing area widget for creating 2D drawings.
    
    This widget provides the 2D drawing canvas where users can create 
    building drawings with grid support and various drawing tools.
    
    Attributes:
        scene: QGraphicsScene for managing drawing elements
        drawing: Current Drawing model
        grid_visible: Whether grid is visible
        grid_size: Size of grid cells in pixels
    """
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the drawing area.
        
        Args:
            parent: Optional parent widget
        """
        super().__init__(parent)
        # Implementation...
```

## Commit Guidelines

### Commit Messages
- Follow [Conventional Commits](https://www.conventionalcommits.org/) format
- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Use imperative mood

### Examples
```bash
# Good examples
git commit -m "feat: add line drawing tool"
git commit -m "fix: resolve grid rendering issue"
git commit -m "docs: update contributing guidelines"
git commit -m "refactor: improve file I/O error handling"
git commit -m "test: add integration tests for drawing workflow"

# Bad examples
git commit -m "fixed bug"
git commit -m "added some features"
git commit -m "WIP"
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Build process or auxiliary tool changes
- `perf`: Performance improvements
- `ci`: CI configuration changes

## Testing

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_line.py

# Run with verbose output
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=anglehelper --cov-report=term-missing
```

### Test Requirements
- All new features must include unit tests
- Maintain at least 90% test coverage
- Test edge cases and error conditions
- Use descriptive test names

### Test Structure
```python
def test_function_name_when_condition_expected_result():
    # Arrange
    input_data = ...
    expected = ...
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result == expected
```

## Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Create a descriptive branch name:**
   - `feat/feature-name` for new features
   - `fix/issue-description` for bug fixes
   - `docs/doc-updates` for documentation
3. **Make your changes** following coding standards
4. **Write tests** for new functionality
5. **Run tests locally** to ensure nothing breaks
6. **Update documentation** if needed
7. **Push to your fork** and submit a pull request
8. **Fill out the PR template** completely

## Code Review Process

- All pull requests require at least one approval
- Reviewers will check for:
  - Code quality and style
  - Test coverage
  - Documentation
  - Performance considerations
  - Security implications
- Address review comments promptly
- Update the PR with any changes

## Development Workflow

### Branching Strategy
- `main`: Stable production-ready code
- `develop`: Integration branch for features
- Feature branches: `feat/description`
- Bug fix branches: `fix/description`
- Release branches: `release/version`

### Versioning
- Follow [Semantic Versioning](https://semver.org/)
- `MAJOR.MINOR.PATCH` format
- Update version in `__init__.py` and `pyproject.toml`

## VS Code Setup and Debugging

### Prerequisites
- VS Code with Python extension installed
- Virtual environment created (`python3 -m venv venv`)
- Dependencies installed (`pip install -r requirements.txt`)

### Configuration Steps

1. **Set Python Interpreter:**
   - Open Command Palette (Ctrl+Shift+P)
   - Select "Python: Select Interpreter"
   - Choose `./venv/bin/python` (Linux/Mac) or `./venv/Scripts/python.exe` (Windows)

2. **Install Recommended Extensions:**
   - Python (Microsoft) - Essential Python support
   - Pylance - Advanced type checking
   - Black Formatter - Auto-code formatting
   - Flake8 - Linting support
   - pytest - Test runner integration

3. **Configure Launch Settings:**
   - VS Code launch configurations are provided in `.vscode/launch.json`
   - Three configurations available:
     - **Debug AngleHelper with Venv**: Main application debugging
     - **Run Current File**: Execute current Python file
     - **Run Tests**: Run test suite with pytest

4. **Workspace Settings:**
   - VS Code workspace settings in `.vscode/settings.json`
   - Configures Python path, linting, formatting, and testing
   - Automatically excludes `venv/` and `__pycache__` from file explorer

### Debugging

1. **Set breakpoints** in your code by clicking in the gutter
2. **Select debug configuration** from the dropdown (top of debug panel)
3. **Press F5** or click the green debug button
4. **Verify environment**: Debug console should show virtual environment is active

### Running the Application

**Method 1: Using VS Code Debug**
- Select "Debug AngleHelper with Venv" configuration
- Press F5 to start debugging

**Method 2: Using VS Code Terminal**
```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
python -m anglehelper.main
```

**Method 3: Direct Execution**
```bash
# From project root
python -m anglehelper.main

# From inner anglehelper directory
cd anglehelper && python main.py
```

### Troubleshooting

**Issue: "ModuleNotFoundError: No module named 'PyQt6'"**
- **Cause**: VS Code not using virtual environment
- **Solution**:
  1. Check bottom-left corner for Python interpreter
  2. Click on it and select the venv interpreter
  3. Restart VS Code after changing interpreter
  4. Verify with: `pip show PyQt6`

**Issue: Debug button doesn't work**
- **Cause**: Incorrect launch configuration
- **Solution**:
  1. Check `.vscode/launch.json` exists
  2. Ensure "python" path points to `venv/bin/python`
  3. Try running manually: `python -m anglehelper.main`
  4. Check VS Code output panel for errors

**Issue: Qt platform errors**
- **Cause**: Display backend issues
- **Solution**:
  1. Try: `QT_QPA_PLATFORM=offscreen python -m anglehelper.main`
  2. Or: `QT_QPA_PLATFORM=wayland python -m anglehelper.main`
  3. Install missing Qt dependencies: `sudo apt install libxcb-xinerama0`

### VS Code Tips

- **Format code**: Shift+Alt+F (uses Black formatter)
- **Run tests**: Configured in launch.json
- **Linting**: Automatic with Flake8
- **Type checking**: Automatic with Pylance
- **Terminal**: Integrated terminal uses venv automatically

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [pytest Documentation](https://docs.pytest.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [VS Code Python Documentation](https://code.visualstudio.com/docs/python/python-tutorial)

Thank you for contributing to AngleHelper! 🚀