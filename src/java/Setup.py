import os

def main():
    print("Running Setup.py...\n")
    # get test cases
    testcasesfile = open("src\\java\\testcases.txt", "r")
    testcases = []
    for line in testcasesfile.readlines():
        testcases.append(line.strip())

    # open test file
    testfile = open("src\\java\\coco\\coco\\src\\test\\java\\com\\example\\TestSampleInput.java", "w")
    testfile.write("package com.example;\n\nimport org.junit.Test;\n\npublic class TestSampleInput {\n")
                    
    # go through sourcecode directory
    for filename in os.listdir("src\\java\\sourcecode"):
        sourcefile = open("src\\java\\sourcecode\\" + filename, "r")
        sourcefilelines = sourcefile.readlines()
        classname = filename.split(".")[0]
        dupcount = 0
        for test in testcases:
            # generate dup file
            dupcount += 1
            dupname = classname + str(dupcount)
            dupfile = open("src\\java\\coco\\coco\\src\\main\\java\\com\\example\\" + dupname + ".java", "w")
            # write to dup file
            dupfile.write("package com.example;\n")
            for line in sourcefilelines:
                dupfile.write(line.replace(classname, dupname))
            dupfile.close()
            # generate test case
            testfile.write("\t@Test\n\tpublic void test" + dupname + "() {\n")
            testfile.write("\t\t" + dupname + " si = new " + dupname + "();\n")
            testfile.write("\t\tsi.test(" + str(test) + ");\n\t}\n\n")
            dupfile.close()

    testfile.write("}")
    testfile.close()

if __name__ == "__main__":
    main()