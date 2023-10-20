import re

java_keywords = {
    "abstract": 0,
    "assert": 0,
    "boolean": 0,
    "break": 0,
    "byte": 0,
    "case": 0,
    "catch": 0,
    "char": 0,
    "class": 0,
    "const": 0,  # Not used, but reserved
    "continue": 0,
    "default": 0,
    "do": 0,
    "double": 0,
    "else": 0,
    "enum": 0,
    "extends": 0,
    "final": 0,
    "finally": 0,
    "float": 0,
    "for": 0,
    "if": 0,
    "goto": 0,  # Not used, but reserved
    "implements": 0,
    "import": 0,
    "instanceof": 0,
    "int": 0,
    "interface": 0,
    "long": 0,
    "native": 0,
    "new": 0,
    "package": 0,
    "private": 0,
    "protected": 0,
    "public": 0,
    "return": 0,
    "short": 0,
    "static": 0,
    "strictfp": 0,
    "super": 0,
    "switch": 0,
    "synchronized": 0,
    "this": 0,
    "throw": 0,
    "throws": 0,
    "transient": 0,
    "try": 0,
    "void": 0,
    "volatile": 0,
    "while": 0
}

java_operators = {
    "+": ["addition", 0],
    "-": ["subtraction", 0],
    "*": ["multiplication", 0],
    "/": ["division", 0],
    "%": ["modulus", 0],

    "++": ["increment", 0],
    "--": ["decrement", 0],
    
    "=": ["assignment", 0],
    "+=": ["addAndAssign", 0],
    "-=": ["subtractAndAssign", 0],
    "*=": ["multiplyAndAssign", 0],
    "/=": ["divideAndAssign", 0],
    "%=": ["modulusAndAssign", 0],
    
    "==": ["equalTo", 0],
    "!=": ["notEqualTo", 0],
    "<": ["lessThan", 0],
    ">": ["greaterThan", 0],
    "<=": ["lessThanOrEqual", 0],
    ">=": ["greaterThanOrEqual", 0],
    #ignore everything below here for now
    "&&": ["logicalAnd", 0],
    "||": ["logicalOr", 0],
    "!": ["logicalNot", 0],
    
    "&": ["bitwiseAnd", 0],
    "|": ["bitwiseOr", 0],
    "^": ["bitwiseXor", 0],
    "~": ["bitwiseNot", 0],
    "<<": ["leftShift", 0],
    ">>": ["rightShift", 0],
    ">>>": ["unsignedRightShift", 0],
    
    "? :": ["conditionalTernary", 0],
    "instanceof": ["instanceOf", 0],
    "new": ["objectCreation", 0],
    "->": ["lambdaExpression", 0],
}

func_calls = {}

infile_path = "C:\\Users\\benson\\Desktop\\school\\research\\ParseInject\\src\\java\\testInput.java"
outfile_path = "C:\\Users\\benson\\Desktop\\school\\research\\ParseInject\\src\\java\\testOutput.java"
runfile_path = "C:\\Users\\benson\\Desktop\\school\\research\\ParseInject\\src\\java\\Runner.java"


variables = []
output_lines = []
name_stack = []
#dictionary to specifically hold the code that run in each iteration of a for loop
loop_code = {}

def strip_strings(line):
    append = True
    modded_line = ""
    for char in line:
        if (char == "\\"):
            continue
        if (char == "\""):
            append = not append
            modded_line += "\""
            continue
        if (append):
            modded_line += char
    return modded_line

def get_var_name(arg):
    var_name = ""
    for part in name_stack:
        var_name += part + "_"
    return var_name + arg

def insert(op):
    var_name = get_var_name(java_operators[op][0] + str(java_operators[op][1]))
    variables.append(var_name)
    # print("var_name = " + var_name + ", for_control = " + str(for_control) + ", semicolon_counter = " + str(semicolon_counter))
    if ((for_control and semicolon_counter > 0) or (while_control and while_condition_start)): #add only if it is in between the first ; and )
        if (name_stack[-1] in loop_code.keys()):
            loop_code[name_stack[-1]].append(var_name + "++;\n")
        else:
            loop_code[name_stack[-1]] = [var_name + "++;\n"]
    else:
        output_lines.append(var_name + "++;\n")
    java_operators[op][1] += 1

def insert_func_call(func_name):
    if (func_name not in func_calls.keys()):
        func_calls[func_name] = 0
    var_name = get_var_name(func_name + str(func_calls[func_name]))
    variables.append(var_name)
    output_lines.append(var_name + "++;\n")
    func_calls[func_name] += 1

