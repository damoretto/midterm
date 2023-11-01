while(True):
#Input two integers and operation
    num1 = int(input('enter first integer'))
    num2 = int(input('enter second integer'))
    operation = str(input('enter operation you would like to perform: +,-,/,*'))

    if operation == '+':
        answer = num1+num2

    else:
        print('please use symbol for operation')

    print(answer)
