"""
Drawing area widget for AngleHelper.

This widget provides the 2D drawing canvas where users can create building drawings.
"""

from PyQt5.QtWidgets import QWidget, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPen, QColor, QBrush, QPainter
from PyQt5.QtCore import Qt, QPointF
from models.drawing import Drawing
from models.line import Line
from utils.file_io import save_drawing_to_file, load_drawing_from_file
from utils.constants import (
    DEFAULT_GRID_SIZE,
    DEFAULT_LINE_COLOR,
    DEFAULT_LINE_WIDTH,
    DEFAULT_BACKGROUND_COLOR,
    GRID_LINE_COLOR,
    GRID_LINE_WIDTH
)


class DrawingArea(QGraphicsView):
    """Drawing area widget for creating 2D drawings.
    
    Attributes:
        scene: QGraphicsScene for managing drawing elements
        drawing: Current Drawing model
        grid_visible: Whether grid is visible
        grid_size: Size of grid cells
        current_line: Currently being drawn line (None if not drawing)
    """
    
    def __init__(self):
        """Initialize the drawing area."""
        super().__init__()
        
        # Set up graphics scene
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        # Set view properties
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setBackgroundBrush(QBrush(QColor(DEFAULT_BACKGROUND_COLOR)))
        
        # Initialize drawing
        self.drawing = Drawing("Untitled Drawing")
        self.grid_visible = True
        self.grid_size = DEFAULT_GRID_SIZE
        self.current_line = None
        
        # Set up mouse tracking
        self.setMouseTracking(True)
        
        # Draw grid if enabled
        if self.grid_visible:
            self._draw_grid()
    
    def _draw_grid(self):
        """Draw grid on the scene."""
        # Clear existing grid
        for item in self.scene.items():
            if hasattr(item, 'is_grid') and item.is_grid:
                self.scene.removeItem(item)
        
        if not self.grid_visible:
            return
        
        # Draw grid lines
        pen = QPen(QColor(GRID_LINE_COLOR), GRID_LINE_WIDTH, Qt.DotLine)
        
        # Get visible area
        visible_rect = self.mapToScene(self.viewport().rect()).boundingRect()
        
        # Draw vertical lines
        start_x = int(visible_rect.left()) - (int(visible_rect.left()) % self.grid_size)
        end_x = int(visible_rect.right()) + (self.grid_size - int(visible_rect.right()) % self.grid_size)
        
        for x in range(start_x, end_x + 1, self.grid_size):
            line = self.scene.addLine(x, visible_rect.top(), x, visible_rect.bottom(), pen)
            line.is_grid = True
        
        # Draw horizontal lines
        start_y = int(visible_rect.top()) - (int(visible_rect.top()) % self.grid_size)
        end_y = int(visible_rect.bottom()) + (self.grid_size - int(visible_rect.bottom()) % self.grid_size)
        
        for y in range(start_y, end_y + 1, self.grid_size):
            line = self.scene.addLine(visible_rect.left(), y, visible_rect.right(), y, pen)
            line.is_grid = True
    
    def resizeEvent(self, event):
        """Handle resize events to redraw grid."""
        super().resizeEvent(event)
        if self.grid_visible:
            self._draw_grid()
    
    def mousePressEvent(self, event):
        """Handle mouse press events for drawing."""
        if event.button() == Qt.LeftButton:
            # Start drawing a line
            scene_pos = self.mapToScene(event.pos())
            self.current_line = self.scene.addLine(
                scene_pos.x(), scene_pos.y(),
                scene_pos.x(), scene_pos.y(),
                QPen(QColor(DEFAULT_LINE_COLOR), DEFAULT_LINE_WIDTH)
            )
        
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events for drawing."""
        if self.current_line is not None:
            # Update line end point
            scene_pos = self.mapToScene(event.pos())
            self.current_line.setLine(
                self.current_line.line().x1(),
                self.current_line.line().y1(),
                scene_pos.x(),
                scene_pos.y()
            )
        
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events for drawing."""
        if event.button() == Qt.LeftButton and self.current_line is not None:
            # Finish drawing the line
            scene_pos = self.mapToScene(event.pos())
            
            # Add line to drawing model
            line = Line(
                start_point=(self.current_line.line().x1(), self.current_line.line().y1()),
                end_point=(scene_pos.x(), scene_pos.y()),
                color=DEFAULT_LINE_COLOR,
                width=DEFAULT_LINE_WIDTH
            )
            self.drawing.add_line(line)
            
            self.current_line = None
        
        super().mouseReleaseEvent(event)
    
    def new_drawing(self):
        """Create a new drawing."""
        self.drawing = Drawing("Untitled Drawing")
        self.scene.clear()
        if self.grid_visible:
            self._draw_grid()
    
    def open_drawing(self, parent):
        """Open a drawing from file."""
        drawing = load_drawing_from_file(parent)
        if drawing:
            self.drawing = drawing
            self._redraw_all()
    
    def save_drawing(self, parent):
        """Save the current drawing."""
        save_drawing_to_file(self.drawing, parent)
    
    def save_drawing_as(self, parent):
        """Save the current drawing with a new name."""
        # For now, just use regular save
        self.save_drawing(parent)
    
    def clear_drawing(self):
        """Clear the current drawing."""
        self.drawing.clear()
        self._redraw_all()
    
    def set_grid_visible(self, visible):
        """Set grid visibility."""
        self.grid_visible = visible
        self._draw_grid()
    
    def _redraw_all(self):
        """Redraw all elements from the drawing model."""
        self.scene.clear()
        
        # Draw all lines
        for line in self.drawing.lines:
            pen = QPen(QColor(line.color), line.width)
            scene_line = self.scene.addLine(
                line.start_point[0], line.start_point[1],
                line.end_point[0], line.end_point[1],
                pen
            )
            # Store reference to line model for potential future use
            scene_line.line_model = line
        
        # Draw grid if enabled
        if self.grid_visible:
            self._draw_grid()