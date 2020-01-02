import numpy as np

global tiffShape
global center

import matplotlib.pyplot as plt
import scipy.signal



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
    # ax=[]
    feature=[]
    while True:
        line=f.readline()
        if not line:
            break
        cutted=line.split(" ")
        # ax.append(float(cutted[1]))

        feature.append(float(cutted[3]))
    # plt.plot(ax,feature)
    # plt.title("before")
    # plt.show()




    # #peakmask
    # thres = np.max(feature) / 10
    # peaks=scipy.signal.find_peaks(feature,width=0,prominence=thres)
    # npeaks=len(peaks[0])
    # mask=np.zeros([len(feature)])
    # for i in range(npeaks):
    #     lp=int(peaks[1]['left_ips'][i])
    #     rp=int(peaks[1]['right_ips'][i])+1
    #     # peakmin=feature[lp]
    #     for j in range(lp,rp):
    #         # peakmin=min(peakmin,feature[j])
    #         mask[j]=1
    #     # for j in range(lp, rp):
    #     #     feature[j]-=peakmin
    # feature=feature*mask
    # #\peakmask


    return feature

if __name__=="__main__":
    print(chiToFeature("D:\\PXRDAutoEncoder\\500C chi\\sample500C_tilt_15degree-06534.chi"))
