// Sieve of Eratosthenes to print all prime numbers up to N

#include <iostream>
#include <vector>
using namespace std;

void sieveOfEratosthenes(int N) {
    vector<bool> isPrime(N + 1, true);
    isPrime[0] = isPrime[1] = false;

    for(int i = 2; i * i <= N; i++) {
        if(isPrime[i]) {
            for(int j = i * i; j <= N; j += i) {
                isPrime[j] = false;
            }
        }
    }

    cout << "Prime numbers up to " << N << " are: ";
    for(int i = 2; i <= N; i++) {
        if(isPrime[i]) cout << i << " ";
    }
    cout << endl;
}

int main() {
    int N;
    cout << "Enter a number: ";
    cin >> N;

    sieveOfEratosthenes(N);
    return 0;
}
