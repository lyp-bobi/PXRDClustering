import numpy as np
import tifffile
from mpl_toolkits.mplot3d import Axes3D
global tiffShape
global center

import matplotlib.pyplot as plt
import scipy.signal
import math

global tiffShape
global center

tiffShape=[1679,1475]
center =[1413,721]
maxdist=1700

def pixelsNum(dist):
    angle=2*math.pi
    place=center[1]
    if(place<dist):
        angle-=2*math.acos(place/dist)
    place=tiffShape[1]-center[1]
    if (place < dist):
        angle -= 2*math.acos(place / dist)
    place=tiffShape[0]-center[0]
    if (place < dist):
        angle -= 2*math.acos(place / dist)
    return round(angle*dist)



# np.set_printoptions(threshold=1e9)
def tiffToFeature(s):
    global tiffShape
    global center
    if(tiffShape==[] or center==[]):
        centerEsimate(s)
    img=tifffile.imread(s)
    px=0
    py=center[1]
    sum=np.zeros(maxdist+1)
    count=np.zeros(maxdist+1)
    for j in range(5):
        py=round(center[1]+(tiffShape[1]-center[1])*j/6)
        for i in range(tiffShape[0]):
            px = i
            if img[px,py]>10:
                dist = round(math.sqrt(pow(px - center[0], 2) + pow(py - center[1], 2)))
                sum[dist]+=img[px,py]
                count[dist]+=1

    feature=list(map(lambda x,y:0 if y==0 else x/y,sum,count))
    polethres=10000
    pole=np.where(img>polethres)
    for i in range(len(pole[0])):
        px=pole[0][i]
        py=pole[1][i]
        dist=math.sqrt(pow(px-center[0],2)+pow(py-center[1],2))
        feature[round(dist)]+=img[px,py]/pixelsNum(dist)
        # print(feature[round(dist)])

    # # peakmask
    # thres=np.max(feature)/10
    # peaks = scipy.signal.find_peaks(feature, width=0, prominence=thres)
    # npeaks = len(peaks[0])
    # mask = np.zeros([len(feature)])
    # for i in range(npeaks):
    #     lp = int(peaks[1]['left_ips'][i])
    #     rp = int(peaks[1]['right_ips'][i]) + 1
    #     # peakmin = feature[lp]
    #     for j in range(lp, rp):
    #         # peakmin = min(peakmin, feature[j])
    #         mask[j] = 1
    #     # for j in range(lp, rp):
    #         # feature[j] -= peakmin
    # feature = feature * mask
    # # \peakmask

    return feature



def centerEsimate(file):
    global tiffShape
    global center
    img = tifffile.imread(file)
    tiffShape=img.shape
    print("shape is ", tiffShape)
    x = int(0)
    y = round(tiffShape[1] / 2)
    lenof0 = 0
    maxlen0 = 0
    mid = 0
    arr = img[:, y]
    plt.title(x)
    plt.plot(range(len(arr)), arr)
    plt.show()
    for x in range(tiffShape[0]):
        if img[x,y]<10:
            # print(x,y)
            lenof0+=1
        else:
            if lenof0>maxlen0:
                maxlen0=lenof0
                mid=int(x-lenof0/2)
            lenof0=0
    print(maxlen0)
    x=mid

    for y in range(tiffShape[1]):
        if img[x,y]<10:
            # print(x,y)
            lenof0+=1
        else:
            if lenof0>maxlen0:
                maxlen0=lenof0
                mid=int(y-lenof0/2)
            lenof0=0
    print(maxlen0)
    y=mid
    center=[x,y]
    blankRad=maxlen0
    print("shape center is ",x,y," blank radius is ",blankRad)

def plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = tifffile.imread("./500C/sample500C_tilt_15degree-06582.tif")
    for i in range(0,tiffShape[0],10):
        for j in range(0,tiffShape[1],10):
            ax.scatter(i,j,img[i][j])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

if __name__=="__main__":
    # centerEsimate("./sample.tif")
    # tiffToFeature("./sample.tif")
    plot()
