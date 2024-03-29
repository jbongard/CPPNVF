import constants as c

import math

import numpy as np

from vectorField import VECTOR_FIELD

class CPPN: 

    def __init__(self):

        self.inputLayer   = np.zeros(c.cppnInputs,dtype='f')

        self.IHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnInputs,c.cppnHiddens] )

        self.hiddenLayer1 = np.zeros(c.cppnHiddens,dtype='f')

        self.activeLayer1 = {}

        for h in range(c.cppnHiddens):

            activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

            self.activeLayer1[h] = c.cppnActivationFunctions[activationFunctionType] 

        self.HHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnHiddens] )

        self.hiddenLayer2 = np.zeros(c.cppnHiddens,dtype='f')

        self.activeLayer2 = {}

        for h in range(c.cppnHiddens):

            activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

            self.activeLayer2[h] = c.cppnActivationFunctions[activationFunctionType]

        self.HOWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnOutputs] )

        self.outputLayer  = np.zeros(c.cppnOutputs,dtype='f')

    def Draw(self,fig,panelIndex):

        vectorField = VECTOR_FIELD()

        self.Paint(vectorField)

        vectorField.Draw(fig,panelIndex)

    def Mutate(self):

        if np.random.randint(2) == 0:

            self.Mutate_A_Weight()
        else:
            self.Mutate_An_Activation_Function()

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

        self.inputLayer[0] = x

        self.inputLayer[1] = y

        self.inputLayer[2] = np.sqrt( x**2 + y**2 ) # How far is the element from the center?

        self.inputLayer[3] = 1 # Bias neuron


        self.hiddenLayer1 = np.dot( self.inputLayer   , self.IHWeights )

        for h in range(c.cppnHiddens):

            self.hiddenLayer1[h] = self.activeLayer1[h]( self.hiddenLayer1[h] )


        self.hiddenLayer2 = np.dot( self.hiddenLayer1 , self.HHWeights )

        for h in range(c.cppnHiddens):

            self.hiddenLayer2[h] = self.activeLayer2[h]( self.hiddenLayer2[h] )


        self.outputLayer  = np.tanh( np.dot( self.hiddenLayer2 , self.HOWeights ) )


        return self.outputLayer 

    def Gaussian(self,x):

        return np.exp( -x**2 / 2.0 )

    def Mutate_A_Weight(self):

        mutateLayer = np.random.randint(3)

        if mutateLayer == 0:

            self.Mutate_A_Weight_In(self.IHWeights)

        elif mutateLayer == 1:

            self.Mutate_A_Weight_In(self.HHWeights)

        else:
            self.Mutate_A_Weight_In(self.HOWeights)

    def Mutate_A_Weight_In(self,W):

        cols, rows = W.shape

        col = np.random.randint(cols)
        row = np.random.randint(rows)

        W[col,row] = np.random.normal( loc = W[col,row] , scale = np.abs(W[col,row]) )

    def Mutate_An_Activation_Function(self):

        mutateLayer = np.random.randint(2)

        if mutateLayer == 0:

            self.Mutate_An_Activation_Function_In(self.activeLayer1)

        elif mutateLayer == 1:

            self.Mutate_An_Activation_Function_In(self.activeLayer2)

    def Mutate_An_Activation_Function_In(self,activeLayer):

        h = np.random.randint(c.cppnHiddens)

        activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

        activeLayer[h] = c.cppnActivationFunctions[activationFunctionType]

    def Paint(self,vectorField):

        for x in vectorField.Get_Xs():

            for y in vectorField.Get_Ys():

                outputs = self.Evaluate_At(x,y)

                vectorField.Set_Action_At(x,y,self.Get_Action_From_Outputs(outputs))

                vectorField.Set_DeltaX_At(x,y,self.Get_DeltaX_From_Outputs(outputs))

                vectorField.Set_DeltaY_At(x,y,self.Get_DeltaY_From_Outputs(outputs))
