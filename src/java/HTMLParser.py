# import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(tag, attrs):
#         print("Encountered a start tag:", tag)

#     def handle_endtag(tag):
#         print("Encountered an end tag :", tag)

#     def handle_data(data):
#         print("Encountered some data  :", data)

# parser = MyHTMLParser()
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

filename = "SampleInput"

infile = open("src\\java\\coco\\coco\\target\\site\\cobertura\\com.example." + filename + ".html", "r")
infile_lines = infile.readlines()
while (not infile_lines[0] == "</table>\n"):
    infile_lines.pop(0);
while (not infile_lines[-1] == "</table>\n"):
    infile_lines.pop(-1)
data = []
for line in infile_lines:
    # print(line)
    if (("numLine" in line and "nbHits" in line) or ("numLineCover" in line and "nbHitsCovered" in line)):
        nbsp_indexs = list(find_all(line, "&nbsp"))
        # first one is line number, second one is times executed
        # first
        index = nbsp_indexs[0]
        while (line[index] != ";"):
            index += 1
        index += 1
        end_index = index
        while (line[end_index] != "<"):
            end_index += 1
        line_num = line[index:end_index]
        # print("line_num = " + str(line_num))
        # second
        index = nbsp_indexs[1]
        while (line[index] != ";"):
            index += 1
        index += 1
        end_index = index
        while (line[end_index] != "<"):
            end_index += 1
        executions = line[index:end_index]
        if executions == "":
            executions = "0"
        data.append(line_num + ":" + executions + ":")


print(data)
source = open("src\\java\\coco\\coco\\src\\main\\java\\com\\example\\" + filename + ".java", "r")
source_lines = source.readlines()

report_file = open("src\\java\\report.txt", "w")
i = 0
for line in source_lines:
    report_file.write(data[i] + line)
    i += 1