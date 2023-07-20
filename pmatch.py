import re

text_search = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789
Hi HiHi Metacharacters needed to be escaped:.^*$\+?[]|()rstforum.net
123-456-7891 100-234-5679 1w2-45y-6789 192.168.120.12 192.168.120.13
1.1.1.1 22.22.22.22 100.100.100.100 Mr.Gupta Mr.Kaushik Ms.Swati Mrs.Bose Mr.T'''

pattern = re.compile(r'\d{1,3}\-\d{1,3}\-\d{1,4}')
matches = pattern.finditer(text_search)

print("Using Regular Expression")
for match in matches:
    print(match.group())
    
def isphonenumber():
    ss = text_search.split()
    pat_mat = list()
    
    for i in ss:
        if len(i) == 12 and i[3] == '-' and i[7] == '-':
            pat_mat.append(i)
            
    for i in pat_mat:
        tran = i.translate({ord('-'):None})
        if tran.isdigit():
            print(i)
            
print("Without using Regular Expression")
isphonenumber()
