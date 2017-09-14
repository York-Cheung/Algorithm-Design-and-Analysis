#ifndef SORTING_ALGORITHMS_H
#define SORTING_ALGORITHMS_H

#include <iostream>
#include <ctime>
#include <iterator>
#include <vector>
#include <algorithm>
#include <string>

class SortingFunctions
{
public:
    SortingFunctions(){};
    ~SortingFunctions(){};
    void selectionSort(int[], int);             // 选择排序
    void bubble(int[], int);                    // 冒泡排序
    void mergeSort(int[], int[], int, int);     // 归并排序
    void quickSort(int[], int, int);            // 快速排序
    void insertSort(int[], int);                // 插入排序

private:
    int partition(int array[], int left, int right);  // 快速排序中的轴值操作
    void merge(int[], int[], int, int); // 把两个有序数组合并成一个有序数组
};

#endif