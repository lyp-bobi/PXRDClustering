import sklearn.cluster
import os
import time
import numpy as np

from sklearn import metrics

import json

import tiffReader
import chiReader



np.set_printoptions(threshold=1e9)

#cluster tifs

names = os.listdir("./500C")
datanum=len(names)
start=time.time()
sumOfTifs=0
for i in range(datanum-1,-1,-1):
    if(names[i].find(".tif")!=-1):
        sumOfTifs+=1
    else:
        names.remove(names[i])
datanum=sumOfTifs
features=[]

for i in range(datanum):
    path=os.path.join("./500C", names[i])
    path= os.path.abspath(path)
    features.append(tiffReader.tiffToFeature(path))

# clustering = sklearn.cluster.MeanShift().fit(features)
clustering = sklearn.cluster.KMeans(n_clusters=10).fit(features)
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
    # features2.append(chiReader.chiToFeature(path))
    features2.append(chiReader.chiToPeak(path))


# clustering2 = sklearn.cluster.MeanShift().fit(features2)
clustering2 = sklearn.cluster.KMeans(n_clusters=10).fit(features)
print(clustering2.labels_)
end=time.time()
print("used time is "+str(end-start))

print("the difference of clustering is")
print(clustering.labels_-clustering2.labels_)

print("adjust rand score is"+str(metrics.adjusted_rand_score(clustering.labels_,clustering2.labels_)))

clustmap1={}
clustmap2={}
for i in range(datanum):
    clustmap1[names[i]]={"clusterNum":str(clustering.labels_[i])}
    clustmap2[names[i]] ={"clusterNum":str(clustering2.labels_[i])}

jsObj = json.dumps(clustmap1)

fileObject = open('tiffResult.json', 'w')
fileObject.write(jsObj)
fileObject.close()

jsObj = json.dumps(clustmap2)

fileObject = open('chiResult.json', 'w')
fileObject.write(jsObj)
fileObject.close()

# a=clustering.labels_-clustering2.labels_
#
# print(len(a))
# count=0
# for i in a:
#     if i!=0:
#         count+=1
# print(count)