number = int(input("Enter the number to get fabonacci number: "))

def faboo(a,b):
    
    if a > number:
        return
    print(a)
    faboo(b, a+b)
faboo(0,1)