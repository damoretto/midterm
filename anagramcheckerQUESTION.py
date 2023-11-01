#Problem 14: Anagram Checker
#• Create a Python function that checks if two given strings are anagrams of each other (i.e.contain the same characters, ignoring spaces and capitalization).
#• You can use any user interface that you like, but the user must be able to continuously supply different pairs of items to be checked
#• Make sure that you attempt to handle all/some error cases

while(True):
    
    string1 = str(input('enter first string: '))
    string2 = str(input('enter second string: '))
    
    string1 = string1.lower()
    string2 = string2.lower()
    
    #remove spaces
    
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    
    list1 = list(string1)
    list2 = list(string2)
    
    #sort lists
    
    list1 = list1.sort()
    list2 = list2.sort()
    
    string1final = "".join(list1)
    string2final = "".join(list2)
    
    
    
    if string1final == string2final:
        print('these strings are anagrams!')
        
    #if list1 != list2:
        #print('these strings are not anagrams!')
