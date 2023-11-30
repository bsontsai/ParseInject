import os
import subprocess
import Setup
import HTMLParser

# Run Setup.py
Setup

# Run code coverage
cwd = os.getcwd()
coco_dir = cwd + "\\src\\java\\coco\\coco"
os.chdir(coco_dir)
os.system("mvn clean cobertura:cobertura")

os.chdir(cwd)

# Run HTMLParser
HTMLParser