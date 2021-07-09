x = int(input("number first= "))
y = int(input("number second= "))
op= input(" operation ")
def add():
    return x + y
def sub():
    result = x - y
    return result
def multiply():
    result = x*y
    return result
def division():
    result= x/y
    return result
if op == "+":
    print("answer = ", add())
elif op == "-":
    print("Answer =",sub())
elif op == "*":
    multiply()
    print("result =", multiply())
elif op == "/":
    division()
    print("result =",division())
else :
     print( "invalid oparation")