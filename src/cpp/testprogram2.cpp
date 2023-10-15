#include<iostream>
using namespace std;

// this c++ file uses a recursive method to get fibonacci numbers
// it is not recommended to put n above 30

int fibonacci(int n) {
    if (n <= 1)
        return n;
    else
        return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int n = 10;
    cout << "Fibonacci(" << n << ") = " << fibonacci(n) << endl;
    return 0;
}
