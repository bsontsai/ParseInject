'''

note: currently does not handle bit shift

'''

'''
Extracts cpp operators and stores them in a fictionary called operators that count their occurrence
ex: '=': 'equals'
'''

operators_count = {} # counts occurrence  of a particular operator
operators_name = {} # matches the operator and its name

operators_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInjectCPP\operators.txt'
operators_file = open(operators_path, 'r')

operators_lines = operators_file.readlines()

for line in operators_lines:

    op_and_name = line.split(',')
    op = op_and_name[0].strip()
    name = op_and_name[1].strip()
    operators_name[op] = name
    operators_count[op] = 0

'''
Extract cpp keywords and stores them in a dictionary
ex: 'new'
'''

keywords = {}

keywords_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInjectCPP\keywords.txt'
keywords_file =open(keywords_path, 'r')

keywords_lines = keywords_file.readlines()


for line in keywords_lines:

    keywords[line.strip()] = 0


var_stack = []

'''
does the reading and injecting
'''


source_code_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInjectCPP\doWhileTest.txt'
source_code_file = open(source_code_path, 'r')
source_code_lines = source_code_file.readlines()

static_declaration = []
lines_to_inject = []

append_in_for = []
append_in_while = []

for_control = False  # true if parser in for loop line
while_control = False  # true if parser in while loop line
do_while_control = False  # true if parser in do while loop

for line in source_code_lines:

    line.strip()

    tokens = line.split(' ')

    for_control = False
    while_control = False

    #print(line)

    # 3 cases for loops
    # 1: we just exited a while loop so we append in line after while loop statement
    if not while_control and not do_while_control and len(append_in_while) != 0:
        lines_to_inject += append_in_while
        append_in_while = []

    # 2: we just exited a for loop so we appen in for

    if not for_control and len(append_in_for) != 0:
        lines_to_inject += append_in_for
        append_in_for = []

    # 3: we just exited a do while loop so we append in line before while loop statement
    print(while_control)
    print(do_while_control)
    print(len(append_in_while))

    if  (not while_control) and do_while_control and len(append_in_while) != 0:


        for l in append_in_while:
            lines_to_inject.insert(len(lines_to_inject) - 1, l)

        append_in_while = []
        do_while_control = False



    for t in tokens:

        t = t.strip()

        if len(t) == 0: #slight optimization to skip empty lines
            continue

        loop_counter = 0

        # case with keywords (for and while loops)
        if t in keywords.keys():
            #print(f'found keyword {t} in code')
            var_stack.append(keywords[t])
            keywords[t] += 1
            if t == 'for':
                for_control = True
            elif t == 'while':
                while_control = True
            elif t == 'do':
                do_while_control = True



        # operators
        else:
            if for_control: # we are in a for loop

                if t in operators_name.keys(): # found operator

                    if t in operators_name.keys():
                        #print(f'found operator {t} in code')

                        # assignment is special case:
                        if t == '=':
                            static_declaration.append(
                                f"int {operators_name[t] + str(operators_count[t])} = 0;\n")  # add counter
                            lines_to_inject.append(f"{operators_name[t] + str(operators_count[t])}++;\n")  # increment
                            operators_count[t] += 1  # increase count for this operator

                        else:
                            static_declaration.append(
                                f"int {operators_name[t] + str(operators_count[t])} = 0;\n")  # add counter
                            append_in_for.append(f"{operators_name[t] + str(operators_count[t])}++;\n")  # increment
                            operators_count[t] += 1  # increase count for this operator

                    ## cheating right now for checking increament and decreament
                else: # when token is in form {t}++ and {t}--
                    if "--" in t:
                        #print(f'found operator -- in code {t}')
                        static_declaration.append(
                            f"int {operators_name['--'] + str(operators_count['--'])} = 0;\n")  # add counter
                        append_in_for.append(
                            f"{operators_name['--'] + str(operators_count['--'])}++;\n")  # increment
                        operators_count['--'] += 1  # increase count for this operator

                    elif "++" in t:
                        #print(f'found operator ++ in code {t}')
                        static_declaration.append(
                            f"int {operators_name['++'] + str(operators_count['++'])} = 0;\n")  # add counter
                        append_in_for.append(
                            f"{operators_name['++'] + str(operators_count['++'])}++;\n")  # increment
                        operators_count['++'] += 1  # increase count for this operator
                if t == '{': # end of for loop
                    for_control = False
                    #print('for control now false')
            elif while_control:
                #print(t)
                if t in operators_name.keys():
                    print(f'found operator {t} in code')

                    static_declaration.append(f"int {operators_name[t] + str(operators_count[t])} = 0;\n") # add counter
                    append_in_while.append(f"{operators_name[t] + str(operators_count[t])}++;\n") # increment
                    operators_count[t] += 1 # increase count for this operator

                ## cheating right now for checking increament and decreament
                else:
                    if '--' in t:
                        #print(f'found operator -- in code {t}')
                        static_declaration.append(
                            f"int {operators_name['--'] + str(operators_count['--'])} = 0;\n")  # add counter
                        append_in_while.append(f"{operators_name['--'] + str(operators_count['--'])}++;\n")  # increment
                        operators_count['--'] += 1  # increase count for this operator

                    elif '++' in t:
                        #print(f'found operator ++ in code {t}')
                        static_declaration.append(
                            f"int {operators_name['++'] + str(operators_count['++'])} = 0;\n")  # add counter
                        append_in_while.append(f"{operators_name['++'] + str(operators_count['++'])}++;\n")  # increment
                        operators_count['++'] += 1  # increase count for this operator

                if t == '{':
                    while_control = False

            else: # we are not on a line in a for loop
                if t in operators_name.keys():
                    #print(f'found operator {t} in code')

                    static_declaration.append(f"int {operators_name[t] + str(operators_count[t])} = 0;\n") # add counter
                    lines_to_inject.append(f"{operators_name[t] + str(operators_count[t])}++;\n") # increment
                    operators_count[t] += 1 # increase count for this operator

                ## cheating right now for checking increament and decreament
                else:
                    if '--' in t:
                        #print(f'found operator -- in code {t}')
                        static_declaration.append(
                            f"int {operators_name['--'] + str(operators_count['--'])} = 0;\n")  # add counter
                        lines_to_inject.append(f"{operators_name['--'] + str(operators_count['--'])}++;\n")  # increment
                        operators_count['--'] += 1  # increase count for this operator

                    elif '++' in t:
                        #print(f'found operator ++ in code {t}')
                        static_declaration.append(
                            f"int {operators_name['++'] + str(operators_count['++'])} = 0;\n")  # add counter
                        lines_to_inject.append(f"{operators_name['++'] + str(operators_count['++'])}++;\n")  # increment
                        operators_count['++'] += 1  # increase count for this operator

    lines_to_inject.append(line)



### writing outcome

f = open("outputTest.txt", "w")


for var in static_declaration:
    f.write(var)

for line in lines_to_inject:
    f.write(line)





















