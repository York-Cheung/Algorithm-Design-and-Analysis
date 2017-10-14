# -*- coding: utf-8 -*-
#
#@Author: Yorkson 
#@Date: 2017-10-08 03:02:41 
#@Last Modified by:   Yorkson 
#@Last Modified time: 2017-10-13 03:02:41 
#
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.pyplot import pause
import sys
import random

plt.ion()
colors = []
p = None 
pause_time = 0.01

# 入口函数
def closest(P, n):
    
    X=list(P)
    Y=list(P)

    # 预处理数据
    X.sort()
    Y = sort_y(Y)
    
    return closest_pair(X, Y, n)

# 分治法
def closest_pair(X, Y, n):
   
    if n <= 3:
        return brute_force(X, n)
             
    mid = n/2 
    Y_Left  = []
    Y_Right = [] 

    # 绘制直线L
    draw_line(X[mid][0])
    global pause_time
    pause(pause_time)

    print "Middle:", X[mid]
    
    for p in Y:
        if p in X[:mid]:
            Y_Left.append(p)
        else:
            Y_Right.append(p) 
    
    print "Y_RIGHT: %s" % Y_Right
    print "Y_LEFT : %s" % Y_Left

    dis_left  = closest_pair(X[:mid], Y_Left, mid)
    dis_right = closest_pair(X[mid:], Y_Right, n-mid)


    min_dis = min(dis_left, dis_right)
    
    print "min_dis: %s" % min_dis
     
    strip  = [] 

    # 只考虑dx2d的矩形区域
    for (x,y) in Y:
        if abs( x - X[mid][0] ) < min_dis:
            strip.append((x,y))
    return min(min_dis, strip_closest(strip, min_dis))

# 处理中间区域  
def strip_closest(strip, d):
    min_d = d
    global n
    for i,(x,y) in enumerate(strip):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_d and distance(strip[i], strip[j]) < min_d:
                min_d = distance(strip[i], strip[j])
    return min_d                   

# 计算两点距离
def distance(a,b):
    return math.sqrt( math.pow( (a[0]-b[0]), 2) + math.pow((a[1]-b[1]), 2) ) 

# 按y轴排序
def sort_y(tuples):
  return sorted (tuples,key=lambda last : last[-1])

# 当 n<=3 时使用蛮力法
def brute_force(X, n):
    global p
    min_d = distance(X[0], X[1])
    P1_min = X[0]
    P2_min = X[1]

    points = p.get_offsets().tolist()

    for i,(x,y) in enumerate(X):
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_d = distance(X[i], X[j])  
                colors[points.index([X[j][0],X[j][1]])]=1
                colors[points.index([x,y])]=1
                P1_min = X[i]
                P2_min = X[j]
            else:
                colors[points.index([X[0][0],X[0][1]])]=1
                colors[points.index([X[1][0],X[1][1]])]=1

    draw_line_points(P1_min, P2_min) 
    plt.text(P1_min[0]+1, P1_min[1]+1, "{0:.2f}".format(min_d), ha='left', rotation=random.randint(-60,60))
    
    global pause_time    
    pause(pause_time)   
    
    A=[]
    B=[]
    area = [100]*len(points)

    for x,y in p.get_offsets():
        A.append(x)
        B.append(y)
    plt.scatter(A,B,s=area,c=colors)
                  
    return min_d

# 绘制点
def plot_points(points):
    global colors
    global p

    X = []
    Y = []
    axis = []
    
    # Find X and Y values of points 
    for (x,y) in points:
        X.append(x)
        Y.append(y)

    # Set up X and Y axises
    axis.append(0)
    axis.append(max(X)+1)
    axis.append(0)
    axis.append(max(Y)+1)
    
    # Set up node area
    area = [100]*len(points)

    # Set up colors
    colors = [0.1]*len(points)

    p = plt.scatter(X, Y, s=area, c=colors)
    plt.axis(axis)
    plt.xticks(np.arange(0, max(X)+1, 1.0))
    plt.yticks(np.arange(0, max(Y)+1, 1.0))
    plt.grid(True)
    plt.show()

# 绘制垂直线
def draw_line(x):
    y_max = int(max(plt.yticks()[0]))

    line_y = range(0, y_max+1,1)
    line_x = [x]*len(line_y)
    line, = plt.plot(line_x,line_y,linewidth=2)

# 绘制两点连线
def draw_line_points(a,b):    
    x=[]
    x.append(a[0])
    x.append(b[0])

    y=[]
    y.append(a[1])
    y.append(b[1])

    line, = plt.plot(x,y,linewidth=1)
# 生成随机点
def gen_points(r):
    points=[]
    for i in range(1,r):
        points.append( (random.uniform(1, r), random.uniform(1, r)) )
    return points

########## Start Program ########
# 0. 输入规模
N = input("Set data size N = ")
# 1. 生成随机点
points = gen_points( N )
print points
# 2. 绘制随机点
plot_points(points)
pause(3)
# 3. 分治法求解
print "Minimum distance between two points is %s" % closest(points, len(points))
pause(0)
