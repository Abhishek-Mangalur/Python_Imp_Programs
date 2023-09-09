file_name = input("Enter the file name: ")
fin = open(file_name,'r')
n = int(input("Enter the no. of lines to read: "))

for i in range(n):
    line = fin.readline()
word = input("Enter the word: ")
fin.seek(0)
fwords = fin.read()
print("No. of words", fwords.count(word))
fin.close()