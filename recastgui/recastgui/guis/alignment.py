import tkinter as tk
import pandas as pd 

from recastgui.guis.table import TablePanel, LineEntryPanel
from recastgui.structs import enums

class AlignmentEntryPanel(LineEntryPanel):
    def __init__(self, parent, window, count):
        super().__init__(parent, window, count)
        self.parent = parent
        self.window = window
        self.index = count-1
                
        self.alignment_type = tk.StringVar()
        self.set_frame(100)
        
        self.set_lineentry_base()
        self.alignment_label = tk.Label(self.frame, text = "Signal:")
        self.alignment_menubutton = self.get_menu_button()

        for j in enums.AlignmentType:
            self.alignment_menubutton.menu.add_radiobutton(label=j.value, variable=self.alignment_type, value=j.value, command=self.select_data_type)
        self.alignment_menubutton['menu']=self.alignment_menubutton.menu


    """_summary_
    _memthod_: select_data_type
    _description_: This method sets the alignment type to the value of the alignment_type variable
    _arguments_: None
    _returns_: None
    """
    def select_data_type(self):
        self.alignment_menubutton['text']= self.alignment_type.get()

    """_summary_
    _method_: get_menu_button   
    _description_: This method creates a menubutton widget
    _arguments_: None
    _returns_: button: The menubutton widget
    """
    def get_menu_button(self):
        button = tk.Menubutton(self.frame, text="Choose File", relief='raised')
        button.grid()
        button.menu = tk.Menu(button,tearoff = 0)
        return button
    
    """_summary_
    _method_: update
    _description_: This method updates the alignment type variable
    _arguments_: args: A dictionary containing the alignment type
    _returns
    """
    def update(self, args):
        self.alignment_type.set(args['type'])
        self.select_data_type()


    """_summary_
    _method_: build
    _description_: This method builds the frame and widgets
    _arguments_: None
    _returns_: None
    """
    def build(self):
        super().build()        

        self.alignment_label.grid(row=0, column=1, sticky='W', padx=self.window.padx, pady=self.window.pady)
        self.alignment_menubutton.grid(row=0, column=2, sticky='W', padx=self.window.padx, pady=self.window.pady)
    
    """_summary_
    _method_: parse
    _description_: This method parses the alignment type variable
    _arguments_: None
    _returns_: args: A dictionary containing the alignment type
    """
    def parse(self, controller):
        return  controller.alignment_type.get()


class AlignmentPanel(TablePanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_frame(200, "Alignments")

        self.set_line_entry(AlignmentEntryPanel)
        self.set_table_base()
        
    """
    _summary_   
    update
    Description:
    Updates the alignment_entry.Panel objects with preset arguements
    Args:struct: a struct of arguements
    Returns:None
    """
    def update(self, args):
        for i in range(len(self.data)):
            self.data[i].remove_data()

        for i in range(len(args.alignments)):
            self.add_data()
            self.data[i].update(args.alignments[i])
            

    def build(self):
        """_summary_
        _Description_:
        Builds the alignment panel
        Args:None
        Returns:None
        """
        super().build()
        self.add_data()
        
    """_summary_
    parse
    Description:
    Parses the alignment panel and returns a struct of arguements
    Args:None
    Returns:dataframe of alignment types
    """ 
    def parse(self):
        align =[]
        for i in range(self.count):
            alignment = self.data[i].parse()
            align.append(alignment.alignment_type)
        alignments= pd.DataFrame(data={'type':align})
        return alignments   

