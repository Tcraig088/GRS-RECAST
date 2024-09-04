import tkinter as tk
from tkinter import filedialog

from recastgui.guis.panel import Panel
from recastgui.structs import enums

class DataPanel(Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_frame(200, "Data")
        
        self.path = tk.StringVar()
        self.id = tk.StringVar()
        self.filetype = tk.StringVar()
        
        self.folder_label = tk.Label(self.frame, text = "Folder:") 
        self.folder_entry = tk.Entry(self.frame,textvariable=self.path)
        self.folder_button = tk.Button(self.frame, text="Browse",command=self.get_data_path)
        
        self.id_label = tk.Label(self.frame, text = "Identifier:")
        self.id_entry = tk.Entry(self.frame,textvariable=self.id)
        self.type_label = tk.Label(self.frame, text = "Data Type:")
        self.type_menubutton = self.get_menu_button()
        
        for j in enums.ProjectionType:
            self.type_menubutton.menu.add_radiobutton(label=j.value, variable=self.filetype, value=j.value, command=self.select_data_type)
        self.type_menubutton['menu']=self.type_menubutton.menu

    def build(self):
        super().build()

        self.folder_label.grid(row=0, column=0, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.folder_entry.grid(row=0, column=1, columnspan=3, sticky='W'+'E', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.folder_button.grid(row=0, column=4, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)

        self.id_label.grid(row=1, column=0, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.id_entry.grid(row=1, column=1, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.type_label.grid(row=1, column=2, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        self.type_menubutton.grid(row=1, column=3, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)
        
    def get_data_path(self):
        self.path.set(filedialog.askdirectory())

    #TODO: Fix   
    def update(self, args):
        pass
    
    #TODO: Fix
    def parse(self):
        self.args = self.Args(self)
        return self.args

    def select_data_type(self):
        self.type_menubutton['text']= self.filetype.get()

    def get_menu_button(self):
        button = tk.Menubutton(self.frame, text="Choose File", relief='raised')
        button.grid()
        button.menu = tk.Menu(button,tearoff = 0)
        return button
 

