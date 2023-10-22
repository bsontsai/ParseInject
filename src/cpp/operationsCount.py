
'''

Author: Dennis Hsieh

Identifies operations and number of time operations is done on each line. Operators are according to operators.txt
Also identifies the number of time certain keywords appears

'''

'''
list with all the special keywords we need to track
'''

keywords = ['for', '?', '#include']


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
reads in files
'''

line_operator_dict = {} ## each key is the line number, corresponds to a dictionary storing the operators
special_dict = {} ## each key is the line number, corresponds to a dictionary of any special operators like for

source_code_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInject\src\cpp\\testprogram.cpp'
source_code_file = open(source_code_path, 'r')
source_code_lines = source_code_file.readlines()

for_control = False  # true if parser in for loop line
while_control = False  # true if parser in while loop line
do_while_control = False  # true if parser in do while loop

line_counter = 1

for line in source_code_lines:

    line.strip()

    char1 = ''
    char2 = ''

    i = 0

    line_operator_dict[line_counter] = dict()

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

        elif char1 in operators: ## if c1 is an operator
            i += 1

            try:
                line_operator_dict[line_counter][char1] += 1
            except KeyError:
                line_operator_dict[line_counter][char1] = 1

        else: # if c1 and char are not operators
            i += 1

    ### check for any special operators

    special_dict[line_counter] = dict()

    # check if there are keywords in this line
    for keyword in keywords:
        if keyword in line:


            if keyword == 'for':
                location = line.find(keyword) # find location of for

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