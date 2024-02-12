import subprocess
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os
import time

cpp_file = "testprogram.cpp"  # replace with needed .cpp file
gpp_path = "C:\\MinGW\\bin\\" # If G++ already installed and added to path, only keep 'g++'
output_name = "test.exe" # the name of the executable

def record_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {func.__name__} is {end_time - start_time} seconds")
        return result
    # if need to record runtime, add @record_runtime in front of functions
    return wrapper

def check_regression(x, y, reg_type):
    # Perform linear regression
    slope, intercept, r_val, p_val, std_err = stats.linregress(x, y)
    line_err = {'reg': "n", 'value':r_val**2}

    # Perform quadratic regression
    quad_y = np.sqrt(y)
    slope, intercept, r_val, p_val, std_err = stats.linregress(x, quad_y)
    quad_err = {'reg': "n^2", 'value': r_val ** 2}

    # Perform cubic regression
    cub_y = np.cbrt(y)
    slope, intercept, r_val, p_val, std_err = stats.linregress(x, cub_y)
    cub_err = {'reg': "n^3", 'value': r_val ** 2}

    # Perform exponential regression
    expo2_y = np.log2(y)
    slope, intercept, r_val, p_val, std_err = stats.linregress(x, expo2_y)
    expo_err = {'reg': "2^n", 'value': r_val ** 2}

    # Perform inverse regression
    inver_x = np.reciprocal(x)
    slope, intercept, r_val, p_val, std_err = stats.linregress(inver_x, y)
    inver_err = {'reg': "1/n", 'value': r_val ** 2}

    error = list([line_err, quad_err, cub_err, expo_err, inver_err])

    biggest = 0
    pattern = "none"
    for item in error:
        print(item.get('reg') + ": "+ str(item.get('value')))
        if item.get('value') > biggest:
            pattern = item.get('reg')
            biggest = item.get('value')

    print("pattern is " + pattern)
    print("You asked: is the pattern "+reg_type)
    if pattern is reg_type:
        print("Yes, it is")
    else:
        print("No, it is not")

def prepare_cpp_coverage(cpp_file):
    code_command = f"chcp 65001"
    subprocess.call(code_command, shell=True)
    # Turn GBK to UTF-8
    # Remove or comment out this line if running on US computer.

    test_command = f"chdir"
    # subprocess.call(test_command, shell=True)
    # Test command, remove if not running on Windows

    test_command = f"ls"
    # subprocess.call(test_command, shell=True)
    # Would not work on Windows

    test_command = f"dir"
    # subprocess.call(test_command, shell=True)
    # Equivalent of ls on Linux

    test_command = gpp_path + f"g++ --version"
    # subprocess.call(test_command, shell=True)
    # Is gcc installed?

    # Compile the .cpp file with g++
    compile_command = gpp_path + f"g++ -fprofile-arcs -ftest-coverage -O0 -o {output_name} {cpp_file}"
    subprocess.call(compile_command, shell=True)

    test_command = f"dir"
    # subprocess.call(test_command, shell=True)

def run_cpp_coverage(cpp_file, input_val):

    # Run the compiled file
    run_command = f"{output_name} {str(input_val)}"
    subprocess.call(run_command, shell=True)

    # Run gcov on the .cpp file
    gcov_command = gpp_path + f"gcov {cpp_file}"
    subprocess.call(gcov_command, shell=True)

    # Parse the .gcov file for coverage info
    coverage_info = {}
    with open(f"{cpp_file}.gcov", 'r') as f:
        for line in f:
            if line.startswith('    #####'):
                continue
            parts = line.split(':')
            line_number = int(parts[1])
            times_run = 0
            try:
                times_run = int(parts[0].strip())
            except:
                times_run = 0
            coverage_info[line_number] = times_run

    return coverage_info

if __name__ == '__main__':
    test_max = 25
    prepare_cpp_coverage(cpp_file)
    run_data = []
    accu_data = 0
    for n in range(test_max):
        # Running it test_max times
        coverage_info = run_cpp_coverage(cpp_file, n)
        coverage_data = list(coverage_info.values())
        del coverage_data[-1]
        max_runtime = max(coverage_data) - accu_data
        accu_data = accu_data + max_runtime
        run_data.append(max_runtime)
        print("ran " + str(n) + " times, got " + str(max_runtime))
    x_data = [i+1 for i in range(len(run_data))]
    check_regression(x_data, run_data, "n")
    plt.plot(x_data, run_data)
    plt.show()

    #manual_data = [3, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973, 3193, 5167, 8361, 13529, 21891, 35421, 57313, 92735, 150049, 242785, 2692537, 29860703, 331160281, 3672623805]
    #manual_data_capped = [3, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973, 3193, 5167, 8361, 13529, 21891, 35421, 57313, 92735, 150049, 242785]
    #manual_data_time = [2.21, 1.61, 1.68, 2.69, 1.81, 1.70, 1.78, 2.26, 3.03, 2.03, 1.75, 2.49, 3.02, 2.41, 3.10, 6.32, 3.55, 1.61, 1.63, 5.21, 1.74, 2.82, 1.76, 1.74, 3.12, 4.74, 4.31, 5.12, 9.39]
    # manual_data_x = [1 * (i+1) for i in range(len(manual_data))]
    #manual_data_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 30, 35, 40, 45]
    #manual_data_x_capped = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    #map_data_x = [i+1 for i in range(len(coverage_data))]
    #plt.bar(map_data_x, coverage_data)
    #plt.plot(manual_data_x_capped, manual_data_capped)
    # print(max(coverage_data))
    #check_regression(manual_data_x_capped, manual_data_capped, "2^n")



