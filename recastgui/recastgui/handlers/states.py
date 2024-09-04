"""
class StateHandler
This class is responsible for handling the state of application threads. Just to ensure files open and close correctly.
Attributes:
state_running: boolean - The state of the application
state_active_threads: int - The number of active threads
"""
class StateHandler():
    def __init__(self):
        self.state_running = False
        self.state_active_threads = 0

    def handle(self, event):
        pass