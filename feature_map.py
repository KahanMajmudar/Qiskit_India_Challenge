# the write_and_run function writes the content in this cell into the file "feature_map.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap
import numpy as np
import time
import functools
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def feature_map(): 
    # BUILD FEATURE MAP HERE - START
    
    # import required qiskit libraries if additional libraries are required
    def custom_map(x):
        coeff = 0
        if len(x)==1:
            coeff = x[0]
        elif len(x)==3:
            coeff = functools.reduce(lambda l,m,n:1*m*n,np.pi - x)
        return coeff
    
    # build the feature map
    feature_map = None

    feature_map = PauliFeatureMap(feature_dimension=3,
                                reps=5,
                                entanglement="full",
                                paulis=['Z','ZZ'],
                                data_map_func=custom_map)
    
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map
