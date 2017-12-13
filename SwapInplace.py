def swap(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return num1,num2

x=input("Enter a number: ")
y=input("Enter a number: ")
print "before swap", (x,y)
print "after swap", swap(x,y)