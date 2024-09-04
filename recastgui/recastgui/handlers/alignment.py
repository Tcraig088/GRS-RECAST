import os 
import numpy as np
import pandas as pd 
from recastgui.structs import enums, classes
from recastgui.functions import alignments as al

class Handler():
    def __init__(self, args):
        self.array = 3
        self.args = args
        self.gif = os.path.join(self.args.data.path,'stuff.gif')
        self.signals = len(self.args.data.signals)
        self.signalcount = 0
        df = self.args.data.signals
        self.alignto = df['align'].loc[lambda x: x==True].index
        self.projections = [None]*self.signals
        
    def Align(self, tiltseries, projection):
        for item, row in self.args.data.signals.iterrows():
            if row.identifier == projection.identifier:
                self.projections[item] = projection
            else:
                self.signalcount = self.signalcount+1
        if self.signalcount == self.signals:
            for item, row in self.args.alignments.alignments.iterrows():
                if row.name== enums.AlignmentType.CCTiltAlign.value:
                    ref =  np.zeros(np.size(self.projections[0].data))
                    idx = 0 
                    if row.reference == enums.ReferenceType.Angular.value:
                        idx = (np.abs(tiltseries.angle - self.projection[0].angle)).argmin()
                        ref = tiltseries.data[idx][:,:,self.alignto]
                    else:
                        idx = tiltseries.nproj-1
                        ref = tiltseries.data[idx][:,:,self.alignto]
                    self.projections[i]= al.Align(self.projection[self.alignto].data, ref)
                elif row.name== enums.AlignmentType.Centre.value:
                    print('Centre')
                    shift = al.Centre(self.projections[self.alignto].data)
                    for i in range(len(self.projections)):
                        self.projections[i] = np.roll(self.projections[i], np.array(shift, dtype=np.int32), (0, 1))
                    print(shift)
                elif row.name== enums.AlignmentType.Square.value:
                    for i in range(len(self.projections)):
                        self.projections[i] = al.Square(self.projections[i])
                elif row.name == enums.AlignmentType.Resize.value:
                    for i in range(len(self.projections)):
                        self.projections[i] = al.Resize(self.projections[i],row.dimx, row.dimy)
                elif row.name == enums.AlignmentType.BKGSubMedian.value:
                    for i in range(len(self.projections)):
                        self.projections[i] = al.Background_Subtract_Median(self.projections[i])
                elif row.name == enums.AlignmentType.SegOtsu.value:
                    for i in range(len(self.projections)):
                        self.projections[i] = al.OtsuSegment(self.projections[i])
                elif row.name == enums.AlignmentType.FilterGaussian.value:
                    for i in range(len(self.projections)):
                        self.projections[i] = al.GaussianFilter(self.projections[i], row.sigma)

            self.signalcount = 0
            size = np.shape(self.projections[0].data)
            img = np.zeros((size[0],size[1],self.signals))
            for i in range(self.signals):
                img[:,:,i]=self.projections[i].data
            if tiltseries.nproj == 0:
                tiltseries.angles = [self.projections[0].angle]
                tiltseries.data = [img]
                tiltseries.index = [0]
            else:
                tiltseries.angles.append(self.projections[0].angle)
                tiltseries.data.append(img)
                tiltseries.index.append(tiltseries.index[-1]+1)
            tiltseries.angles_rad = np.round(np.radians(tiltseries.angles),4)
            tiltseries.nproj = tiltseries.nproj+1
            return tiltseries
