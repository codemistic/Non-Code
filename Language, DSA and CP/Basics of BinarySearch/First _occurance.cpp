#include <iostream>

using namespace std; 
int firstOcc(int arr[],int size,int key) 
{ 
    int s=0 , e=size-1;  //e --> ending index vaue 
                      // s ---> Starting index value
    int mid = s+(e-s)/2; 
    int ans = -1; 
    while(s<=e) 
    { 
        if(arr[mid]==key) 
        {  
            ans = mid;
            e=mid-1; 
        } 
        if(key>arr[mid]) 
        { 
            s = mid+1; 
            
        } 
        else 
        { 
            e=mid-1; 
    } 
    mid=s +(e-s)/2;
} 
return ans;
}

int main()
{ 
    int arr[5] = {1,2,3,3,5};
    cout<<"First occurance of 3 is at Index "<<firstOcc(arr,5,3);

    return 0;
}
