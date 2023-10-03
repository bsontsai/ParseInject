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


source_code_path = 'C:\Dennis\Purdue\Junior Year\Algorithm Analysis\ParseInjectCPP\inputTest.txt'
source_code_file = open(source_code_path, 'r')
source_code_lines = source_code_file.readlines()

static_declaration = []
lines_to_inject = []

for line in source_code_lines:

    line.strip()

    tokens = line.split(' ')

    for t in tokens:
        t.strip()

        # case with keywords (for and while loops)
        if t in keywords.keys():
            print(f'found keyword {t} in code')
            var_stack.append(keywords[t])
            keywords[t] += 1



        # operators
        else:
            if t in operators_name.keys():
                print(f'found operator {t} in code')

                static_declaration.append(f"int {operators_name[t] + str(operators_count[t])} = 0;\n") # add counter
                lines_to_inject.append(f"{operators_name[t] + str(operators_count[t])}++;\n") # increment
                operators_count[t] += 1 # increase count for this operator

            ## cheeting right now for checking increament and decreament
            else:
                if '--' in t:
                    print(f'found operator -- in code {t}')
                    static_declaration.append(
                        f"int {operators_name['--'] + str(operators_count['--'])} = 0;\n")  # add counter
                    lines_to_inject.append(f"{operators_name['--'] + str(operators_count['--'])}++;\n")  # increment
                    operators_count['--'] += 1  # increase count for this operator

                elif '++' in t:
                    print(f'found operator ++ in code {t}')
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





















