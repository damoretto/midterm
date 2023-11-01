#Problem 9: Currency Converter
#• Build a program that converts between different currencies, based on user input
#• You can use any user interface that you like, but the user must be able to continuously enter amounts to be converted and be able to specify the old and new currencies in question (you can also assume any conversion rate that you like!)
#• Make sure that you attempt to handle all/some error cases

#CAD TO USD AND VICE VERSA I GUESS

while(True):
    
    CAD=float(input('enter value in CAD, ENTER 0 IF CONVERTING FROM USD: '))
    USD=float(input('enter value in CAD, ENTER 0 IF CONVERTING FROM CAD: '))
    
    if CAD > 0:
        USDconv = CAD*1.25
        print('the USD value for this amount is:', USDconv)
        
    if USD > 0:
        CADconv = USD*0.75
        print('the CAD value for this amount is:', CADconv)
            
