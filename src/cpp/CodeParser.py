import re
import subprocess

prog_name = "testprogram"
pattern = r'(?<!/)(?<!\*)(?<!=)(?<!\+)(?<!\-)[+\-*/=](?!\*)(?!=)(?!\+)(?!\-)'
pattern = r'[+\-*/=](?!/)(?<!/)'
s = 'a = b + c - d * e / f; // This is a comment. a == b; /* comment */ a ** b;'

def count_operations(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    operations_count = []
    for line in lines:
        count = len(re.findall(pattern, line))
        operations_count.append(count)

    return operations_count

def compile_and_run(filename):
    result = subprocess.run(['g++', filename, '-o', './' + prog_name], stdout=subprocess.PIPE)
    if result.returncode != 0:
        print('Compilation failed')
        print(result.stdout.decode('utf-8'))
        return

    result = subprocess.run(['./' + prog_name], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))

if __name__ == '__main__':

    filename = './' + prog_name + '.cpp'  # replace with your filename
    operations_count = count_operations(filename)
    print(operations_count)
    # matches = re.findall(pattern, s)
    # print(matches)  # prints: ['=', '+', '-', '*', '/']
    # compile_and_run(filename)
    print("done")
