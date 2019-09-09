import constants as c

import math, random

class NODE:

    def __init__(self):

        self.x = 0.0

        self.y = 0.0

        self.edgeIndex2Edge = {}

    def Add(self,edge):

        numOutgoingEdges = len(self.edgeIndex2Edge)

        self.edgeIndex2Edge[numOutgoingEdges] = edge

    def Grow(self,totalEdges):

        numEdges = len(self.edgeIndex2Edge)

        for edgeIndex in range(numEdges):

            changeType = random.random()

            if changeType < 0.25:

                if totalEdges < c.maxEdges:

                    self.edgeIndex2Edge[edgeIndex].Split()

                    totalEdges = totalEdges + 1

            elif changeType < 0.5:

                if totalEdges < c.maxEdges: 

                    self.edgeIndex2Edge[edgeIndex].Add_New_Edge()

                    totalEdges = totalEdges + 1

            elif changeType < 0.75:

                self.edgeIndex2Edge[edgeIndex].Change_Length_By(0.1)
 
            else:
                self.edgeIndex2Edge[edgeIndex].Change_Angle_By(math.pi/20.0)

            totalEdges = self.edgeIndex2Edge[edgeIndex].Grow(totalEdges)

        return totalEdges

    def Count(self):

        numEdges = 0 

        for edgeIndex in self.edgeIndex2Edge:

            numEdges = numEdges + self.edgeIndex2Edge[edgeIndex].Count()

        return numEdges

    def Draw(self):

        for edgeIndex in self.edgeIndex2Edge:

            self.edgeIndex2Edge[edgeIndex].Draw(self.x,self.y)

    def Get_X(self):

        return self.x

    def Get_Y(self):

        return self.y

    def Print(self):

        print('node: ',self.x,self.y)

        for edgeIndex in self.edgeIndex2Edge:

            self.edgeIndex2Edge[edgeIndex].Print()

    def Update_Positions(self,x,y,previousTheta):

        self.x = x

        self.y = y

        for edgeIndex in self.edgeIndex2Edge:

            self.edgeIndex2Edge[edgeIndex].Update_Positions(self.x,self.y,previousTheta)
