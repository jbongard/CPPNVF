import numpy as np

import math

# -------- Visualization -----------------

numberOfCPPNs          = 4 ** 2 

# --------------- Edges ------------------

maxEdges               = 100

edgeAngleChangeAmount  = math.pi / 20.0

edgeLengthChangeAmount = 0.1

numEdgeChangeActions   = 4

# ----------- Vector field ---------------

vectorFieldResolution  = 41 

vectorFieldMinimum     = -1.0

vectorFieldMaximum     = +1.0

vectorFieldWidth       = vectorFieldMaximum - vectorFieldMinimum

vectorFieldHeight      = vectorFieldWidth

vectorFieldCellWidth   = vectorFieldWidth / ( vectorFieldResolution - 1 )

vectorFieldCellHeight  = vectorFieldCellWidth

vectorFieldXDeltaMin   = -vectorFieldCellWidth  / 2

vectorFieldXDeltaMax   = +vectorFieldCellWidth  / 2

vectorFieldYDeltaMin   = -vectorFieldCellHeight / 2

vectorFieldYDeltaMax   = +vectorFieldCellHeight / 2

vectorFieldActionColors = {
0 : [0,0,0],
1 : [1,0,0],
2 : [0,1,0],
3 : [0,0,1]}

# ---------------- CPPN -----------------

cppnInputs = 4 # x , y , r and bias

cppnHiddens = numEdgeChangeActions + 2

cppnOutputs = numEdgeChangeActions + 2 

cppnInitialMinWeight = -1.0

cppnInitialMaxWeight = +1.0

cppnSinActFn = 0
cppnAbsActFn = 1
cppnGauActFn = 2
cppnTanActFn = 3
cppnNegActFn = 4
cppnIdnActFn = 5

def Gaussian(X):

    return np.exp( -X**2 / 2.0 )

def Negate(X):

    return -1 * X 

def Identity(X):

    return X

cppnActivationFunctions = {}

cppnActivationFunctions[cppnSinActFn] = np.sin

cppnActivationFunctions[cppnAbsActFn] = np.abs

cppnActivationFunctions[cppnGauActFn] = Gaussian

cppnActivationFunctions[cppnTanActFn] = np.tanh

cppnActivationFunctions[cppnNegActFn] = Negate

cppnActivationFunctions[cppnIdnActFn] = Identity

numCPPNActivationFunctions = len(cppnActivationFunctions)
