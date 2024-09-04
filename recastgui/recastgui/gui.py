import tkinter as tk
import time
import pickle

from threading import Thread
from recastgui.guis import *
from recastgui.handlers import StateHandler, ProjectionHandler, PluginHandler

"""
RECAST Launcher

This is the main class for the RECAST Launcher. It is responsible for creating the GUI and managing the various panels.
Inherits from StateHandler, AcquistionHandler, PluginHandler

Attributes:
gui: The main tkinter window
window: The main window object

settings_frame: The settings panel
data_frame: The data panel
acquisition_frame: The acquisition panel
alignments_frame: The alignments panel
submit_frame: The submit panel
frames: A list of all the panels

Methods:
start: Starts the GUI
end: Ends the GUI and kills processes
build: Builds the GUI

"""
class RECASTLauncher(StateHandler, ProjectionHandler, PluginHandler):
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.title('RECAST Launcher')
        self.window = Window(self)  
         
        self.settings_frame = SettingsPanel(self)
        self.data_frame = DataPanel(self)
        self.alignments_frame = AlignmentPanel(self)
        self.submit_frame = SubmitPanel(self)
        
        self.frames = [self.settings_frame, self.data_frame, self.alignments_frame, self.submit_frame]
        
        self.settings_frame.save_button.config(command = self.save)
        self.settings_frame.load_button.config(command = self.load)
        self.submit_frame.submit_button.config(command = self.exec)
        
        self.build()
    """
    start
    This method starts the GUI.
    Args:None
    Returns:None
    """  
    def start(self):
        self.gui.mainloop()
    
    """
    end
    This method ends the GUI.
    Args:None
    Returns:None
    """   
    def end(self):
        self.state_running = False
        while self.state_active_threads > 0:
            time.sleep(1)
        self.gui.destroy()
    
    
    """_summary_
    build
    This method builds the GUI.
    Args:None
    Returns:None
    """
    def build(self):
        for frames in self.frames:
            frames.build()       
    
    """_summary_
    exec
    This method executes the program.
    Args:None
    Returns:None
    """
    def exec(self):
        self.parse()
        self.state_running = True
        
        self.start_acquisition()
        self.start_plugin()
    
    
    """
    parse
    This method parses the arguments.
    Args:None
    Returns:
    args: Dictionary of arguments
    """
    def parse(self):
        args = {}
        for frame in self.frames:
            key, value = frame.parse()
            args[key] = value
            
        return args

    """
    save
    This method saves the settings tp a pickle file.
    Args:None
    Returns:None
    """
    def save(self):
        with open(self.settings_frame.path.get(), 'wb') as f:
            self.parse()
            pickle.dump(self.args, f)

    """_summary_
    load
    This method loads the settings from a pickle file.
    Args:None
    Returns:None
    """
    def load(self):
        with open(self.settings_frame.path.get(), 'rb') as f:
            args = pickle.load(f)
        
        self.data_frame.update(args.data)
        self.acquisition_frame.update(args.acquisition)
        self.alignments_frame.update(args.alignments)

        


