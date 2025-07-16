#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int ROOT = 3;

int mod_inverse(int a, int mod)
{
    int result = 1, b = mod - 2;
    while (b)
    {
        if (b & 1)
            result = 1LL * result * a % mod;
        a = 1LL * a * a % mod;
        b >>= 1;
    }
    return result;
}

int mod_pow(int a, int b, int mod)
{
    int result = 1;
    while (b)
    {
        if (b & 1)
            result = 1LL * result * a % mod;
        a = 1LL * a * a % mod;
        b >>= 1;
    }
    return result;
}

void ntt(vector<int> &a, bool inverse)
{
    int N = a.size();

    for (int i = 1, j = 0; i < N; i++)
    {
        int bit = N >> 1;
        while (j & bit)
        {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j)
            swap(a[i], a[j]);
    }

    for (int step = 2; step <= N; step <<= 1)
    {
        int half = step >> 1;
        int w = 1;
        int wn = mod_pow(ROOT, (MOD - 1) / step, MOD);
        if (inverse)
            wn = mod_inverse(wn, MOD);

        for (int i = 0; i < N; i += step)
        {
            w = 1;
            for (int j = 0; j < half; ++j)
            {
                int u = a[i + j];
                int v = 1LL * a[i + j + half] * w % MOD;
                a[i + j] = (u + v) % MOD;
                a[i + j + half] = (u - v + MOD) % MOD;
                w = 1LL * w * wn % MOD;
            }
        }
    }

    if (inverse)
    {
        int n_inv = mod_inverse(N, MOD);
        for (int i = 0; i < N; ++i)
            a[i] = 1LL * a[i] * n_inv % MOD;
    }
}

vector<int> string_to_digits(const string &s)
{
    vector<int> digits(s.size());
    for (int i = 0; i < s.size(); ++i)
        digits[i] = s[s.size() - 1 - i] - '0';
    return digits;
}

string multiply_large_numbers(string a_str, string b_str)
{
    vector<int> a = string_to_digits(a_str);
    vector<int> b = string_to_digits(b_str);

    int n = 1;
    while (n < a.size() + b.size())
        n <<= 1;

    a.resize(n);
    b.resize(n);

    ntt(a, false);
    ntt(b, false);

    vector<int> c(n);
    for (int i = 0; i < n; ++i)
        c[i] = 1LL * a[i] * b[i] % MOD;

    ntt(c, true);

    vector<int> result(n);
    int carry = 0;
    for (int i = 0; i < n; ++i)
    {
        int total = c[i] + carry;
        result[i] = total % 10;
        carry = total / 10;
    }

    while (carry)
    {
        result.push_back(carry % 10);
        carry /= 10;
    }

    while (result.size() > 1 && result.back() == 0)
        result.pop_back();

    string res;
    for (int i = result.size() - 1; i >= 0; --i)
        res += (result[i] + '0');
    return res;
}

int main()
{
    string A, B;
    cin >> A >> B;
    cout << multiply_large_numbers(A, B) << endl;
    return 0;
}