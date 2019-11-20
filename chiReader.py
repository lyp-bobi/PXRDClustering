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

def chiToPeak(s):
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
    feature=feature-np.percentile(feature,80)#这个80可以改，不一定和那边那个一样
    feature[feature<0]=0
    # print(feature)
    return feature

if __name__=="__main__":
    print(chiToFeature("D:\\PXRDAutoEncoder\\500C chi\\sample500C_tilt_15degree-06534.chi"))
