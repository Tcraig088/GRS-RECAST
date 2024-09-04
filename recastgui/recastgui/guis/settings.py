
import tkinter as tk
from tkinter import filedialog

from recastgui.guis.panel import Panel

class SettingsPanel(Panel):
    def __init__(self, parent):
        super().__init__(parent)
                
        # Tkinter Variables
        self.path = tk.StringVar()

        #Define Frame
        self.set_frame(200, "Load/Save Reconstruction Settings")
        
        self.file_label = tk.Label(self.frame, text = "Load/Save File (.pkl):") 
        self.file_entry = tk.Entry(self.frame,textvariable=self.path)
        self.file_button = tk.Button(self.frame, text="Browse",command=self.get_path)
        
        self.save_button = tk.Button(self.frame, text="Save",command=self.parent.save)
        self.load_button = tk.Button(self.frame, text="Load",command=self.parent.load)

    def get_path(self):
        self.path.set(filedialog.askopenfilename())
        
    def build(self):
        super().build()

        self.file_label.grid(row=0, column=0, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.file_entry.grid(row=0, column=1, columnspan=3, sticky='W'+'E', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.file_button.grid(row=0, column=4, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.save_button.grid(row=0, column=5, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.load_button.grid(row=0, column=6, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)

