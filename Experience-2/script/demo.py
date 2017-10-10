# -*- coding: utf-8 -*-
from Tkinter import *
import math
import sys
import random
from datetime import datetime
import time
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1.x-point2.x)**2 + (point1.y - point2.y)**2)
 
    def __str__(self):
        return "[x = {0}, y = {1}]".format(self.x, self.y)
 
    def __cmp__(self, other):
        return self.x < other.x
 
 
def debug(points):
    for p in points:
        print p
 
"""
产生长度为n的随机列表
"""
def randomList(n, maxN):
    data = [i for i in range(0, maxN)]
    result = data[:n]
    for i in xrange(n, maxN):
        r = random.randint(0, i)
        if r < n:
            result[r] = data[i]
    return result
 
"""
随机生成n个点
"""
def randomPoints(n, maxX, maxY):
    if n <= min(maxX, maxY):
        r = randomList(n, maxX)
        random.shuffle(r)
        points = [Point(x, x) for x in r]
        r = randomList(n, maxY)
        random.shuffle(r)
        for i in xrange(n):
            points[i].y = r[i]
        return points
    points = [Point(x, y) for x in xrange(maxX) for y in xrange(maxY)]
    if maxX * maxY <= n:
        return points
    # 从maxX x maxY个点中拿n个点
    result = points[:n]
    for i in xrange(n, maxX * maxY):
        r = random.randint(0, i)
        if r < n:
            result[r] = points[i]
    return result
 
 
class MinPoints:
    """
    一般的O(n^3)解法
    """
    def normalSolution(self, points):
        """
        :param points:点集合
        :return :tuple (最小距离,两个点)
        """
        minDis = sys.maxint
        resultP1, resultP2 = Point(-1, -1), Point(-1, -1)
        for i in xrange(len(points)):
            for j in xrange(i + 1, len(points)):
                dis = Point.distance(points[i], points[j])
                if dis < minDis:
                    minDis = dis
                    resultP1 = points[i]
                    resultP2 = points[j]
        return (minDis, resultP1, resultP2)
 
 
    def betterSolution(self, points):
        points.sort(key = lambda p:p.x)
        return self.help(points, 0, len(points))
 
    def help(self, points, start, end):
        if end - start < 2:
            return (sys.maxint, Point(-sys.maxint, -sys.maxint), Point(sys.maxint, sys.maxint))
        if end - start == 2:
            return (Point.distance(points[start], points[end - 1]), points[start], points[end - 1])
 
        mid = start + (end - start) / 2
        midP = points[mid]
 
        # 分别找到两个子集合的最近点距离
        dis1, p1, p2 = self.help(points, start, mid + 1)
        dis2, p3, p4 = self.help(points, mid, end)
 
        if dis1 < dis2:
            dis, resultP1, resultP2 = dis1, p1, p2
        else:
            dis, resultP1, resultP2 = dis2, p3, p4
 
        # 找到x坐标与x中值距离<dis的点
        midResult = [points[i] for i in xrange(start, end) if abs(points[i].x - midP.x) <= dis]
 
        midResult = sorted(midResult, key = lambda p:p.y)
        for i in xrange(len(midResult)):
            for j in xrange(i + 1, min(i + 8, len(midResult))):
                # 如果y的距离差已经不小于dis,直接比下一个点
                if abs(midResult[i].y - midResult[j].y) >= dis:
                    break
                tempDis = Point.distance(midResult[i], midResult[j])
                if tempDis < dis:
                    dis = tempDis
                    resultP1, resultP2 = midResult[i], midResult[j]
        return (dis, resultP1, resultP2)
 
