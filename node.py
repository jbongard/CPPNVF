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

            totalEdges = self.Change_Edge(edgeIndex,totalEdges)

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

# ------------------- Private methods ----------------------

    def Add_Imminent(self,changeType):

        return changeType < 0.5

    def Attempt_Add(self,edgeIndex,totalEdges):

        if totalEdges < c.maxEdges:

            self.edgeIndex2Edge[edgeIndex].Add_New_Edge()

            return totalEdges + 1

        return totalEdges

    def Attempt_Split(self,edgeIndex,totalEdges):

        if totalEdges < c.maxEdges:

            self.edgeIndex2Edge[edgeIndex].Split()

            return totalEdges + 1

        return totalEdges

    def Change_Angle(self,edgeIndex):

        if random.random() < 0.5:

            self.edgeIndex2Edge[edgeIndex].Change_Angle_By(+c.edgeAngleChangeAmount)
        else:
            self.edgeIndex2Edge[edgeIndex].Change_Angle_By(-c.edgeAngleChangeAmount)

    def Change_Edge(self,edgeIndex,totalEdges):

        changeType = random.random()

        if self.Split_Imminent(changeType):

            totalEdges = self.Attempt_Split(edgeIndex,totalEdges)

        elif self.Add_Imminent(changeType):

            totalEdges = self.Attempt_Add(edgeIndex,totalEdges)

        elif self.Change_Length_Imminent(changeType):

            self.Change_Length(edgeIndex)

        else:

            self.Change_Angle(edgeIndex)

        return totalEdges

    def Change_Length(self,edgeIndex):

       self.edgeIndex2Edge[edgeIndex].Change_Length_By(c.edgeLengthChangeAmount)

    def Change_Length_Imminent(self,changeType):

        return changeType < 0.75

    def Split_Imminent(self,changeType):

        return changeType < 0.25
