#include<bits/stdc++.h>
using namespace std;
int binarySearch(int arr[],int target,int n){
	int start=0;
	int end=n-1;
	while(start<=end){
		int mid=start+(end-start)/2;
		if(target<arr[mid])
			end=mid-1;
		else if(target>arr[mid])
			start=mid+1;
		else
			return mid;
	}
	return -1;
}
int main(){
	int arr[]={1,2,3,4,5};
	int target=5;
	int len=sizeof(arr)/sizeof(arr[0]);
	cout<<"The index of the "<<target<<" is: "<<binarySearch(arr,target,len)<<endl;
	return 0;
}
