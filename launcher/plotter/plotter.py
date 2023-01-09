import pandas as pd 

import matplotlib.pyplot as plt
import multiprocessing as mp
import time
import matplotlib
import numpy as np
import slicerecon
import copy
import sklearn.preprocessing as pp

class ProcessPlotter:
    def __init__(self):
        self.x = []
        self.y1 = []
        self.y2= []
    def terminate(self):
        plt.close('all')

    def call_back(self):
        while self.pipe.poll():
            command = self.pipe.recv()
            if command is None:
                self.terminate()
                return False
            else:
                time.sleep(0.1)
                if len(self.x)!=0 and command[0]<self.x[-1]:
                    self.x = []
                    self.y1 = []
                    self.y2= []
                self.x.append(command[0])
                self.y1.append(command[1])
                self.y2.append(command[2])
                self.ax[0,0].plot(self.x, self.y1)
                self.ax[0,1].plot(self.x, self.y2)
                self.ax[1,0].imshow(command[3])
                self.ax[1,1].imshow(command[4])
                self.ax[1,2].imshow(command[5])
                self.ax[2,0].imshow(command[6])
                self.ax[2,1].imshow(command[7])
                self.ax[2,2].imshow(command[8])
                
                self.fig.suptitle(str(command[0])+ ' Projections')
        self.fig.canvas.draw()
        return True
        
    def __call__(self, pipe):
        print('starting plotter...')

        self.pipe = pipe
        self.fig, self.ax = plt.subplots(3,3)
        timer = self.fig.canvas.new_timer(interval=1000)
        timer.add_callback(self.call_back)
        timer.start()

        print('...done')
        plt.show()
        

