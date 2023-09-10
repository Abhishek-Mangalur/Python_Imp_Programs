class A:
    def __init__(self,s):
        self.s = s
        
    def palindrome(self):
        rev = self.s[::-1]
        if rev == self.s:
            print("It's a Palindrome")
        else:
            print("It's not a Palindrome!")
            
class B(A):
    '''def __init__(self,s):
        self.s = s'''
        
    def palindrome(self):
        temp = self.s
        rev = 0
        count = 0
        while self.s != 0:
            rem = self.s % 10
            rev = rev * 10 + rem
            self.s = self.s // 10
            
        if temp == rev:
            print("It's a Palindrome")
        else:
            print("It's not a Palindrome!")
            
a = A(input("Enter the String: "))
b = B(int(input("Enter the no.: ")))
a.palindrome()
b.palindrome()