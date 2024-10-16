#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

unsigned long long speed_step(unsigned long long a, unsigned long long n, unsigned long long limit) {
	if (n == 0)return 1;
	if (n % 2 == 1)return (((a % limit) * (speed_step(a, n - 1, limit) % limit)) % limit);
	unsigned long long b = speed_step(a, n / 2, limit);
	return (b * b) % limit;
}

int main() {
	unsigned long long a, n, limit;
	cin >> a >> n >> limit;
	cout << speed_step(a, n, limit) << '\n';
}
