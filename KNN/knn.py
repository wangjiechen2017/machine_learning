from numpy import *
import operator

def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
    
    
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]                              #得到行数
    diffMat = tile(inX, tile(dataSetSize,1)) - dataSetSize      #tile函数,重复array
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)                       #sum(axis = 1)行方向上相加
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    
    
    
    
