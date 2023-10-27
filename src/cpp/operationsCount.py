
import re

'''

Author: Dennis Hsieh

Identifies operations and number of time operations is done on each line. Operators are according to operators.txt
Also identifies the number of time certain keywords appears

TODO: combine function checking and name extraction
TODO: handle ternary operator
TODO: handle edge cases see desc for getOpsInString()

'''


'''
Reads all the operators according to operators.txt into a list
'''

operators = []

def getAllOperators():

    operators_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInjectCPP\operators.txt'
    operators_file = open(operators_path, 'r')

    operators_lines = operators_file.readlines()

    for line in operators_lines:

        op_and_name = line.split(',')
        op = op_and_name[0].strip()
        name = op_and_name[1].strip()
        operators.append(op)


'''
gets all the operators on this line
returns a dictionary
key: line number
value: dictionary of operators on the line where the key is the operator and value is the times it appeared
'''

def getOperatorsOnLine(line, line_counter, line_operator_dict, bracket_stack):
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
returns a dictionary of operators on string represented by line
key: operators:
value: occurrences 

will count operators in cases such as: srand(static_cast<unsigned int>(time(0)));
note this is legal: bool a = i < j > k;
'''

def getOpsInString(line):
    i = 0
    ops = {}
    while i < (len(line) - 1):
        char1 = line[i]
        if char1 == ' ':  # slight optimization
            i += 1
            continue
        char2 = line[i + 1]

        c = char1 + char2

        if c == '//':
            break

        elif c in operators:  ## if c is an operator
            i += 2  # we skip char 2 because it's already used

            try:
                ops[c] += 1
            except KeyError:
                ops[c] = 1

        elif c == '<<' or c == '>>':  ## special cases to take care of
            i += 1

        elif char1 in operators:  ## if char1 is an operator
            i += 1

            try:
                ops[char1] += 1
            except KeyError:
                ops[char1] = 1

        else:  # if c1 and char are not operators
            i += 1

    return ops

'''
list with all the special keywords we need to track
will add entire line to dictionary if line has for loop
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

                        special_dict[line_counter] = line
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


coverageInfo = {}

coverageInfo[1] = 1
coverageInfo[2] = 1
coverageInfo[3] = 1
coverageInfo[4] = 0
coverageInfo[5] = 1
coverageInfo[6] = 1
coverageInfo[7] = 1
coverageInfo[8] = 1
coverageInfo[9] = 0
coverageInfo[10] = 51
coverageInfo[11] = 5050
coverageInfo[12] = 5000
coverageInfo[13] = 0
coverageInfo[14] = 0
coverageInfo[15] = 2
coverageInfo[16] = 0

'''
gets the total times each operation is done
keys: operator
value: times done
'''

def getTotalOps(operatorsByLine, keywords_dict, coverageInfo):

    totalOps = {}

    assert(len(coverageInfo) == len(operatorsByLine))

    for line_num, times_ran in coverageInfo.items():

        if keywords_dict[line_num]: ## there's keyword on this line

            if str(keywords_dict[line_num]).find("for") > -1: ## for loop

                tokens = keywords_dict[line_num].split(';')

                ## form of: for (___;____;___)

                for i in range(3):

                    ops_in_token = getOpsInString(tokens[i])

                    if i == 0: # for (we are here; ___ ; ___)

                        for op, count in ops_in_token.items():

                            try:
                                totalOps[op] += (count * 1)
                            except KeyError:
                                totalOps[op] = (count * 1)
                    else:
                        for op, count in ops_in_token.items():

                            try:
                                totalOps[op] += (count * times_ran)
                            except KeyError:
                                totalOps[op] = (count * times_ran)


        else: ## regular operations

            for op, appearance in operatorsByLine[line_num].items():
                try:
                    totalOps[op] += appearance * times_ran
                except KeyError:
                    totalOps[op] = appearance * times_ran
    return totalOps

'''
reads in files
'''

line_operator_dict = {} ## each key is the line number, corresponds to a dictionary storing the operators
special_dict = {} ## each key is the line number, corresponds to a dictionary of any special operators like for
function_dict = {} ## each key is function name, corresponding to a tuple/length 2 list storing start and end of function

source_code_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInject\src\cpp\\testprogram3.cpp'
source_code_file = open(source_code_path, 'r')
source_code_lines = source_code_file.readlines()

for_control = False  # true if parser in for loop line
while_control = False  # true if parser in while loop line
do_while_control = False  # true if parser in do while loop
function_control = False # true if parser in function
bracket_stack = [] # stack for the brackets
func_name = "" #name of function
getAllOperators()

line_counter = 1

for line in source_code_lines:

    line.strip()

    line_operator_dict[line_counter] = dict()

    getOperatorsOnLine(line, line_counter, line_operator_dict, bracket_stack)

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


total_ops = getTotalOps(line_operator_dict, special_dict, coverageInfo)

print(total_ops)