import constants as c

import numpy as np

from vectorField import VECTOR_FIELD

class CPPN: 

    def __init__(self):

        self.inputLayer = np.zeros(c.cppnInputs,dtype='f')

        self.IHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnInputs,c.cppnHiddens] )

        self.hiddenLayer = np.zeros(c.cppnHiddens,dtype='f')

        self.HOWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnOutputs] )

        self.outputLayer = np.zeros(c.cppnOutputs,dtype='f')

    def Draw(self):

        vectorField = VECTOR_FIELD()

        self.Paint(vectorField)

        vectorField.Draw()

    def Print(self):

        print(self.weights)

# ---------------- Private methods -----------

    def Get_Action_From_Outputs(self,outputs):

        minusOneToOne = outputs[0]

        zeroToTwo = minusOneToOne + 1

        zeroToOne = zeroToTwo / 2.0

        zeroToNumActionsMinusOne = zeroToOne * c.numEdgeChangeActions

        action = np.floor(zeroToNumActionsMinusOne) 

        return action 

    def Get_DeltaX_From_Outputs(self,outputs):

        minusOneToOne = outputs[1]

        minusDeltaXToDeltaX = minusOneToOne * c.vectorFieldXDeltaMax

        return minusDeltaXToDeltaX 

    def Get_DeltaY_From_Outputs(self,outputs):

        minusOneToOne = outputs[2]

        minusDeltaYToDeltaY = minusOneToOne * c.vectorFieldYDeltaMax

        return minusDeltaYToDeltaY

    def Evaluate_At(self,x,y):

        self.inputLayer[0] = x

        self.inputLayer[1] = y

        self.hiddenLayer = np.dot( self.inputLayer , self.IHWeights )

        self.hiddenLayer = np.tanh( self.hiddenLayer )

        self.outputLayer = np.dot( self.hiddenLayer , self.HOWeights )

        self.outputLayer = np.tanh( self.outputLayer )

        return self.outputLayer 

    def Paint(self,vectorField):

        for x in vectorField.Get_Xs():

            for y in vectorField.Get_Ys():

                outputs = self.Evaluate_At(x,y)

                vectorField.Set_Action_At(x,y,self.Get_Action_From_Outputs(outputs))

                vectorField.Set_DeltaX_At(x,y,self.Get_DeltaX_From_Outputs(outputs))

                vectorField.Set_DeltaY_At(x,y,self.Get_DeltaY_From_Outputs(outputs))
