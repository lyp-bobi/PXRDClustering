import sklearn.cluster
import os
import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

import json

import tiffReader
import chiReader

def rand_index(y_true, y_pred):
    n = len(y_true)
    a, b = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if (y_true[i] == y_true[j]) & (y_pred[i] == y_pred[j]):
                a += 1
            elif (y_true[i] != y_true[j]) & (y_pred[i] != y_pred[j]):
                b += 1
            else:
                pass
    RI = (a + b) / (n * (n - 1) / 2)
    return RI



np.set_printoptions(threshold=1e9)

#parameters
tifFiles="./500C"
chiFiles="./500C chi"
# visualize=True
visualize=False


#cluster tifs
names = os.listdir(tifFiles)
datanum=len(names)
# start=time.time()
sumOfTifs=0
for i in range(datanum-1,-1,-1):
    if(names[i].find(".tif")!=-1):
        sumOfTifs+=1
    else:
        names.remove(names[i])
datanum=sumOfTifs
featuresTif=[]
featuresChi=[]
names.sort()
cNames=[]
for i in range(datanum):
    path1=os.path.join(tifFiles, names[i])
    path1= os.path.abspath(path1)
    f1=tiffReader.tiffToFeature(path1)
    featuresTif.append(f1)
    chiName=names[i].replace(".tif",".chi")
    cNames.append(names[i].replace(".tif",""))
    path2 = os.path.join(chiFiles, chiName)
    path2 = os.path.abspath(path2)
    f2=chiReader.chiToPeak(path2)
    featuresChi.append(f2)
    if visualize:
        if i %10==9:
            input("next:")
        plt.title(i)
        plt.plot(range(len(f1)),f1)
        plt.show()
        plt.title(i)
        plt.plot(range(len(f2)), f2)
        plt.show()





for nclust in [3,4,5,6,7,8,9,10,20,30]:
    # clustering = sklearn.cluster.MeanShift().fit(features)
    clustering = sklearn.cluster.AgglomerativeClustering(n_clusters=nclust).fit(featuresTif)
    # plt.hist(clustering.labels_,bins=nclust)
    # plt.title(nclust)
    # plt.show()
    # print(clustering.labels_)
    # end=time.time()
    # print("used time is "+str(end-start))

    # clustering2 = sklearn.cluster.MeanShift().fit(features2)
    clustering2 = sklearn.cluster.AgglomerativeClustering(n_clusters=nclust).fit(featuresChi)
    # plt.hist(clustering2.labels_, bins=nclust)
    # plt.title(nclust)
    # plt.show()
    # print(clustering2.labels_)
    # end=time.time()
    # print("used time is "+str(end-start))

    # print("the difference of clustering is")
    # print(clustering.labels_-clustering2.labels_)
    print(nclust)
    print("rand score is" + str(rand_index(clustering.labels_, clustering2.labels_)))

    # print("adjust rand score is"+str(metrics.adjusted_rand_score(clustering.labels_,clustering2.labels_)))
    #
    # print("adjust mutual info score is" + str(metrics.adjusted_mutual_info_score(clustering.labels_, clustering2.labels_)))


    clustmap1={}
    clustmap2={}
    for i in range(len(cNames)):
        clustmap1[cNames[i]]={"clusterNum":str(clustering.labels_[i])}
        clustmap2[cNames[i]] ={"clusterNum":str(clustering2.labels_[i])}

    jsObj = json.dumps(clustmap1)

    fileObject = open("tiffResult"+str(nclust)+".json", 'w')
    fileObject.write(jsObj)
    fileObject.close()

    jsObj = json.dumps(clustmap2)

    fileObject = open("chiResult"+str(nclust)+".json", 'w')
    fileObject.write(jsObj)
    fileObject.close()

