#include <iostream>
#include <vector>
#include <math.h>

using namespace std;
// 1 2 3 5 8 13 21 34 55 89
// 1 0   0 1
// 0 1   1 2
// 1 1   2 3
// 1 2   3 4
// 2 3   4 5
// 3 5   5 6
// 5 8   6 7
int main() {
    int D, K;
    cin >> D >> K;

    vector<int> fibo(D);
    fibo[0] = 1;
    fibo[1] = 1;
    for (int i = 2; i < D; i++) {
        fibo[i] = fibo[i-2] + fibo[i-1];
    }
    
    int a = fibo[D - 3];
    int b = fibo[D - 2];

    if (D == 1) {
        a = 1;
        b = 0;
    }
    else if (D == 2) {
        a = 0;
        b = 1;
    }

    for (int x = 1; x <= floor(K/a); x++) {
        int L = K - (a * x);
        if (L % b == 0) {
            int R = floor(L / b);
            cout << x << endl << R;
            return 0;
        }
    }
}


// 숏코딩

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int main(){int D,K;cin>>D>>K;vector<int>fibo(D);fibo[0]=1;fibo[1]=1;for(int i=2;i<D;i++){fibo[i]=fibo[i-2]+fibo[i-1];}int a=fibo[D-3];int b=fibo[D-2];if(D==1){a=1;b=0;}else if(D==2){a=0;b=1;}for(int x=1;x<=floor(K/a);x++){int L=K-(a*x);if(L%b==0){int R=floor(L/b);cout<<x<<endl<<R;return 0;}}}