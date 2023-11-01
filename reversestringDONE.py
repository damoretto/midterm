#Problem 8: Reverse a String
#• Develop a program that reverses a given string, supplied by a user
#• You can use any user interface that you like, but the user must be able to continuously enter strings to be reversed
#• Make sure that you attempt to handle all/some error cases


#separate into list and reverse list then put back into string
while(True):
    
    string = str(input('enter a string '))
    thelist = list(string)
    thelist.reverse()
    reversedstring = "".join(thelist)
    
    print(reversedstring)