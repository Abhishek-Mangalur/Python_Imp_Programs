import re

fin = open("file1.txt",'r')
lines = fin.read()
regex = re.compile(r'([A-Xa-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
Nregex = re.compile(r'\+[9][1]\d{10}')

for i in re.finditer(regex, lines):
    print(i.group())
    
for j in re.finditer(Nregex, lines):
    print(j.group())