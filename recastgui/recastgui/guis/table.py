import tkinter as tk 
from recastgui.guis.panel import Panel


class LineEntryPanel(Panel):
    def __init__(self, parent, window, count):
        super().__init__(parent)
        self.window = window
        self.index = count-1

    def set_lineentry_base(self):
        if self.frame is not None:
            self.remove_button = tk.Button(self.frame, text="Remove", command=self.remove_data)
            
    def remove_data(self):
        self.frame.grid_forget()
        self.parent.remove_data(self.index)

    def build(self):
        super().build()
        print('build')
        self.remove_button.grid(row=0, column=0, sticky='W', padx=self.window.padx, pady=self.window.pady)
        
class TablePanel(Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = []
        self.count = 0
        
    def set_table_base(self):
        if self.frame is not None:
            self.add_button = tk.Button(self.frame, text ="Add", command = self.add_data)
        else:
            raise ValueError("Frame is not set. Call set_frame first.")
        
    def set_line_entry(self, line_entry):
        #line_entry should be a class that inherits from LineEntryPanel
        self.line_entry = line_entry
        
    def add_data(self):
        self.count = self.count + 1
        self.data.append(self.line_entry(self, self.parent.window, self.count))
        self.data[-1].build()
        
    def remove_data(self, row):
        del self.data[row]
        self.count = self.count -1
        for i in range(row,self.count):
            self.data[i].index=self.data[i].index-1
            
    def build(self):
        if self.frame is not None:
            super().build()
            self.add_button.grid(row=0, column=0, sticky='W', padx=self.parent.window.padx, pady=self.parent.window.pady)


  