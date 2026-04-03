"""
Main entry point for Blueprint application.

This module contains the main application entry point and initializes the GUI.
"""

import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow


def main():
    """Main application entry point."""
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("Blueprint")
    app.setOrganizationName("Serebrink AB")
    app.setApplicationVersion("0.1.0")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start application event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()