/*
 * @Author: Yorkson 
 * @Date:   2017-10-07 22:35:41 
 * @Last Modified by: Yorkson
 * @Last Modified time: 2017-10-14 11:32:16
 */
#include <iostream>
#include <ctime>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <set>
using namespace std;

/* 
 * 定义二维点类和全局变量 
 */
class Point
{
  public:
	double x, y;
	Point() : x(0), y(0){};
	Point(double x_, double y_) : x(x_), y(y_){};
	bool operator<(const struct Point &right) const // 重载<运算符
	{
		if (this->x == right.x && this->y == right.y) // 根据坐标去重
			return false;
		else
		{
			if (this->x != right.x)
			{
				return this->x < right.x; // 按x轴升序排列
			}
			else
			{
				return this->y < right.y; // 若x轴相同按y轴升序排列
			}
		}
	}
};

Point *p = NULL;
Point *p1 = NULL;

int a[10000000];
double pointx1, pointy1;
double pointx2, pointy2;

//对x进行排序
int compx(const Point &a, const Point &b)
{
	return a.x < b.x;
}

//对y进行排序
int compy(int &a, int &b)
{
	return p[a].y < p[b].y;
}

//求两点之间的距离
double dis(const Point &a, const Point &b)
{
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

//返回较小的距离
double min(double a, double b)
{
	return a > b ? b : a;
}

/* 
 * 蛮力法求最近点对
 */
double brute_force(int n)
{
	double dis;
	int i, j;

	double min = RAND_MAX;
	int x1, x2, y1, y2;

	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
		{
			dis = sqrt((p[i].x - p[j].x) * (p[i].x - p[j].x) + (p[i].y - p[j].y) * (p[i].y - p[j].y));
			if (dis < min)
			{
				x1 = p[i].x;
				y1 = p[i].y;
				x2 = p[j].x;
				y2 = p[j].y;
				min = dis;
			}
		}

	//记录
	pointx1 = x1;
	pointy1 = y1;
	pointx2 = x2;
	pointy2 = y2;

	return min;
}

/* 
 * 分治法递归求最小距离
 */
double divide_and_conquer(int low, int high)
{
	// n = 1, distance = ∞
	if (low == high)
		return RAND_MAX;
	// n = 2, 直接返回两点距离
	if (low + 1 == high)
		return dis(p[low], p[high]);
	// n = 3, 蛮力法查找
	if (low + 2 == high)
		return min(min(dis(p[low], p[low + 1]), dis(p[low], p[high])), dis(p[low + 1], p[high]));

		
	int mid = (low + high) / 2;
	double d = min(divide_and_conquer(low, mid), divide_and_conquer(mid + 1, high));

	// 计算得到的矩形区域里面最短距离的点对，并和之前递归调用得到的最短距离相比较，得出最短距离
	int i, j, t = 0;
	for (i = low; i <= high; i++)
		if (p[i].x >= p[mid].x - d && p[i].x <= p[mid].x + d)
			a[t++] = i;

	// 快速排序，线性效率
	sort(a, a + t, compy);

	for (i = 0; i < t; ++i)
	{
		int one = 0;
		for (j = i + 1; j < t; ++j)
		{
			if (one < 7)
			{
				if (p[a[j]].y - p[a[i]].y <= d)
					d = min(d, dis(p[a[i]], p[a[j]]));
				one++;
			}
			else
			{
				break;
			}
		}
	}

	return d;
}

/* 
 * 程序开始
 */
int main()
{

	int n, i;
	pointx1 = 0;
	pointy1 = 0;
	pointx2 = 0;
	pointy2 = 0;

	double time1, time2; //分治法所需时间
	double time3, time4; //蛮力法所需时间

	for (int counter = 1; counter <= 10; counter++)
	{
		set<Point> points_set;
		n = counter * 10;
		p = new Point[n];
		p1 = new Point[n];

		srand(counter); //设置随机种子值
		for (i = 0; i < n; i++)
		{
			points_set.insert(Point(rand(), rand()));
		}
		int i_ = 0;
		for (auto it : points_set)
		{
			p[i_].x = it.x;
			p[i_].y = it.y;
			p1[i_].x = it.x;
			p1[i_].y = it.y;
			i_++;
		}
		for (i = 0; i < n; i++)
		{
			cout << p[i].x << " , " << p[i].y << endl;
		}

		cout << "Generating random points done." << endl;
		cout << "Data Scale:    " << n << endl;
		cout << "Size of set: 	" << points_set.size() << endl;

		// 蛮力法
		cout << "Brute Force..." << endl;

		time3 = clock();
		cout << "Distance: " << brute_force(n) << endl;
		time4 = clock() - time3;
		cout << "Time cost: " << time4 << "ms" << endl;
		cout << "The Points: "
		<< "(" << pointx1 << "," << pointy1 << ")  "
		<< "(" << pointx2 << "," << pointy2 << ")" << endl;
		// 分治法
		cout << "Divide and Conquer..." << endl;

		time1 = clock();

		// 线性效率的快速排序
		sort(p, p + n, compx);
		cout << "Distance: " << divide_and_conquer(0, n - 1) << endl;
		time2 = clock() - time1;
		cout << "Time cost: " << time2 << "ms" << endl;

		cout << "The Points: "
			 << "(" << pointx1 << "," << pointy1 << ")  "
			 << "(" << pointx2 << "," << pointy2 << ")" << endl;
	}
	return 0;
}