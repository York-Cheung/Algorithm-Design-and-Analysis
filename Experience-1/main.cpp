#include "sorting_algorithms.h"
#include <iostream>
#include <ctime>
#include <iterator>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define SIZE 50
int main()
{
    SortingFunctions sort;  
    srand(time(NULL));    
    int a[SIZE];
    int b[SIZE];
    for (int i = 0; i < SIZE; ++i)
    {
        a[i] = rand() % 100000; 
        b[i] = 0;
    }

    // 计时开始
    long start = clock();
    
        // sort.selectionSort(a, SIZE);
        sort.bubble(a, SIZE);
        //sort.mergeSort(a, b, 0, SIZE - 1);
        //sort.quickSort(a, 0, SIZE - 1);
        //sort.insertSort(a, SIZE);
    
    // 计时结束
    long finish = clock();
    
    double totaltime = (double)(finish - start) / CLOCKS_PER_SEC; // 算法耗时计算
    for (int i = 0; i<SIZE; i++)
        cout << a[i] << "  ";
    cout << endl;
    cout << "算法耗时：" << totaltime << 's';
    cout << endl;
    getchar();
    return 0;
}