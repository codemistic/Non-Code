#include<iostream>
using namespace std;
#include<string>
#include<vector>
void compute_prefix_function(string P,vector<int> &pi)
{
    int m,q,k;
    m = P.length();
    pi[0] =-1;
    k = -1;
    for(q=1;q<m;q++)
    {
        while((k>=0)&&(P[k+1]!=P[q]))
        {
            k = pi[k];
        }

        if(P[k+1]==P[q])
            k = k+1;
        
        pi[q] = k+1;
    }
}
void kmp_matcher(string T, string P)
{
    int n,m,q,i;
    n = T.length();
    m = P.length();
    vector<int> pi(m,-1);
    compute_prefix_function(P,pi);
    for(auto pi_entry:pi)
        cout<<pi_entry<<" ";
    cout<<endl;
    q = -1;
    for(i=0;i<n;i++)
    {
        while((q>=0)&&(P[q+1]!=T[i]))
            q = pi[q];
        if(P[q+1]==T[i])
            q = q+1;
        if(q==m-1)
        {
            cout<<"Pattern occurs at "<<i-(m-1)<<endl;
            q = pi[q];
        }
        
    }

}
int main()
{
    string T,P;
    int i;
    cin>>T>>P;
    kmp_matcher(T,P);
    
}
