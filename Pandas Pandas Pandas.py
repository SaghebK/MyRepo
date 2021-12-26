# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:56:05 2021

author: Sagheb Kohpayeh Araghi

Data Science - Pandas Pandas Pandas


Finding the next centroid

Unsupervised learning algorithm clustering involves updating the centroid of 
each cluster. Here we find the next centroids for given data points and 
initial centroids.

Task
Assume that there are two clusters among the given two-dimensional data points
 and two random points (0, 0), and (2, 2) are the initial cluster centroids. 
 Calculate the euclidean distance between each data point and each of the 
 centroid, assign each data point to its nearest centroid, then calculate the 
 new centroid. If there's a tie, assign the data point to the cluster with 
 centroid (0, 0). If none of the data points were assigned to the given 
 centroid, return None.

Input Format
First line: an integer to indicate the number of data points (n)
Next n lines: two numeric values per each line to represent a data point in 
two dimensional space.

Output Format
Two lists for two centroids. Numbers are rounded to the second decimal place.

Sample Input
3
1 0
0 .5
4 0

Sample Output
[0.5 0.25]
[4. 0.]
Explanation
There are 3 data points and we would like to identify two clusters among them.
 Initial centroids are given (0, 0), and (2, 2). The distances between the 
 first data point (1, 0) and each of the centroids are 1.0 and 2.24, rounded 
 to the second decimal place. The first data point is closter to (0, 0), thus
 assigned the 0-th cluster. Similarly data point (0, .5) is closer to (0, 0)
 than to (2, 2), also assigned to the 0th cluster; while (4, 0) is closter to 
 (2, 2), thus assigned to the 1st cluster. To calculate the new centroids, 
 take the mean of all data points in the 0-th and 1st cluster, respectively. 
 Hence the results are [0.5 0.25] and [4. 0.].
"""
import numpy as np

n = int(input())
# Initial centroids
p1 =  np.array([0, 0])   # 1st point
p2 =  np.array([2, 2])   # 2nd point


class_1 = []
class_2 = []
XY = []

for i in range(n):
    XY.append([float(i) for i in input().split()])
    
    new_point = np.array(XY[-1])
    
    dist1 = np.sqrt(((new_point - p1) ** 2).sum())
    dist2 = np.sqrt(((new_point - p2) ** 2).sum())
    if dist1 < dist2:
        class_1.append(XY[-1])
    elif dist1 > dist2:
        class_2.append(XY[-1])
    else:
        class_1.append(XY[-1])

if len(class_1)>0:
    print(np.average(np.array(class_1),axis=0).round(2))
else:
    print(None)


if len(class_2)>0:
    print(np.average(np.array(class_2),axis=0).round(2))
else:
    print(None)
