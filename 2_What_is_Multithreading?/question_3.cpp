/*
Question: OpenMP (Open Multi-Processing) is a popular API for concurrent programming in C++. Write a C++ function to compute the sum of the first N natural numbers. Measure runtime with and without OpenMP parallelization.

Setup for cpp script (macOS):
1. Install libomp via Homebrew:
    brew install libomp
2. Compile and run with the following command:
    g++ -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib -lomp -o solution question_3.cpp && ./solution

Note: The '-Xpreprocessor -fopenmp' flags are required on macOS because Apple's Clang does not natively support OpenMP. 
The '-I' and '-L' flags point to the libomp include and library directories installed by Homebrew.

*/

#include <iostream>
#include <ctime>
#include <omp.h>

int COUNT = 1000000000;

void single_thread_sum(long N) {
    double start = omp_get_wtime();
    long sum = 0;
    for (long i = 1; i <= N; ++i) {
        sum += i;
    }
    double end = omp_get_wtime();

    std::cout << "Time taken without OpenMP: " << end - start << " seconds" << std::endl;
}

void multi_thread_sum(long N) {
    double start = omp_get_wtime();
    long sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for (long i = 1; i <= N; ++i) {
        sum += i;
    }
    double end = omp_get_wtime();

    std::cout << "Time taken with OpenMP: " << end - start << " seconds" << std::endl;
}

int main() {
    single_thread_sum(COUNT);
    multi_thread_sum(COUNT);
    return 0;
}
