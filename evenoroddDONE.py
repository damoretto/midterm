#Problem 2: Even or Odd
#• Write a program that takes a positive or negative integer as input and determines whether it's even or odd
#• You can use any user interface that you like,but the user must be able to continuously test out integers
#• Make sure that you attempt to handle all/ some error cases
while(True):
    num = int(input("enter an integer: "))
    
    remainder = num%2
    
    if remainder > 0:
        print('this integer is odd!')
        
    if remainder == 0:
        print('this integer is even!')


#Remainder = Divide num by 2 with remainder symbol thing

#If remainder greater than 0 - print(“this integer is odd!”)
#If remainder = 0 - print(“this integer is even!”)

#Handle error cases for negative integers? Don't need to.
