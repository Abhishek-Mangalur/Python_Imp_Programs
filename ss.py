import difflib
def string_similarity(str1, str2):
    result = difflib.SequenceMatcher(a = str1.lower(), b = str2.lower())
    return result.ratio()

str1 = input("Enter the String1: ")
str2 = input("Enter the String2: ")
print("Original Strings:")
print(str1)
print(str2)
print("Similarity between two String is ", string_similarity(str1, str2))