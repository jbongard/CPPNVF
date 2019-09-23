import constants as c

import numpy as np

from vectorField import VECTOR_FIELD

class CPPN: 

    def __init__(self):

        self.inputLayer   = np.zeros(c.cppnInputs,dtype='f')

        self.IHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnInputs,c.cppnHiddens] )

        self.hiddenLayer1 = np.zeros(c.cppnHiddens,dtype='f')

        self.hiddenLayer1SinMask = np.random.randint(2, size=c.cppnHiddens) 

        self.hiddenLayer1AbsMask = np.random.randint(2, size=c.cppnHiddens)

        self.hiddenLayer1TanMask = np.random.randint(2, size=c.cppnHiddens)

        self.hiddenLayer1NegMask = np.random.randint(2, size=c.cppnHiddens) 

        self.HHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnHiddens] )

        self.hiddenLayer2 = np.zeros(c.cppnHiddens,dtype='f')

        self.hiddenLayer2SinMask = np.random.randint(2, size=c.cppnHiddens)

        self.hiddenLayer2TanMask = np.random.randint(2, size=c.cppnHiddens)

        self.hiddenLayer2NegMask = np.random.randint(2, size=c.cppnHiddens)

        self.HOWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnOutputs] )

        self.outputLayer  = np.zeros(c.cppnOutputs,dtype='f')

    def Draw(self):

        vectorField = VECTOR_FIELD()

        self.Paint(vectorField)

        vectorField.Draw()

    def Print(self):

        print(self.weights)

# ---------------- Private methods -----------

    def Get_Action_From_Outputs(self,outputs):

        possibleActions = outputs[ 0 : c.numEdgeChangeActions ]

        action = np.argmax( possibleActions )

        return action 

    def Get_DeltaX_From_Outputs(self,outputs):

        # return outputs[c.numEdgeChangeActions]

        minusOneToOne = outputs[c.numEdgeChangeActions]

        minusDeltaXToDeltaX = minusOneToOne * c.vectorFieldXDeltaMax

        return minusDeltaXToDeltaX 

    def Get_DeltaY_From_Outputs(self,outputs):

        # return outputs[c.numEdgeChangeActions+1]

        minusOneToOne = outputs[c.numEdgeChangeActions+1]

        minusDeltaYToDeltaY = minusOneToOne * c.vectorFieldYDeltaMax

        return minusDeltaYToDeltaY

    def Evaluate_At(self,x,y):

        self.inputLayer[0] = 0 # x

        self.inputLayer[1] = 0 # y

        self.inputLayer[2] = np.sqrt( x**2 + y**2 )


        self.hiddenLayer1 = np.dot( self.inputLayer   , self.IHWeights )

        self.hiddenLayer1 = self.hiddenLayer1 + np.multiply( self.hiddenLayer1SinMask , np.sin(self.hiddenLayer1) )

        self.hiddenLayer1 = self.hiddenLayer1 + np.multiply( self.hiddenLayer1AbsMask , np.abs(self.hiddenLayer1) )

        self.hiddenLayer1 = self.hiddenLayer1 + np.multiply( self.hiddenLayer1TanMask , np.tanh(self.hiddenLayer1) )

        self.hiddenLayer1 = self.hiddenLayer1 + np.multiply( self.hiddenLayer1NegMask , -1 * self.hiddenLayer1 )


        self.hiddenLayer2 = np.dot( self.hiddenLayer1 , self.HHWeights )

        self.hiddenLayer2 = self.hiddenLayer2 + np.multiply( self.hiddenLayer2SinMask , np.sin(self.hiddenLayer2) )

        self.hiddenLayer2 = self.hiddenLayer2 + np.multiply( self.hiddenLayer2TanMask , np.tanh(self.hiddenLayer2) )

        self.hiddenLayer2 = self.hiddenLayer2 + np.multiply( self.hiddenLayer2NegMask , -1 * self.hiddenLayer2 )


        self.outputLayer  = np.tanh( np.dot( self.hiddenLayer2 , self.HOWeights ) )


        return self.outputLayer 

    def Gaussian(self,x):

        return np.exp( -x**2 / 2.0 )

    def Paint(self,vectorField):

        for x in vectorField.Get_Xs():

            for y in vectorField.Get_Ys():

                outputs = self.Evaluate_At(x,y)

                vectorField.Set_Action_At(x,y,self.Get_Action_From_Outputs(outputs))

                vectorField.Set_DeltaX_At(x,y,self.Get_DeltaX_From_Outputs(outputs))

                vectorField.Set_DeltaY_At(x,y,self.Get_DeltaY_From_Outputs(outputs))
