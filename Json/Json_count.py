#!/usr/bin/env python3
from sys import argv
import json

try:
    open(argv[1])
except:
    print(f"File '{argv[1]}' not found")
    exit()

RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

data=json.load(open(argv[1],'r'))
element_count=len(data)
print(f"{data}\n")
print("This JSON file contains "+RED+BOLD+f"{element_count}"+END+" elements")
