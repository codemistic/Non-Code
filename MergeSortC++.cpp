#include <iostream>
using namespace std;
void merge(int arr[],int l,int mid,int r,int size)
{
   int n1=mid-l+1;
   int n2=r-mid;
   int a[n1];
   int b[n2];
   for(int i=0;i<n1;i++)
   {
      a[i]=arr[l+i];
   }
   for(int j=0;j<n2;j++)
   {
      b[j]=arr[mid+1+j];
   }
   int i=0;
   int j=0;
   int k=l;
   while(i<n1&&j<n2)
   {
      if(a[i]<b[j])
      {
         arr[k]=a[i];
         k++;
         i++;
      }
      else{
         arr[k]=b[j];
         k++;
         j++;
      }
   }
   while(i<n1)
   {
      arr[k]=a[i];
      k++;
      i++;
   }
   while(j<n2)
   {
      arr[k]=b[j];
      k++;
      j++;
   }
}
void mergesort(int arr[],int l,int r,int size)
{  int mid;
   if(l<r)
   {
      mid=(l+r)/2;
      mergesort(arr,l,mid,size);
      mergesort(arr,mid+1,r,size);
      
      merge(arr,l,mid,r,size);
   }
}
int main()
{
   cout << "Enter size of array: " << endl;
    int size;
    cin >> size;
    int myarray[size];

    cout << "Enter " << size << " integers in any order: " << endl;
    for (int i = 0; i < size; i++)
    {
        cin >> myarray[i];
    }
    cout << "Before Sorting" << endl;
    for (int i = 0; i < size; i++) 
    {
        cout << myarray[i] << " ";
    }
    cout << endl;
    mergesort(myarray, 0, (size - 1), size); 

    cout << "After Sorting" << endl;
    for (int i = 0; i < size; i++)
    {
        cout << myarray[i] << " ";
    }
    return 0;
}
