import math

# --------------- Edges ------------------

maxEdges               = 100

edgeAngleChangeAmount  = math.pi / 20.0

edgeLengthChangeAmount = 0.1

numEdgeChangeActions   = 4

# ----------- Vector field ---------------

vectorFieldResolution  = 31 

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

cppnInputs = 2

cppnHiddens = 3 

cppnOutputs = numEdgeChangeActions + 2 

cppnInitialMinWeight = -1.0

cppnInitialMaxWeight = +1.0

