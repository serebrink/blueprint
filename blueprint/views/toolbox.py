"""
Toolbox widget for AngleHelper.

Contains drawing tools and options.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGroupBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Toolbox(QWidget):
    """Toolbox widget containing drawing tools.
    
    Attributes:
        tool_selected: Signal emitted when a tool is selected
    """
    
    def __init__(self):
        """Initialize the toolbox."""
        super().__init__()
        
        # Set up layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignTop)
        
        # Add title
        title = QLabel("<h3>Tools</h3>")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Create drawing tools group
        drawing_tools_group = QGroupBox("Drawing Tools")
        drawing_tools_layout = QVBoxLayout()
        
        # Line tool button
        self.line_tool_button = QPushButton("Line Tool")
        self.line_tool_button.setCheckable(True)
        self.line_tool_button.setChecked(True)
        self.line_tool_button.setToolTip("Draw lines between points")
        self.line_tool_button.clicked.connect(self._on_line_tool_clicked)
        drawing_tools_layout.addWidget(self.line_tool_button)
        
        # Rectangle tool button (for future use)
        self.rectangle_tool_button = QPushButton("Rectangle Tool")
        self.rectangle_tool_button.setCheckable(True)
        self.rectangle_tool_button.setEnabled(False)  # Not implemented yet
        self.rectangle_tool_button.setToolTip("Draw rectangles (not yet implemented)")
        drawing_tools_layout.addWidget(self.rectangle_tool_button)
        
        # Circle tool button (for future use)
        self.circle_tool_button = QPushButton("Circle Tool")
        self.circle_tool_button.setCheckable(True)
        self.circle_tool_button.setEnabled(False)  # Not implemented yet
        self.circle_tool_button.setToolTip("Draw circles (not yet implemented)")
        drawing_tools_layout.addWidget(self.circle_tool_button)
        
        drawing_tools_group.setLayout(drawing_tools_layout)
        layout.addWidget(drawing_tools_group)
        
        # Create options group
        options_group = QGroupBox("Options")
        options_layout = QVBoxLayout()
        
        # Line color button (placeholder)
        color_button = QPushButton("Line Color")
        color_button.setEnabled(False)  # Not implemented yet
        options_layout.addWidget(color_button)
        
        # Line width button (placeholder)
        width_button = QPushButton("Line Width")
        width_button.setEnabled(False)  # Not implemented yet
        options_layout.addWidget(width_button)
        
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        
        # Add stretch to push content to top
        layout.addStretch()
        
        self.setLayout(layout)
    
    def _on_line_tool_clicked(self, checked):
        """Handle line tool button click."""
        if checked:
            # Line tool selected
            self.rectangle_tool_button.setChecked(False)
            self.circle_tool_button.setChecked(False)
            # TODO: Emit signal to drawing area
    
    def get_current_tool(self):
        """Get the currently selected tool.
        
        Returns:
            String representing the current tool ('line', 'rectangle', 'circle')
        """
        if self.line_tool_button.isChecked():
            return 'line'
        elif self.rectangle_tool_button.isChecked():
            return 'rectangle'
        elif self.circle_tool_button.isChecked():
            return 'circle'
        else:
            return 'line'  # Default to line tool