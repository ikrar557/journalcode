// Ikrar Bagaskara - 210103101 - 21T1'B
// Program Linear Search

#include <iostream>
using namespace std;

int search(int arr[], int n, int x)
{
	int i;
	for (i = 0; i < n; i++)
		if (arr[i] == x)
			return i;
	return -1;
}

void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}


int main(void)
{
	int x;
	int arr[] = { 10,20,30,40,50,60,70,80,90,100};
	int n = sizeof(arr) / sizeof(arr[0]);
	printArray(arr, n);
	cout << "Masukkan data yang akan di cari : ";
	cin >> x ;

	// Function call
	int result = search(arr, n, x);
	(result == -1)
		? cout << "Data tidak ada pada array"
		: cout << "Data tersedia pada array kolom : " << result;
	return 0;
}
