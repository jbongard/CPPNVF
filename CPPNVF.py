from cppn import CPPN

from tree import TREE

cppn = CPPN()

cppn.Draw()

exit()

tree = TREE()

for i in range(10):

    tree.Update_Positions_Starting_At(0,0)

    #tree.Print()
    #tree.Count()
    tree.Draw()

    tree.Grow(cppn)
