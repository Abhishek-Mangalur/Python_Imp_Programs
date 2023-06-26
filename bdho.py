import sys 
def num_to_dec(num_val,n,d):
    dec_val = 0
    count = 0
    digit = 0
    l = len(str(num_val))
    digit = num_val % 10
    while(num_val != 0 and digit <= d):
        dec_val = dec_val + digit * pow(n,count)
        num_val = num_val // 10
        digit = num_val % 10
        count += 1
    if(count == l):
        return dec_val
    else:
        print("Invalid input")   
        
def octal_to_hex(num_val):
    rem = num_val % 16
    ch = ""
    if(rem < 10):
        ch = rem
    if(rem == 10):
        ch = "A"
    if(rem == 11):
        ch = "B"
    if(rem == 12):
        ch = "C"
    if(rem == 13):
        ch = "D"
    if(rem == 14):
        ch = "E"
    if(rem == 15):
        ch = "F"
    if(num_val - rem != 0):
        return octal_to_hex(num_val // 16) + str(ch)
    else:
        return str(ch)

while(True):
    print("\n1. Binary to Decimal")
    print("2. Octal to Hexadecimal")
    print("3. Exit")
    
    ch = int(input("Enter your choice: "))
    if(ch == 1):
        num_val = int(input("Enter the Binary value: "))
        print("The decimal value of binary {} is {}".format(num_val, num_to_dec(num_val, 2, 1)))
    elif(ch == 2):
        num_val = int(input("Enter the Octal value: "))
        octalno = num_to_dec(num_val, 8, 7)
        if(octalno != None):
            print("The Hexadecimal value of octal value {} is {}".format(num_val, octal_to_hex(octalno)))
        else:
            print("Cannot be converted")
    else:
        print("Thank You")
        sys.exit()