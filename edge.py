import copy

import matplotlib.pyplot as plt

import math

from node import NODE

class EDGE:
  
    def __init__(self, r , theta , nodeAtBase ):

        self.nodeAtBase = nodeAtBase 

        self.r     = r 

        self.theta = theta

        self.nodeAtTip = NODE()

    def Add_New_Edge(self):

        newEdge = EDGE( self.r , 0.0 , self.nodeAtTip )

        self.nodeAtTip.Add(newEdge)

    def Draw(self,baseX,baseY):

        tipX = self.nodeAtTip.Get_X()

        tipY = self.nodeAtTip.Get_Y()
       
        plt.plot([baseX,tipX],[baseY,tipY])

        self.nodeAtTip.Draw()

    def Change_Angle_By(self,deltaTheta):

        self.theta = self.theta + deltaTheta

    def Change_Length_By(self,deltaR):

        self.r = self.r + deltaR

    def Count(self):

        return 1 + self.nodeAtTip.Count() 

    def Grow(self,totalEdges):

        return self.nodeAtTip.Grow(totalEdges)

    def Print(self):

        print('edge: ',self.r,self.theta)

        self.nodeAtTip.Print()

    def Split(self):

        newEdge = EDGE( self.r , self.theta + math.pi/20.0 , self.nodeAtBase )

        self.nodeAtBase.Add(newEdge)
 
    def Update_Positions(self,x,y,previousTheta):

        xTip = x + self.r * math.sin( previousTheta + self.theta )

        yTip = y + self.r * math.cos( previousTheta + self.theta )

        self.nodeAtTip.Update_Positions(xTip,yTip,self.theta)
