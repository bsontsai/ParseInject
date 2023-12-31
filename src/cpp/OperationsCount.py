
import re

'''

Author: Dennis Hsieh

Identifies operations and number of time operations is done on each line. Operators are according to operators.txt
Also identifies the number of time certain keywords appears

TODO: combine function checking an name extraction

'''


'''
Reads all the operators according to operators.txt into a list
'''

operators_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInjectCPP\operators.txt'
operators_file = open(operators_path, 'r')

operators_lines = operators_file.readlines()

operators = [] ## operator stores all the operators

for line in operators_lines:

    op_and_name = line.split(',')
    op = op_and_name[0].strip()
    name = op_and_name[1].strip()
    operators.append(op)


'''
'''

def getOperators(line, line_counter, line_operator_dict, bracket_stack):
    i = 0
    while i < (len(line) - 1):
        char1 = line[i]
        if char1 == ' ': # slight optimization
            i += 1
            continue
        char2 = line[i + 1]

        c = char1 + char2

        if c == '//':
            break

        elif c in operators: ## if c is an operator
            i += 2 # we skip char 2 because it's already used

            try:
                line_operator_dict[line_counter][c] += 1
            except KeyError:
                line_operator_dict[line_counter][c] = 1

        elif c == '<<' or c == '>>': ## special cases to take care of
            i += 1

        elif char1 in operators: ## if char1 is an operator
            i += 1

            try:
                line_operator_dict[line_counter][char1] += 1
            except KeyError:
                line_operator_dict[line_counter][char1] = 1

        else: # if c1 and char are not operators

            # if bracket stack is not empty, we are in a function, we then push when we see { and pop when we see }
            if bracket_stack:
                if char1 == '{':
                    bracket_stack.append('{')
                elif char1 == '}':
                    bracket_stack.pop()

            i += 1


'''
list with all the special keywords we need to track
'''

keywords = ['for', '?', '#include']


def getKeywords(line, line_counter, special_dict):
    # check if there are keywords in this line
    for keyword in keywords:
        if keyword in line:

            if keyword == 'for':
                location = line.find(keyword)  # find location of for

                '''
                checks if it is in the form:
                for(...;...;...) or
                for (...;...;...)
                '''

                try:
                    if line[location + 3] == '(' or line[location + 4] == '(':

                        try:
                            special_dict[line_counter][keyword] += 1
                        except KeyError:
                            special_dict[line_counter][keyword] = 1
                except:
                    continue
            else:

                try:
                    special_dict[line_counter][keyword] += 1
                except KeyError:
                    special_dict[line_counter][keyword] = 1


'''
matches function declarations. does not handle trailing return
steps
1. uses regex
2. [\:0-9a-zA-Z\[\]\*\&]+ attempts to match return type 
3. [ \*]+ attempts to match the space or pointer between return type and function name
4. [0-9a-zA-Z_]+ attempts to match function name
5. [ ]* attempts to match space that may or may not exists between function name and left parenthesis
6. \( matches left parenthesis
7. [\*\&\:0-9a-zA-Z_,=\[\] ]* attempts to match parameter list
8. \) attempts to match right parenthesis
9. [a-z ]* attempts to match something like noexcept
10.\{\n end of function declaration

returns true if line matches function false other wise.
works on:

int main(int a) {
float[] try_this(int c, Temp t) {
myVar try_that(float[] arr, int a) {
int f2(std::string str) noexcept {
void duplicate (int& a, int& b, int& c) {
int * ptr(int* a, int * b){
int divide (int a, int b=2) {
int main() {
'''

return_keywords = ['void', 'int', 'double', 'float', 'auto']

def matchFunction(line):

    regex = "([\:0-9a-zA-Z\[\]\*]+[ \*\&]+[0-9a-zA-Z_]+[ ]*\([\*\&\:0-9a-zA-Z_,=\[\] ]*\)[a-z ]*\{\n)"
    pattern = re.compile(regex)

    #print("matching" + line)

    match = pattern.fullmatch(line)

    #print(match)

    return not match==None

'''
extract name of function
'''

def extractFuncName(line):

    regex = "([0-9a-zA-Z_]+[ ]*\()"
    pattern = re.compile(regex)

    match = pattern.search(line)

    return match



'''
reads in files
'''

line_operator_dict = {} ## each key is the line number, corresponds to a dictionary storing the operators
special_dict = {} ## each key is the line number, corresponds to a dictionary of any special operators like for
function_dict = {} ## each key is function name, corresponding to a tuple/length 2 list storing start and end of function

source_code_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInject\src\cpp\\testprogram2.cpp'
source_code_file = open(source_code_path, 'r')
source_code_lines = source_code_file.readlines()

for_control = False  # true if parser in for loop line
while_control = False  # true if parser in while loop line
do_while_control = False  # true if parser in do while loop
function_control = False # true if parser in function
bracket_stack = [] # stack for the brackets
func_name = "" #name of function

line_counter = 1

for line in source_code_lines:

    line.strip()

    line_operator_dict[line_counter] = dict()

    getOperators(line, line_counter, line_operator_dict, bracket_stack)

    ### check for any special operators

    special_dict[line_counter] = dict()

    getKeywords(line, line_counter, special_dict)

    ## tracks if we are in a function or not
    if not function_control: ## we are not in a function
        function_control = matchFunction(line)
        if function_control: # we just entered a function
            func_name = extractFuncName(line)
            bracket_stack.append('{')
            function_dict[func_name] = [line_counter, 0]
    else: ## we are in a function
        if len(bracket_stack) == 0: # stack is empty so we are out of the function
            function_control = False
            function_dict[func_name][1] = line_counter




    line_counter += 1


'''
prints out line number and corresponding dictionary with the operations on that line and the 
number of times such operations were done
'''
print('Operations')
for key, value in line_operator_dict.items():
    print(key)
    print(value)

'''
prints out line number and corresponding dictionary with the special keywords on that line and the 
number of times such keywords appear 
'''
print('Keywords')
for key, value in special_dict.items():
    print(key)
    print(value)

'''
prints out functions names and corresponding lines that functions span
'''
print('Functions')
for key, value in function_dict.items():
    print(key)
    print(value)