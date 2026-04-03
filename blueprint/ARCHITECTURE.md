# Architecture Overview - Blueprint 2D Drawing Application

## System Architecture

Blueprint follows the **Model-View-Controller (MVC) pattern** with clear separation of concerns:

```
┌─────────────────────────────────────────────────┐
│                 USER INTERFACE                  │
│                 (Qt Widgets)                    │
└─────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│                 CONTROLLERS                     │
│                 (Business Logic)                │
└─────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│                   MODELS                        │
│                   (Data Layer)                  │
└─────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│                 FILE I/O & PERSISTENCE          │
│                 (JSON Serialization)             │
└─────────────────────────────────────────────────┘
```

## Core Components

### 1. Models Layer

**Location**: `models/`

**Responsibilities**:
- Business data representation
- Validation and business rules
- Serialization/deserialization
- State management

**Key Models**:

- **Line Model** (`models/line.py`)
  - Represents line segments with start/end points
  - Properties: color, width, length calculation
  - Immutable coordinates using tuples (x,y)
  - Serialization support for JSON

- **Drawing Model** (`models/drawing.py`)
  - Manages collection of Line objects
  - Grid settings (enabled/size)
  - Add/remove/clear operations
  - Complete serialization support

### 2. Views Layer

**Location**: `views/`

**Responsibilities**:
- User interface presentation
- User interaction handling
- Visual feedback
- Layout management

**Key Views**:

- **MainWindow** (`views/main_window.py`)
  - Application shell with menu bar
  - Layout management (toolbox + drawing area)
  - Menu actions and keyboard shortcuts
  - Central widget coordination

- **DrawingArea** (`views/drawing_area.py`)
  - QGraphicsView-based canvas
  - Grid rendering with dynamic resizing
  - Mouse event handling for drawing
  - Line visualization and interaction

- **Toolbox** (`views/toolbox.py`)
  - Tool selection interface
  - Current tool state management
  - Visual feedback for tool selection
  - Placeholder for future tools

### 3. Controllers Layer

**Location**: `controllers/`

**Responsibilities**:
- Business logic coordination
- Model-View mediation
- Application workflow
- Command processing

**Current Implementation**:
- Basic drawing controller for line operations
- Future expansion for complex operations

### 4. Utilities Layer

**Location**: `utils/`

**Responsibilities**:
- Cross-cutting concerns
- Common functionality
- File operations
- Helper functions

**Key Utilities**:

- **File I/O** (`utils/file_io.py`)
  - JSON serialization/deserialization
  - Qt file dialog integration
  - Error handling and user feedback
  - Tuple/list conversion for JSON compatibility
  - Automatic .json extension handling

- **Geometry** (`utils/geometry.py` - placeholder)
  - Future geometric calculations
  - Spatial algorithms
  - Collision detection

## Technical Design Decisions

### 1. MVC Architecture

**Rationale**: Clear separation of concerns improves maintainability and testability

**Benefits**:
- Models can be tested without UI
- Views can be modified without affecting business logic
- Controllers coordinate workflow cleanly
- Easy to extend with new features

### 2. JSON File Format

**Rationale**: Human-readable, easy to debug, widely supported

**Implementation**:
- Automatic tuple ↔ list conversion for JSON compatibility
- Pretty-printed output for readability
- Comprehensive error handling
- Versioning-ready structure

### 3. Qt Graphics Framework

**Rationale**: Mature, cross-platform GUI toolkit with excellent 2D graphics support

**Key Features Used**:
- QGraphicsView/QGraphicsScene for canvas
- QPen/QBrush for styling
- Mouse event handling
- Layout management
- Menu and action system

### 4. Type Hints and Documentation

**Rationale**: Improve code quality and developer experience

**Implementation**:
- Complete type annotations for public APIs
- Comprehensive docstrings for all classes/methods
- PEP 8 compliant formatting
- Black code formatter integration

## Data Flow

### Drawing Creation Flow

