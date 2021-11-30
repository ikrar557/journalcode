// C++ program to implement recursive Binary Search
#include <bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int l, int r, int x)
{
	if (r >= l) {
		int mid = l + (r - l) / 2;
		if (arr[mid] == x)
			return mid;
			
		if (arr[mid] > x)
			return binarySearch(arr, l, mid - 1, x);


		return binarySearch(arr, mid + 1, r, x);
	}
	return -1;
}

int main(void)
{
	int arr[9] = { 3,6,9,10,13,16,26,38,58 };
  cout << "Array Index:" << endl;
  int loop;

  for(loop = 0; loop < 9; loop++)
      printf("%d ", arr[loop]);
  cout << " " << endl;
	int x;
  cout << "Input Data: ";
  cin >> x;
	int n = sizeof(arr) / sizeof(arr[0]);
	int result = binarySearch(arr, 0, n - 1, x);
	(result == -1) ? cout << "Angka tidak tersedia di array"
				: cout << "Angka tersedia di array " << result;
	return 0;
}
