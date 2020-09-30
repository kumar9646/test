a = int(input("enter first number: "))
b = int(input("enter second number: "))

def sum(a,b):
    s=a+b
    return(s)
def mul(a,b):
    m=a*b
    return(m)
def sub(a,b):
    s=a-b
    return(s)
def divide(a,b):
    try:
        d=a/b
        return (d)
    except ZeroDivisionError as e:
        print(e," you are dividing by 0, not good")
print("sum:", sum(a,b),"multiple:", mul(a,b),"subtraction:", sub(a,b), "Quotient:",divide(a,b))
