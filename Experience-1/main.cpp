#include "sortingalgorithms.h"

using namespace std;

void help()
{
    cout << "Usage: main <sorting method> <size> <random seed>" << endl;
}
int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        help();
        return -1;
    }
    int SIZE = stol(argv[2]);
    int SEED = stol(argv[3]);
    SortingFunctions sort;
    srand(SEED);
    int a[SIZE];
    int b[SIZE];
    for (int i = 0; i < SIZE; ++i)
    {
        a[i] = rand() % 100000;
        b[i] = 0;
    }

    // 计时开始
    long start = clock();

    int sorting_method = argv[1][0] - '0';
    switch (sorting_method)
    {
    case 1:
        cout << "Selection sorting: " << endl;
        sort.selectionSort(a, SIZE);
        break;
    case 2:
        cout << "Bubble sorting: " << endl;
        sort.bubble(a, SIZE);
        break;
    case 3:
        cout << "Merge sorting: " << endl;
        sort.mergeSort(a, b, 0, SIZE - 1);
        break;
    case 4:
        cout << "Quick sorting:" << endl;
        sort.quickSort(a, 0, SIZE - 1);
        break;
    case 5:
        cout << "Insert sorting:" << endl;
        sort.insertSort(a, SIZE);
        break;

    default:
        cout << "ERROR." << endl;
        return -1;
    }

    // 计时结束
    long finish = clock();

    double totaltime = (double)(finish - start) / CLOCKS_PER_SEC; // 算法耗时计算
    for (int i = 0; i < SIZE; i++)
        cout << a[i] << "  ";
    cout << endl;
    cout << "Data size: " << SIZE << ' ' << "Time cost：" << totaltime << 's' << endl;
    cout << endl
         << endl;
    return 0;
}