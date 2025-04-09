#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    int B, C, D;
    cin >> B >> C >> D;

    deque<int> burger(B);
    deque<int> side(C);
    deque<int> drink(D);
    for (int i = 0; i < B; i++) cin >> burger[i];
    for (int i = 0; i < C; i++) cin >> side[i];
    for (int i = 0; i < D; i++) cin >> drink[i];

    auto cmp = [](int a, int b) -> bool {
        return a > b;
    };

    sort(burger.begin(), burger.end(), cmp);
    sort(side.begin(), side.end(), cmp);
    sort(drink.begin(), drink.end(), cmp);

    int normal_price = 0;

    for (int i = 0; i < B; i++) normal_price += burger[i];
    for (int i = 0; i < C; i++) normal_price += side[i];
    for (int i = 0; i < D; i++) normal_price += drink[i];

    int discount_price = 0;

    while ((!burger.empty()) && (!side.empty()) && (!drink.empty())) {
        discount_price += (burger.front() + side.front() + drink.front()) * 0.9;
        burger.pop_front();
        side.pop_front();
        drink.pop_front();
    }

    for (int i = 0; i < burger.size(); i++) discount_price += burger[i];
    for (int i = 0; i < side.size(); i++) discount_price += side[i];
    for (int i = 0; i < drink.size(); i++) discount_price += drink[i];

    cout << normal_price << endl << discount_price;
}


#include<iostream>
#include<deque>
#include<algorithm>
using namespace std;
#define Z deque<int>
#define S(k,c)sort(k.begin(),k.end(),c);
#define e empty()
#define f front()
#define t pop_front();
#define o(a)for(int i=0;i<a.size();i++)
#define l(a)for(int i=0;i<a;i++)
#define c cin>>
int main(){int B,C,D;c B>>C>>D;Z b(B);Z s(C);Z d(D);o(b)c b[i];o(s)c s[i];o(d)c d[i];auto m=[](int a,int b){return a>b;};S(b,m);S(s,m);S(d,m);int p=0;l(B)p+=b[i];l(C)p+=s[i];l(D)p+=d[i];int q=0;while((!b.e)&&(!s.e)&&(!d.e)){q+=(b.f+s.f+d.f)*0.9;b.t s.t d.t}o(b)q+=b[i];o(s)q+=s[i];o(d)q+=d[i];cout<<p<<endl<<q;}