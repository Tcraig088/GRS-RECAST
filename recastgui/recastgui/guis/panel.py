import tkinter as tk

"""
window: The tkinter window object

_methods_:
build: Builds the panel
set_frame: Sets the frame of the panel
"""
class Panel():
    def __init__(self, parent):
        self.parent = parent
        self.gui = parent.gui
        self.window = parent.window
        self.frame = None  # Initialize self.frame

    """
    _method_: build
    _description_: Builds the panel
    _args_: None
    _returns_: None
    """
    def build(self):
        if self.frame is not None:
            self.frame.grid(sticky='ew', padx=self.window.padx, pady=self.window.pady)
            #self.frame.pack(fill='x', expand=True)
        else:
            raise ValueError("Frame is not set. Call set_frame first.")

    """_method_: set_frame
    _description_: Sets the frame of the panel
    _args_: 
    height: int: The height of the frame
    text: str: The text of the frame
    _returns_: None
    """
    def set_frame(self, height, text=None, width=None):
        if width is None:
            width = self.window.width

        if text is None:
            self.frame = tk.LabelFrame(self.gui, 
                borderwidth=self.window.padx,
                height=height,
                width=width)
        else:
            self.frame = tk.LabelFrame(self.gui, 
                borderwidth=self.window.padx,
                height=height,
                width=width,
                text=text)