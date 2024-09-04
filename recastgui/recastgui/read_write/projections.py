import pandas as pd 
import numpy as np
import hyperspy.api as hp 
import os 
#Image Processing 
from PIL import Image
#import ser_parser
import csv

data_types = ['emi/ser','tiff']

def ReadProjection(filename, filetype):
    if filetype not in data_types:
        raise ValueError('Filetype not supported')
    elif filetype == 'emi/ser':
        (m, n), proj = ser_parser.parser(filename)
        return np.reshape(proj, (m,n))
    elif filetype == 'tiff':
        return np.array(Image.open(filename))
        
class ProjectionHandler():
    def __init__(self):
        self.sernum = 1
       
    def GetID(self, name, filetype):
        identifier = ''
        if filetype not in data_types:
            raise ValueError('Filetype not supported')
        elif filetype == 'emi/ser':
            identifier = '_'+str(self.sernum)+'.ser'
            self.sernum = self.sernum + 1
        elif filetype == 'tiff':
            identifier = name
        return identifier

