#Problem 11: Print a Pattern
#• Write a program that prints a simple pattern using loops, such as a triangle or a square. You
#need to allow the user to pick between at least two different patterns and to select the character that is used for printing that pattern.
#• You can use any user interface that you like, but the user must be able to continuously choose their pattern type and the printable character to be used

while(True):
    
    pattern = str(input('pick a pattern (square or triangle) '))
    pattern = pattern.lower()
    
    char = str(input('pick a character '))
    
    
    if pattern == 'square':
        print(char,char,char,char,char,char)
        print(char,"       ",char)
        print(char,"       ",char)
        print(char,"       ",char)
        print(char,"       ",char)
        print(char,char,char,char,char,char)
        
    if pattern == 'triangle':
        print("   ",char,"   ")
        print(" ",char," ",char," ")
        print(char," ",char," ",char)
    else:
        print('error :D')
        
    