#Problem 13: Unique Elements
#• Write a Python function that takes a list as input and returns a new list with only the unique elements (i.e. removing duplicates)
#• You can use any user interface that you like, but the user must be able to continuously supply different lists to be made to have only unique elements
#• Make sure that you attempt to handle all/some error cases

while(True):
    
    listbruh = list(input('enter your list bozo '))
    
    #convert list into set to remove duplicate elements
    uniquelist = list(set(listbruh))
    
    print(uniquelist)

    
