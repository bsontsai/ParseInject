import subprocess
import matplotlib.pyplot as plt
import os

cpp_file = "testprogram2.cpp"  # replace with needed .cpp file
gpp_path = "C:\\MinGW\\bin\\" # If G++ already installed and added to path, only keep 'g++'
output_name = "test.exe" # the name of the executable

def run_cpp_coverage(cpp_file):
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
            except:
                times_run = 0
            coverage_info[line_number] = times_run

    return coverage_info

if __name__ == '__main__':
    # coverage_info = run_cpp_coverage(cpp_file)
    # coverage_data = list(coverage_info.values())
    manual_data = [3, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973]
    manual_data_x = [1 * (i+1) for i in range(len(manual_data))]
    # map_data_x = [i+1 for i in range(len(coverage_data))]
    # plt.bar(map_data_x, coverage_data)
    plt.plot(manual_data_x, manual_data)
    # print(max(coverage_data))
    plt.show()



