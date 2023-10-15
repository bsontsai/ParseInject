#include <iostream>
#include <cstdlib> 
#include <ctime>

// this c++ file shows single loop and two double loops

int main() {
    srand(static_cast<unsigned int>(time(0))); // seed random number generator

    int n1 = 10;
    int n2 = 100;
    int array[n2];

    // This is a loop with O(n)
    for (int i = 0; i < n1; ++i) {
        array[i] = rand() % 100;
        //std::cout << "array[" << i << "] = " << array[i] << '\n';
    }

    // This is a double loop with O(n^2)
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n2; j++) {
            int result = array[i] / 2;
            //std::cout << "Operation result: " << result << '\n';
        }
    }

    // This is also a double loop with O(0.5n^2)
    for (int i = 0; i < n1; i++) {
        for (int j = i; j < n1; j++) {
            int result = array[i] / 2;
            //std::cout << "Operation result: " << result << '\n';
        }
    }
    return 0;
}