class MinPointsDemo:
    def __init__(self):
        self.s = MinPoints()
        self.MAX_WIN_WIDTH, self.MAX_WIN_HEIGHT, self.CANVAS_WIDTH = 1000, 700, 800
        self.points = []
        self.window = Tk()
        self.window.title("最近点对Demo")
        self.window.geometry("{0}x{1}".format(self.MAX_WIN_WIDTH, self.MAX_WIN_HEIGHT))
 
        self.canvas = Canvas(self.window, width = self.CANVAS_WIDTH, height = self.MAX_WIN_HEIGHT, bg = "white")
        self.canvas.pack(side = LEFT)
        self.canvas.bind("<Button-1>", self.drawPoint)
 
        self.operFrame = Frame(self.window, width = self.MAX_WIN_WIDTH - self.CANVAS_WIDTH, height = self.MAX_WIN_HEIGHT, bg = "#f9f9f9")
        self.operFrame.pack(side = RIGHT, expand=YES, fill=BOTH)
 
        # 在操作框中添加操作按钮
        n2Btn = Button(self.operFrame, text = "O(n^2)算法查找", fg = "brown", pady = 10, command = self.n2MinPoints)
        n2Btn.pack()
 
        self.n2Label = Label(self.operFrame, text = "用时:", pady = 20)
        self.n2Label.pack()
 
        nlgnBtn = Button(self.operFrame, text = "O(nlgn)算法查找", fg = "brown", pady = 10, command = self.nlgnMinPoints)
        nlgnBtn.pack()
 
        self.nlgnLabel = Label(self.operFrame, text = "用时:", pady = 20)
        self.nlgnLabel.pack()
 
        randPointsFrame = Frame(self.operFrame)
        randPointsFrame.pack()
        randPointsHintLabel = Label(randPointsFrame, text = "随机生成点数:")
        randPointsHintLabel.pack(side = LEFT)
        self.randPointsEntry = Entry(randPointsFrame)
        self.randPointsEntry.pack(side = RIGHT)
 
        showPointsBtn = Button(self.operFrame, text = "确定", command = self.showRandomPoints)
        showPointsBtn.pack()
 
        self.numHintLabel = Label(self.operFrame, text = "", fg = "red")
        self.numHintLabel.pack()
 
        clearPointsBtn = Button(self.operFrame, width = 100, text="清空点", pady=30, command = self.clearPoints)
        clearPointsBtn.pack()
 
        self.hintLabel = Label(self.operFrame, bg = "#b5acac", wraplength = 190, justify = "center", text = "提示:\n左侧区域为可绘制点区域,最左上角坐标为(0,0),横轴向右为正,纵轴向下为正.")
        self.hintLabel.pack()
 
        self.window.mainloop()
         
    def n2MinPoints(self):
        start = time.time()
        minDis, p1, p2 = self.s.normalSolution(self.points)
        end = time.time()
        delta = int(1000 * (end - start))
        self.n2Label.config(text = "用时:" + str(delta) + "ms")
 
        self.canvas.delete("line")
        self.canvas.delete("point")
        self.canvas.create_oval(p1.x, p1.y, p1.x, p1.y, fill = "red", outline = "red", tags = ("n2", "point"))
        self.canvas.create_oval(p2.x, p2.y, p2.x, p2.y, fill = "red", outline = "red", tags = ("n2", "point"))
        self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill = "#42f468", tags = ("n2", "line"))
 
    def nlgnMinPoints(self):
        start = time.time()
        minDis, p1, p2 = self.s.normalSolution(self.points)
        end = time.time()
        delta = int(1000 * (end - start))
        self.nlgnLabel.config(text = "用时:" + str(delta) + "ms")
 
        self.canvas.delete("line")
        self.canvas.delete("point")
        self.canvas.create_oval(p1.x, p1.y, p1.x, p1.y, fill = "#42f468", outline = "#42f468", tags = ("nlgn", "point"))
        self.canvas.create_oval(p2.x, p2.y, p2.x, p2.y, fill = "#42f468", outline = "#42f468", tags = ("nlgn", "point"))
        self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill = "red", tags = ("nlgn", "line"))
 
    def drawPoint(self, event):
        p = Point(event.x, event.y)
        self.showPoint(p)
        self.points.append(p)
 
    def showRandomPoints(self):
        num = self.randPointsEntry.get()
        if not num.isdigit():
            self.numHintLabel.config(text = "请输入>0的整数")
            return
        self.clearPoints()
        self.numHintLabel.config(text = "")
        self.points = randomPoints(int(num), self.CANVAS_WIDTH, self.MAX_WIN_HEIGHT)
        for p in self.points:
            self.showPoint(p)
 
    def showPoint(self, p):
        self.canvas.create_oval(p.x, p.y, p.x, p.y)
 
    def clearPoints(self):
        self.canvas.delete("all")
        self.points = []
 
if __name__ == "__main__":
    MinPointsDemo()