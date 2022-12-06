#include <bits/stdc++.h>
using namespace std;

int binarySearch(char arr[], int l, int r, char x)
{
  if (r >= l)
  {
    int mid = l + (r - l) / 2;

    if (arr[mid] == x)
    {
      if (arr[mid - 1] != x)
        return mid;
      else
        return binarySearch(arr, l, mid - 1, x);
    }

    return binarySearch(arr, mid + 1, r, x);
  }

  return -1;
}

int main(void)
{
    char arr[] = {1, 2, 3, 4, 5, '$', '$', '$' ,'$' ,'$' ,'$'};
    int n = sizeof(arr) / sizeof(arr[0]);


    int result = binarySearch(arr, 0, n - 1, '$');
    (result == -1)
        ? cout << "$ not found\n"
        : cout << "Fifth $ at index " << result+4 << endl;
  return 0;
}