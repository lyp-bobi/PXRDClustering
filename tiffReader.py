import numpy as np
import tifffile

global tiffShape
global center

tiffShape=[1679,1475]
center =[1413,725]

def inRange(x,y):
    global tiffShape

    if x<tiffShape[0] and x>=0 and y <tiffShape[1] and y>=0:
        return True
    else:
        return False

def tiffToFeature(s):
    img=tifffile.imread(s)
    feature=[]
    pt=center.copy()
    i=0
    while inRange(pt[0],pt[1]):
        feature.append(img[pt[0], pt[1]])
        if i%1==0:
            pt[0]-=1
        i=i+1
    pt = center.copy()
    i = 0
    while inRange(pt[0],pt[1]):
        feature.append(img[pt[0], pt[1]])
        if i%1==0:
            pt[0]-=1
        if i%2==0:
            pt[1]+=1
        i=i+1
    pt = center.copy()
    i = 0
    while inRange(pt[0],pt[1]):
        feature.append(img[pt[0], pt[1]])
        if i%1==0:
            pt[0]-=1
        if i%1==0:
            pt[1]+=1
        i=i+1
    for f in feature:
        if np.isnan(f):
            f=0
    # print(feature)
    feature=feature-np.percentile(feature,50)
    feature[feature<0]=0
    return feature
    # print(len(feature))

tiffToFeature("./sample.tif")