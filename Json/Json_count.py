#!/usr/bin/env python3
from sys import argv
import json

try:
    open(argv[1])
except:
    print(f"File '{argv[1]}' not found")
    exit()

data=json.load(open(argv[1],'r'))
element_count=len(data)
print(f"{data}\n")
print(f"This JSON file contains {element_count} elements")