```
User Mouse Click
    ▼
DrawingArea.mousePressEvent()
    ▼
Create QGraphicsLineItem
    ▼
Update on mouse move
    ▼
DrawingArea.mouseReleaseEvent()
    ▼
Create Line model
    ▼
Add to Drawing model
    ▼
Persist to JSON (on save)
```

### File Loading Flow

```
User selects "Open"
    ▼
MainWindow._open_drawing()
    ▼
FileIO.load_drawing_from_file()
    ▼
Qt file dialog
    ▼
JSON deserialization
    ▼
Drawing.from_dict()
    ▼
DrawingArea._redraw_all()
    ▼
Render on canvas
```

## Testing Strategy

### Test Coverage

- **22 total tests** covering all core functionality
- **100% coverage** for models and file I/O
- **Mock testing** for GUI components

### Test Organization

- **Unit Tests**: Isolated testing of individual components
- **Serialization Tests**: Verify JSON round-trip accuracy
- **Edge Case Testing**: Default values, empty drawings, error conditions
- **Mock Objects**: Test file operations without GUI dependencies

### Test Files

- `test_line.py`: 8 tests for Line model functionality
- `test_drawing.py`: 8 tests for Drawing model operations
- `test_file_io.py`: 6 tests for file operations and error handling

## Performance Considerations

### Current Implementation

- **Grid Rendering**: Dynamic grid redrawing on resize events
- **Line Storage**: Simple list-based collection
- **File I/O**: Synchronous JSON operations
- **Memory Usage**: Minimal overhead for typical drawings

### Future Optimization Opportunities

- **Grid Caching**: Cache grid lines to reduce redraw overhead
- **Spatial Indexing**: Quadtree or R-tree for large drawings
- **Incremental Saving**: Track changes for efficient saves
- **Lazy Loading**: Load large drawings progressively

## Extensibility Points

### Designed for Future Expansion

1. **Additional Drawing Elements**
   - Rectangle, Circle, Arc tools
   - Custom shape support
   - Shape properties and styling

2. **Layer System**
   - Layer management interface
   - Layer visibility and ordering
   - Layer-based operations

3. **Advanced Features**
   - Measurement tools
   - Snap-to-grid/object
   - Zoom and pan
   - Undo/Redo system

4. **Export Formats**
   - DXF for CAD compatibility
   - SVG for web/vector use
   - PDF for documentation
   - Image export (PNG, JPEG)

## Error Handling Strategy

### User-Friendly Error Handling

- **File Operations**: Clear error messages with recovery options
- **Serialization**: Validation with helpful error messages
- **GUI Feedback**: Qt message boxes for critical errors
- **Graceful Degradation**: Fallback behaviors where possible

### Error Prevention

- **Type Hints**: Catch type errors early
- **Input Validation**: Validate data before processing
- **Defensive Programming**: Handle edge cases explicitly
- **Comprehensive Testing**: Catch issues before deployment

## Development Workflow

### Recommended Practices

1. **Feature Branches**: Develop features in isolated branches
2. **Test-Driven Development**: Write tests before implementation
3. **Code Reviews**: Maintain code quality through peer review
4. **Continuous Integration**: Automated testing on commits
5. **Documentation First**: Update docs with new features

### Build and Deployment

- **Dependencies**: Managed via requirements.txt
- **Packaging**: Standard Python package structure
- **Distribution**: Ready for PyPI packaging
- **Cross-Platform**: Tested on Linux, Windows, macOS

## Migration Path

### From Current State to Production

1. **Immediate Next Steps**
   - Implement undo/redo functionality
   - Add rectangle and circle tools
   - Enhance file management
   - Improve error recovery

2. **Mid-Term Goals**
   - Layer management system
   - Measurement tools
   - Export to DXF/SVG
   - Plugin architecture

3. **Long-Term Vision**
   - Professional CAD features
   - Collaboration support
   - Cloud synchronization
   - Mobile platform support

This architecture provides a solid foundation for building a professional-grade 2D drawing application while maintaining flexibility for future enhancements.