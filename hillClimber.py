import copy

import constants as c

from tree import TREE


class HILL_CLIMBER:

    def __init__(self):

        self.parent = TREE()

    def Play_Back_Best(self):

        self.parent.Simulate( play_blind = False )

    def Run(self):

        self.parent.Simulate( play_blind = True )
    
        self.parent.Compute_Fitness()

        for self.currentGeneration in range(0,c.numGenerations):

            self.Perform_One_Generation()

# ------------- Privat methods -------------

    def Child_More_Fit_Than_Parent(self):

        return self.child.Get_Fitness() > self.parent.Get_Fitness()

    def Perform_One_Generation(self):

        self.child = copy.deepcopy(self.parent)

        self.child.Mutate()

        self.child.Simulate( play_blind = True )

        self.child.Compute_Fitness()

        self.Print()

        if self.Child_More_Fit_Than_Parent():

            self.parent = self.child

    def Print(self):

        print(self.currentGeneration,self.parent.Get_Fitness(),self.child.Get_Fitness()) 
