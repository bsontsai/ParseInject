#include <iostream>
#include <cstdlib> 
#include <ctime>

int main(int argc, char* argv[]) {
    srand(static_cast<unsigned int>(time(0))); // seed random number generator

    int n = atoi(argv[1]);

    // This is a double loop with O(n^2)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int a = 1;
        }
    }
    return 0;
}
