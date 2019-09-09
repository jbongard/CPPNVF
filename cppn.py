import numpy as np

class CPPN: 

    def __init__(self):

        self.inputLayer = np.zeros(2,dtype='f')

        self.synapses = np.zeros((2,2),dtype='f')

        self.outputLayer = np.zeros(2,dtype='f')

    def Print(self):

        print(self.inputLayer)

        print(self.synapses)

        print(self.outputLayer)
