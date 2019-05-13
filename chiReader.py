import numpy as np

global tiffShape
global center



def chiToFeature(s):
    f = open(s, 'r')
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    feature=[]
    while True:
        line=f.readline()
        if not line:
            break
        cutted=line.split(" ")

        feature.append(float(cutted[3]))
    return feature

if __name__=="__main__":
    print(chiToFeature("D:\\PXRDAutoEncoder\\500C chi\\sample500C_tilt_15degree-06534.chi"))
