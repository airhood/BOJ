#include <iostream>
#include <string>

using namespace std;

string result_a, result_b;

void Hanoi(int n, int k, long long mid, int from, int to, int by){
    if(n==1) {
        result_a = to_string(from) + " " + to_string(to);
        return;
    }
    else if(k<mid){
        Hanoi(n-1, k, (long long)(pow(2,n-1))/2, from,by,to);
    }
    else if (k>mid){
        k -= mid; //1번,2번 수행 횟수를 k에서 빼줌
        Hanoi(n-1, k, (long long)(pow(2,n-1))/2 , by,to,from);
    }
    else if(k==mid){
        result_a = to_string(from) + " " + to_string(to);
        return;
    }
}

int main() {
    int N;
    long long K;
    
    for (N = 3; N < 100; N++) {
        for (K = 1; K < pow(2, N); K++) {
            int A = ((K & (K - 1)) % 3) + 1;
            int B = (((K | (K - 1)) + 1) % 3) + 1;

            if (N % 2 == 0) {
                if (A == 2) A = 3;
                else if (A == 3) A = 2;
                
                if (B == 2) B = 3;
                else if (B == 3) B = 2;
            }
            result_b = to_string(A) + " " + to_string(B);
            
            long long total = (long long)(pow(2,N));
            Hanoi(N, K, total/2, 1,3,2);
            
            if (result_a != result_b) cout << N << ", " << K << " | " << result_a << "  vs  " << result_b << endl;
        }
    }
}