#open input file
infile = open(infile_path, "r")

infile_lines = infile.readlines()

for line in infile_lines:
    #strip strings and leading/trailing whitespaces
    modded_line = strip_strings(line).strip()
    tokens = modded_line.split()
    
    for_control = False
    semicolon_counter = 0
    while_control = False
    while_condition_start = False
    #used to detect function calls, assume there is no space between function name and starting parenthesis
    is_function = False
    func_name = ""
    check_token = False

    for token in tokens:
        if (token == "}"):
            if name_stack:
                #check if it marks the end of a for or while
                if ("for" in name_stack[-1] or "while" in name_stack[-1]):
                    #add the lines
                    for code in loop_code[name_stack[-1]]:
                        output_lines.append(code)
                    del loop_code[name_stack[-1]]
                name_stack.pop()

        #detect function calls
        # elif (re.match(r"[\s\S]+[(][\s\S]*", token)):
        #     #marks the start of a function
        #     is_function = True
        #     func_name = token[:token.find("(")]
        #     if (re.match(r"[\s\S]+[(][\s\S]*[)]", token)): #100% a function
        #         check_token = True
        # elif (is_function): #in or after parenthesis
        #     if (token == ")"):
        #         #check if next token is {
        #         check_token = True
        #     elif (check_token):
        #         if (token == "{"):
        #             #this is a function definition, push to var stack
        #             name_stack.append(func_name)
        #         else:
        #             #not a function definition, therefore a function call, make var and increment
        #             insert_func_call(func_name)
                
        #         is_function = False
        #         func_name = ""
        #         check_token = False


        elif (token in java_keywords.keys()):
            #only deal with for, while, and if for now
            if (token == "for" or token == "while" or token == "if"):
                #push to stack
                name_stack.append(token + str(java_keywords[token]))
                java_keywords[token] += 1
                if (token == "for"):
                    #activate for_control
                    for_control = True
                elif (token == "while"):
                    #activate while_control
                    while_control = True
        elif (token in java_operators.keys()):
            insert(token)
        else:
            #look through token two chars at a time
            if (len(token) > 1):
                pairs = [token[i:i+2] for i in range(0, len(token) - 1)]
                for pair in pairs:
                    if (pair in java_operators.keys()):
                        insert(pair)
                    else:
                        #check individual char
                        char = pair[0]
                        if (for_control):
                            if (char == ";"):
                                semicolon_counter += 1
                            elif (char == ")" and semicolon_counter == 2): #end of for()
                                for_control = False
                                semicolon_counter = 0
                        if (while_control):
                            if (char == "("):
                                while_condition_start = True
                            elif (char == ")"):
                                while_condition_start = False
                                while_control = False
                        if (char in java_keywords.keys()):
                            insert(char)
            #check last char
            char = token[-1]
            if (for_control):
                if (char == ";"):
                    semicolon_counter += 1
                elif (char == ")" and semicolon_counter == 2): #end of for()
                    for_control = False
                    semicolon_counter = 0
            if (while_control):
                if (char == "("):
                    while_condition_start = True
                elif (char == ")"):
                    while_condition_start = False
                    while_control = False
            if (char in java_keywords.keys()):
                insert(char)
            
    #check if still looking for next token to determine function call/function def
    if (is_function and check_token):
        #automatically a function call
        insert_func_call(func_name)
    #write original line
    output_lines.append(line)

#write to output file
outfile = open(outfile_path, "w")
outfile.write("public class testOutput {\n")
for var in variables:
    outfile.write("public static int " + var + " = 0;\n")
for line in output_lines:
    outfile.write(line)
outfile.write("}")

#generate run file
runfile = open(runfile_path, "w")
runfile.write("import java.util.ArrayList;\n"
               + "public class Runner {\n"
               + "    public static void main(String[] args) throws IllegalArgumentException, IllegalAccessException, NoSuchFieldException, SecurityException {\n"
               + "        testOutput test = new testOutput();\n"
               + "        ArrayList<String> varList = new ArrayList<>();\n"
               )
for var in variables:
    runfile.write("        varList.add(\"" + var + "\");\n")
runfile.write("        test.testInput();\n"
              + "        for (String var : varList) {\n"
              + "            System.out.println(var + \" = \" + testOutput.class.getField(var).get(testOutput.class));\n"
              + "        }\n"
              )


runfile.write("    }\n}")
