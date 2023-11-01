#Problem 7: Count Vowels & Consonants
#• Write a program that counts the number of vowels and consonants in a given string, with letters in the English alphabet
#– Hint: The vowels are: a/A, e/E, i/I, o/O or u/U and the consonants are all of the other letters
#• You can use any user interface that you like, but the user must be able to continuously enter strings to be analyzed
#• Make sure that you attempt to handle all/some error cases

while(True):
    string = str(input('enter a word or sentence: '))
    
    string = string.lower()
    
    string = string.replace(" ", "")
   
    index=0
    
    count1=0
    
    count2=0
    
    for index in range(len(string)):
        if ((string[index] == "a")
        or (string[index] == "e")
        or (string[index] == "i")
        or (string[index] == "o")
        or (string[index] == "u")):
            count1 += 1
        
        else:
            count2 += 1
    print('number of vowels is', count1)
    print('number of consonants is', count2)
            
    
    #list1=
    #count1= len(list1)
    #list2=
    #count2 = len(list2)