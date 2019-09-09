import matplotlib.pyplot as plt

import math

from edge import EDGE

from node import NODE

class TREE:

    def __init__(self):

        self.root = NODE()

        r = 1.0

        theta = 0.0

        edge = EDGE( r , theta , self.root )

        self.root.Add(edge)

    def Count(self):

        print(self.root.Count())

    def Draw(self):

        fig = plt.figure()

        ax = fig.add_subplot(111)

        ax.set_xlim(-10,10)
        ax.set_ylim(-10,10)

        self.root.Draw()

        plt.show()

    def Grow(self,cppn):

        totalEdges = self.root.Count()

        self.root.Grow(totalEdges)
 
    def Print(self):

        self.root.Print()

        print('')

    def Update_Positions_Starting_At(self,rootX,rootY):

       self.root.Update_Positions(rootX,rootY,0.0)
