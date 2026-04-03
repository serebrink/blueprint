"""
Constants and configuration values for Blueprint application.

Centralizes magic numbers and configuration to improve maintainability.
"""

# Grid settings
DEFAULT_GRID_SIZE = 20
MIN_GRID_SIZE = 5
MAX_GRID_SIZE = 100

# Drawing defaults
DEFAULT_LINE_COLOR = "#000000"
DEFAULT_LINE_WIDTH = 2.0
DEFAULT_BACKGROUND_COLOR = "#FFFFFF"
GRID_LINE_COLOR = "#C8C8C8"
GRID_LINE_WIDTH = 1
GRID_LINE_STYLE = "dot"

# File settings
DEFAULT_FILE_EXTENSION = ".json"
FILE_FILTER_JSON = "JSON Files (*.json)"
FILE_FILTER_ALL = "All Files (*)"

# UI settings
TOOLBOX_WIDTH = 200
MIN_WINDOW_WIDTH = 800
MIN_WINDOW_HEIGHT = 600
DEFAULT_WINDOW_TITLE = "Blueprint - 2D Building Drawing"

# Drawing tools
TOOL_LINE = "line"
TOOL_RECTANGLE = "rectangle"
TOOL_CIRCLE = "circle"
TOOL_SELECT = "select"
TOOL_PAN = "pan"

# Application metadata
APP_NAME = "Blueprint"
APP_VERSION = "0.1.0"
APP_AUTHOR = "Johan Serebrink"
APP_DESCRIPTION = "2D Building Drawing Application"