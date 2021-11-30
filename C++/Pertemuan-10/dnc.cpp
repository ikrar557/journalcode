
# include<iostream>
using namespace std;
int DAC_Max(int arr[], int index, int l)
{
	int max;
	if(index >= l - 2)
	{
		if(arr[index] > arr[index + 1])
		return arr[index];
		else
		return arr[index + 1];
	}
	max = DAC_Max(arr, index + 1, l);
	if(arr[index] > max)
	return arr[index];
	else
	return max;
}

int DAC_Min(int arr[], int index, int l)
{
	int min;
	if(index >= l - 2)
	{
		if(arr[index] < arr[index + 1])
		return arr[index];
		else
		return arr[index + 1];
	}

	min = DAC_Min(arr, index + 1, l);
	if(arr[index] < min)
	return arr[index];
	else
	return min;
}
// Driver code
int main()
{
	int arr[] = {25, 20, 15, 3, 7, 2, 1};
	int n = sizeof(arr) / sizeof(arr[0]);
	int max, min;
	max = DAC_Max(arr, 0, n);
	min = DAC_Min(arr, 0, n);
	cout << "Maximum: " << max << endl;
	cout << "Minimum: " << min << endl;
	return 0;
}
// This code is contributed by probinsah.
