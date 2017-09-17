#include "sortingalgorithms.h"

using namespace std;

// 选择排序
void SortingFunctions::selectionSort(int array[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        // 内循环，每次循环时找出比array[min]小的元素，将其坐标赋给min作为新的最小元素值
        for (int j = i + 1; j < n; j++)
        {
            if (array[j] < array[min])
                min = j;
        }
        swap(array[i], array[min]);
    }
}

// 冒泡排序
void SortingFunctions::bubble(int array[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = n - 1; j > 0; j--)
        {
            if (array[j] < array[j - 1])
                swap(array[j], array[j - 1]);
        }
    }
}

// 快速排序的一次循环子函数
// 将轴值放到数组的适当的位置
int SortingFunctions::partition(int array[], int left, int right)
{
    int pivot = (left + right) / 2;
    int tmp = array[pivot];
    swap(array[pivot], array[right]); // 把轴值放到最右
    int i = left;
    int j = right;
    while (1)
    {
        // 左边指针i向右移动，直到找到一个大于轴值tmp的值
        while (1)
        {
            // 如果i与j相遇则确定轴值位置，将当前下标返回
            if (i == j)
            {
                array[i] = tmp;
                return i;
            }
            // 若轴值左边元素大于轴值，则与轴值右边j下标元素互换
            if (array[i] > tmp)
            {
                array[j] = array[i];
                j--;
                break;
            }
            i++;
        }
        // 右边指针j向左移动，直到找到一个小于轴值tmp的值
        while (1)
        {
            // 如果i与j相遇则确定轴值位置，将当前下标返回
            if (i == j)
            {
                array[j] = tmp;
                return j;
            }
            // 若轴值右边元素小于轴值，则与轴值坐边i下标元素互换
            if (array[j] < tmp)
            {
                array[i] = array[j];
                i++;
                break;
            }
            j--;
        }
    }
}

// 快速排序
void SortingFunctions::quickSort(int array[], int left, int right)
{
    if (right <= left)
        return;
    int pivot = SortingFunctions::partition(array, left, right);
    quickSort(array, left, pivot - 1);
    quickSort(array, pivot + 1, right);
}

// 插入排序
void SortingFunctions::insertSort(int array[], int n)
{
    for (int i = 1; i < n; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (array[j] < array[j - 1])
                swap(array[j - 1], array[j]);
            else
                break;
        }
    }
}

// 归并排序
void SortingFunctions::mergeSort(int array[], int temp[], int left, int right)
{
    int middle = (left + right) / 2;
    if (left >= right)
        return;
    mergeSort(array, temp, left, middle);
    mergeSort(array, temp, middle + 1, right);
    for (int i = left; i <= right; i++)
        temp[i] = array[i];
    // 分前后两部分
    int j = left;
    int k = middle + 1;
    for (int curr = left; curr <= right; curr++)
    {
        if (j == middle + 1)
            array[curr] = temp[k++];
        else if (k > right)
            array[curr] = temp[j++];
        else if (temp[j] < temp[k])
            array[curr] = temp[j++];
        else
        {
            array[curr] = temp[k++];
        }
    }
}
