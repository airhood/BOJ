#include <iostream>

using namespace std;

int main(void)
{
	int k,n,m,dam;
    cin >> k;
	for(int z=0; z<k; z++)
	{
		dam=1;
        cin >> n >> m;
		for(int i=0; i<n; i++)
		{
			dam*=m-i; 
			dam/=1+i;
		}
        cout << dam << endl;
	}
}