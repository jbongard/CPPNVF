import constants as c

import math

import matplotlib.pyplot as plt

import numpy as np

import random

class VECTOR_FIELD:

    def __init__(self):

        self.xs      = np.linspace(c.vectorFieldMinimum,c.vectorFieldMaximum,c.vectorFieldResolution)

        self.ys      = np.linspace(c.vectorFieldMinimum,c.vectorFieldMaximum,c.vectorFieldResolution)

        self.actions = {}

        self.deltaXs = {}

        self.deltaYs = {}

        for x in self.xs:

            for y in self.ys:

                self.Set_Action_At(x,y,0) 

                self.Set_DeltaX_At(x,y,0.0)

                self.Set_DeltaY_At(x,y,0.0) 

    def Draw(self,fig,panelIndex):

        ax = self.Prep_Drawing(fig,panelIndex)

        self.Draw_Vectors()

        self.Clean_Up_Drawing(ax)

    def Get_Xs(self):

        return self.xs

    def Get_Ys(self):

        return self.ys

    def Set_Action_At(self,x,y,action):

        self.actions[x,y] = action

    def Set_DeltaX_At(self,x,y,deltaX):

        self.deltaXs[x,y] = deltaX

    def Set_DeltaY_At(self,x,y,deltaY):

        self.deltaYs[x,y] = deltaY

# --------------------- Private methods ----------------------

    def Clean_Up_Drawing(self,ax):
       
        plt.xticks([])

        plt.yticks([])
 
        #ax.set_xticklabels([])

        #ax.set_yticklabels([])

    def Draw_Vectors(self):

        for x in self.xs:

            for y in self.ys:

                action = self.actions[x,y]

                deltaX = self.deltaXs[x,y]

                deltaY = self.deltaYs[x,y]

                plt.plot( [x,x + deltaX] , [y , y + deltaY] , color=c.vectorFieldActionColors[action])

                # plt.plot(x,y,'k.')

    def Paint_Randomly(self):

        for x,y in self.actions:

            self.Set_Action_At(x,y,np.random.randint(0,c.numEdgeChangeActions))

            self.Set_DeltaX_At(x,y,np.random.uniform(-c.vectorFieldXDeltaMin , +c.vectorFieldXDeltaMin))

            self.Set_DeltaY_At(x,y,np.random.uniform(-c.vectorFieldYDeltaMin , +c.vectorFieldYDeltaMin))

    def Prep_Drawing(self,fig,panelIndex):

        # fig = plt.figure()

        ax = fig.add_subplot( math.sqrt(c.numberOfCPPNs) , math.sqrt(c.numberOfCPPNs) , panelIndex )

        plt.title(str(panelIndex))

        ax.set_xlim( c.vectorFieldMinimum - c.vectorFieldCellWidth  , c.vectorFieldMaximum + c.vectorFieldCellWidth)

        ax.set_ylim( c.vectorFieldMinimum - c.vectorFieldCellHeight , c.vectorFieldMaximum + c.vectorFieldCellHeight)

        return ax
