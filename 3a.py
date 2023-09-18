alpha, uppercase, lowercase, digit, words = 0, 0, 0, 0, 0
str = input("Enter a Sentence: ")

for i in str:
    if i.isupper():
        uppercase = uppercase + 1
    elif i.islower():
        lowercase = lowercase + 1
    elif i.isdigit():
        digit = digit + 1
        
print("Uppercase letters: ", uppercase)
print("Lowercase letters: ", lowercase)
print("Total digits: ", digit)
print("Total words: ", len(str.split()))
 
