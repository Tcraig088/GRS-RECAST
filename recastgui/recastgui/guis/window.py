import tkinter as tk
import os 
import sys

"""_class_: Window
_description_: This class is responsible for the window geometry and resizing.
_attributes_:
gui: The main tkinter window
height: int: The height of the window
width: int: The width of the window
"""
class Window():
    def __init__(self, parent):
        self.gui = parent.gui
        
        self.height =1000
        self.width = 500
        
        self.padx = 5
        self.pady = 5

        
        
