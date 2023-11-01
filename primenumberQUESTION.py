#Problem 6: Check for Prime Numbers 
#• Create a program that checks if a given positive or negative integer is prime or not
#– Hint: A prime number divides by itself and 1 only
#– Examples:
#6 is not a prime number, since it is divisible by 2 and 3
#17 is a prime number
#121 is not a prime number, since it is divisible by 11 (twice!)
#• You can use any user interface that you like, but the user must be able to continuously enter numbers to be checked
#• Make sure that you attempt to handle all/some error cases

while(True):
    num = int(input('enter an integer: '))
    
    if num == 1:
        print('This is a prime number!')
        continue
    if num == 2:
        print('This is a prime number!')
        continue
    if num == 3:
        print('This is a prime number!')
        continue
    if num == 5:
        print('This is a prime number!')
        continue  
    if num == 7:
        print('This is a prime number!')
        continue
        
    if num%2 == 0:
        print('This is not a prime number!')
        continue
    if num%3 == 0:
        print('This is not a prime number!')
        continue
    if num%4 == 0:
        print('This is not a prime number!')
        continue
    if num%5 == 0:
        print('This is not a prime number!')
        continue
    if num%6 == 0:
        print('This is not a prime number!')
        continue
    if num%7 == 0:
        print('This is not a prime number!')
        continue
    if num%8 == 0:
        print('This is not a prime number!')
        continue
    if num%9 == 0:
        print('This is not a prime number!')
        continue
    if num%11 == 0:
        print('This is not a prime number!')
        continue
#need to handle prime numbers multipied by itself
   
        
    else:
        print('This is a prime number!')
