import constants as c

import copy

from cppn import CPPN

import matplotlib.pyplot as plt

from tree import TREE

cppns = {}

def Create_CPPNs():

    for panelIndex in range(1,c.numberOfCPPNs+1):

        cppns[panelIndex] = CPPN()

def Draw_CPPNs():

    fig = Prep_Drawing()

    for panelIndex in range(1,c.numberOfCPPNs+1):

        cppns[panelIndex].Draw(fig,panelIndex)

    plt.show()

def Mutate_CPPNs(choice):

    for panelIndex in range(1,c.numberOfCPPNs+1):

        if panelIndex != choice:

            cppns[panelIndex] = copy.deepcopy(cppns[choice])

            cppns[panelIndex].Mutate()

def Prep_Drawing():

    fig = plt.figure(figsize=(20,10))

    #ax = fig.add_subplot(339)

    #ax.set_xlim( c.vectorFieldMinimum - c.vectorFieldCellWidth  , c.vectorFieldMaximum + c.vectorFieldCellWidth)

    #ax.set_ylim( c.vectorFieldMinimum - c.vectorFieldCellHeight , c.vectorFieldMaximum + c.vectorFieldCellHeight)

    return fig

# -------------- Main function -------------------

Create_CPPNs()

Draw_CPPNs()

while True:

    choice = int( input('Which vector field to you like the best [1-'+str(c.numberOfCPPNs)+']: ') )

    Mutate_CPPNs(choice)

    Draw_CPPNs()

exit()

tree = TREE()

for i in range(10):

    tree.Update_Positions_Starting_At(0,0)

    #tree.Print()
    #tree.Count()
    tree.Draw()

    tree.Grow(cppn)
