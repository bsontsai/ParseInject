#include <iostream>
#include <cstdlib> 
#include <ctime>
// this c++ file shows a double loop
int main() {
    srand(static_cast<unsigned int>(time(0))); // seed random number generator
    int n1 = 10;
    int n2 = 100;
    // This is a double loop with O(n^2)
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n2; j++) {
            int result = array[i] / 2;
        }
    }
    return 0;
}
