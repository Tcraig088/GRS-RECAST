import tkinter as tk
from recastgui.guis.panel import Panel

"""
    Class Panel
    This is the base class for the submit button panels. It is responsible for the controls of the interface. 
    
    Attributes:
"""
class SubmitPanel(Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_frame(100)
        
        self.submit_button = tk.Button(self.frame, text ="Submit")
        self.reset_button = tk.Button(self.frame, text ="Reset")
        
    def build(self):
        super().build()

        self.submit_button.grid(row=0, column=0, sticky = 'W', padx = self.parent.window.padx, pady = self.parent.window.pady)
        self.reset_button.grid(row=0, column=1, sticky = 'W', padx = self.parent.window.padx, pady = self.parent.window.pady)
