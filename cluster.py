import sklearn.cluster
import os
import time
import numpy as np

import tiffReader
import chiReader

np.set_printoptions(threshold=1e9)

#cluster tifs

list = os.listdir("./500C")
datanum=len(list)
start=time.time()
sumOfTifs=0
for i in range(datanum-1,-1,-1):
    if(list[i].find(".tif")!=-1):
        sumOfTifs+=1
    else:
        list.remove(list[i])
datanum=sumOfTifs
features=[]

for i in range(datanum):
    path=os.path.join("./500C",list[i])
    path= os.path.abspath(path)
    features.append(tiffReader.tiffToFeature(path))

clustering = sklearn.cluster.MeanShift().fit(features)
print(clustering.labels_)
end=time.time()
print("used time is "+str(end-start))

#cluster chis

list2 = os.listdir("./500C chi")
datanum2=len(list2)
start=time.time()
sumOfChis=0
for i in range(datanum2-1,-1,-1):
    if(list2[i].find(".chi")!=-1):
        sumOfChis+=1
    else:
        list2.remove(list2[i])
print(len(list2))
datanum2=sumOfChis
if datanum!=datanum2:
    print(datanum,datanum2)
features2=[]

for i in range(datanum):
    path=os.path.join("./500C chi",list2[i])
    path= os.path.abspath(path)
    # print(chiReader.chiToFeature(path))
    features2.append(chiReader.chiToFeature(path))


clustering2 = sklearn.cluster.MeanShift().fit(features2)
print(clustering2.labels_)
end=time.time()
print("used time is "+str(end-start))

print("the difference of clustering is")
print(clustering.labels_-clustering2.labels_)