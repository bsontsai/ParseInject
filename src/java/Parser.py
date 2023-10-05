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

infile_path = "C:\\Users\\benson\\Desktop\\school\\research\\ParseInject\\src\\java\\testInput.java"
outfile_path = "C:\\Users\\benson\\Desktop\\school\\research\\ParseInject\\src\\java\\testOutput.java"

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

variable_declarations = []
output_lines = []
name_stack = []

#open input file
infile = open(infile_path, "r")

infile_lines = infile.readlines()

for line in infile_lines:
    #strip strings and leading/trailing whitespaces
    modded_line = strip_strings(line).strip()
    tokens = modded_line.split()
    for token in tokens:
        if (token == "}"):
            if name_stack:
                name_stack.pop()
            continue
        if (token in java_keywords.keys()):
            #only deal with for, while, and if for now
            if (token == "for" or token == "while" or token == "if"):
                #push to stack
                name_stack.append(token + str(java_keywords[token]))
                java_keywords[token] += 1
        elif (token in java_operators.keys()):
            var_name = get_var_name(java_operators[token][0] + str(java_operators[token][1]))
            variable_declarations.append(var_name)
            output_lines.append(var_name + "++;\n")
            java_operators[token][1] += 1
        else:
            #look through token two chars at a time
            pairs = [token[i:i+2] for i in range(0, len(token) - 1)]
            for pair in pairs:
                if (pair in java_operators.keys()):
                    var_name = get_var_name(java_operators[pair][0] + str(java_operators[pair][1]))
                    variable_declarations.append(var_name)
                    output_lines.append(var_name + "++;\n")
                    java_operators[pair][1] += 1
                else:
                    #check individual char
                    char = pair[0]
                    if (char in java_keywords.keys()):
                        print("found single: " + char)
                        var_name = get_var_name(java_operators[char][0] + str(java_operators[char][1]))
                        variable_declarations.append(var_name)
                        output_lines.append(var_name + "++;\n")
                        java_operators[char][1] += 1
            #check last char
            char = token[-1]
            if (char in java_keywords.keys()):
                var_name = get_var_name(java_operators[char][0] + str(java_operators[char][1]))
                variable_declarations.append(var_name)
                output_lines.append(var_name + "++;\n")
                java_operators[char][1] += 1
    
    #write original line
    output_lines.append(line)

#write to output file
outfile = open(outfile_path, "w")
for line in variable_declarations:
    outfile.write("static int " + line + " = 0;\n")
for line in output_lines:
    outfile.write(line)

