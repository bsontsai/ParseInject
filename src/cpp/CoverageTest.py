import subprocess
import matplotlib.pyplot as plt
import os

cpp_file = "testprogram2.cpp"  # replace with needed .cpp file
gpp_path = "C:\\MinGW\\bin\\" # If G++ already installed and added to path, only keep 'g++'
output_name = "test.exe" # the name of the executable

"""
Semiauto Runtime Analyzer through gCov Coverage Testing
by Jiarui Xie

Requirements: 
This approach depends on setting up the environment
gcc package is installed (no need to add to path), including g++ and gcov

Descriptinon:
Code coverage tests tells us which part of the code has been executed and how many times.
To properly test code coverage, optimization should be disabled, hence the flag -O0
I believe we can take advantage of this debug tool, instead of destructively inserting probes as counters.
The returned gcov file has the following format each line:
# of times this line ran : line # : the original line
We will split each line by ':', and that gives us the number of times this line ran.
Save such data, change the N, then compile and run the test again.
With increase in N, there's also increase in the number of run times
And thus we have a runtimes v N function at our hands, the only thing left is regression.

Highlights:
Works on manually changing the number N, no optimazation nor sudden drops observed when increasing N
Works on recursive functions

To-do:
1. The code automatically compiles C program, grep results and parse it. But manual change of N should be added too.
2. Should number of operations each line be counted? Theoretically they should be scalar but not sure.
3. Regression based on the given data.
4. Potentially: segment the array into different parts to give students feeback on which part went overboard.
"""

# helper function to record run time
# not to be confused with runtime.
def record_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {func.__name__} is {end_time - start_time} seconds")
        return result
    # if need to record runtime, add @record_runtime in front of functions
    return wrapper

# does the code coverage.
def run_cpp_coverage(cpp_file):
    " start of testing section "
    # Remove test commands for official use
    
    code_command = f"chcp 65001"
    subprocess.call(code_command, shell=True)
    # Turn GBK to UTF-8
    # comment out this the call if running on US computer.
    # Or if the computer is already running on English Windows system

    test_command = f"chdir"
    # subprocess.call(test_command, shell=True)
    # Test command to see if the code gets current directory, 
    # remove if not running on Windows. Linux equivalent: pwd

    test_command = f"ls"
    # subprocess.call(test_command, shell=True)
    # Would not work on Windows system.

    test_command = f"dir"
    # subprocess.call(test_command, shell=True)
    # Equivalent of ls on Linux,
    # uncomment if need to see if pycharm have writing permissions
    # compare directory now with after compilation.

    test_command = gpp_path + f"g++ --version"
    # subprocess.call(test_command, shell=True)
    # Is gcc installed?
    # If g++ is added to PATH, then the app_path is not needed
    
    " end of testing section "
    
    # Compile the .cpp file with g++
    compile_command = gpp_path + f"g++ -fprofile-arcs -ftest-coverage -O0 -o {output_name} {cpp_file}"
    subprocess.call(compile_command, shell=True)

    test_command = f"dir"
    # subprocess.call(test_command, shell=True)
    # used to check if excuatble is created, if not, check write premission.

    # Run the compiled file
    run_command = f"{output_name}"
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
                # When the line isn't run it wouldn't show as 0 but as -
            except:
                times_run = 0
            coverage_info[line_number] = times_run

    return coverage_info

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

if __name__ == '__main__':
    # Get the coverage info by parsing gcov files
    coverage_info = run_cpp_coverage(cpp_file)
    coverage_data = list(coverage_info.values())

    # Create an X axis
    map_data_x = [i+1 for i in range(len(coverage_data))]
    print(coverage_data)

    # Show the bar graph
    plt.bar(map_data_x, coverage_data)
    plt.show()

    # This graph is NOT a runtime v N graph, but a heatmap of the current N
    # To show runtime v N currently, manually fill out the data
    # examples are in discord.
    # manual_data = [3, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973]
    # manual_data_x = [1 * (i+1) for i in range(len(manual_data))]
    check_regression(manual_data_x, manual_data, "n^2")
    # plt.plot(manual_data_x, manual_data)
    # plt.show()
    
    



