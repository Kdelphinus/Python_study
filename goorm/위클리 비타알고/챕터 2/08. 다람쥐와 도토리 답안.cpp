#include <iostream>
using namespace std;

const int MOD = 1000000007;

long long fpow(int a, int n) {
    long long ret = 1;

    // n을 이진수로 생각하여 해당 비트에 대응되는 a^(2^k)을 곱한다
    while (n) {
        if (n & 1) ret = ret * a % MOD;
        a = (long long)a * a % MOD;
        n >>= 1;
    }
    return ret;
}
long long C(int n, int r) {
    long long a = 1, b = 1;

    // a = n! / (n-r)!
    // b = r!
    for (int i = 0; i < r; ++i) {
        a = a * (n - i) % MOD;
        b = b * (i + 1) % MOD;
    }

    // nCr = a / b = a * b^-1
    return a * fpow(b, MOD - 2) % MOD;
}
int main() {
    int N, M, x1, y1, x2, y2;
    cin >> N >> M >> x1 >> y1 >> x2 >> y2;

    // 시작위치 -> 도토리
    long long a = C(x1 + y1, x1);
    // 도토리 -> 최종위치
    long long b = C(N - x1 + M - y1, N - x1);

    // 시작위치 -> 도토리에 함정이 있는 경우
    if (x2 <= x1 && y2 <= y1)
        a -= C(x2 + y2, x2) * C(x1 - x2 + y1 - y2, x1 - x2) % MOD;

    // 도토리 -> 최종위치에 함정이 있는 경우
    if (x1 <= x2 && y1 <= y2)
        b -= C(x2 - x1 + y2 - y1, x2 - x1) * C(N - x2 + M - y2, N - x2) % MOD;

    // 음수가 됐다면 양수로 만들어 준다
    if (a < 0) a += MOD;
    if (b < 0) b += MOD;

    cout << a * b % MOD;

    return 0;
}