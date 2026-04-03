"""
Main application window for AngleHelper.

This module contains the main window layout and menu setup.
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from .toolbox import Toolbox
from .drawing_area import DrawingArea
from utils.constants import (
    DEFAULT_WINDOW_TITLE,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,
    TOOLBOX_WIDTH
)


class MainWindow(QMainWindow):
    """Main application window.
    
    Contains the main layout with toolbox on the left and drawing area in the center.
    """
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        # Set window properties
        self.setWindowTitle(DEFAULT_WINDOW_TITLE)
        self.setMinimumSize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        
        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create toolbox (left side)
        self.toolbox = Toolbox()
        self.toolbox.setMaximumWidth(TOOLBOX_WIDTH)
        
        # Create drawing area (center)
        self.drawing_area = DrawingArea()
        
        # Add widgets to layout
        main_layout.addWidget(self.toolbox)
        main_layout.addWidget(self.drawing_area)
        
        # Set main widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Create menus
        self._create_menus()
    
    def _create_menus(self):
        """Create the application menu bar."""
        # Create menu bar
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        # Add file actions
        new_action = file_menu.addAction("&New")
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._new_drawing)
        
        open_action = file_menu.addAction("&Open...")
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self._open_drawing)
        
        save_action = file_menu.addAction("&Save")
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self._save_drawing)
        
        save_as_action = file_menu.addAction("Save &As...")
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self._save_drawing_as)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("E&xit")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        
        undo_action = edit_menu.addAction("&Undo")
        undo_action.setShortcut("Ctrl+Z")
        undo_action.setEnabled(False)  # Not implemented yet
        
        redo_action = edit_menu.addAction("&Redo")
        redo_action.setShortcut("Ctrl+Y")
        redo_action.setEnabled(False)  # Not implemented yet
        
        edit_menu.addSeparator()
        
        clear_action = edit_menu.addAction("&Clear All")
        clear_action.triggered.connect(self._clear_drawing)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        grid_action = view_menu.addAction("&Grid")
        grid_action.setCheckable(True)
        grid_action.setChecked(True)
        grid_action.triggered.connect(self._toggle_grid)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = help_menu.addAction("&About")
        about_action.triggered.connect(self._show_about)
    
    def _new_drawing(self):
        """Create a new drawing."""
        self.drawing_area.new_drawing()
    
    def _open_drawing(self):
        """Open a drawing from file."""
        self.drawing_area.open_drawing(self)
    
    def _save_drawing(self):
        """Save the current drawing."""
        self.drawing_area.save_drawing(self)
    
    def _save_drawing_as(self):
        """Save the current drawing with a new name."""
        self.drawing_area.save_drawing_as(self)
    
    def _clear_drawing(self):
        """Clear the current drawing."""
        self.drawing_area.clear_drawing()
    
    def _toggle_grid(self, checked):
        """Toggle grid visibility."""
        self.drawing_area.set_grid_visible(checked)
    
    def _show_about(self):
        """Show about dialog."""
        # TODO: Implement about dialog
        pass