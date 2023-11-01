#Problem 12: To Do List
#• Implement a simple to-do list where users can add, remove, and list tasks
#• You can use any user interface that you like, but the user must be able to continuously choose what they do to their “To Do” list
#• Make sure that you attempt to handle all/some error cases

#list popping and locking

while(True):
    
    todolist = []
    
    add = str(input('what would you like to add to your list? '))
    remove = str(input('what would you like to remove from your list? '))
    
    todolist.insert(add)
    print(list(todolist))
    
    todolist.remove(remove)

#can i get both inputs to show up at the same time? - want to know this for the currency conversion as well

     
    print(list(todolist))