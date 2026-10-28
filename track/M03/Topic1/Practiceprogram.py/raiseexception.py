try:
    res=10/0
except ZeroDivisionError:
    print("cannot divide by Zero")
else:
    print(res)


#raise with try-except
try:
    num1=10
    num2=10
    if num2==0:
        raise ZeroDivisionError("Error: cannot divide by zero")
    res=num1/num2
except ZeroDivisionError as e:
    print(e)
else:
    print(res)

#own exception
age=15
if age<18:
    raise ValueError("Age is Less than 18: Not Eligible")
else:
    print("Eligible to Vote")

marks=34
if marks<35:
    raise ValueError("Fail")
else:
    print("pass")