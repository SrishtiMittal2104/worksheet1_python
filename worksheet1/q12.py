a = int (input("enter the first angle: "))
b = int (input("enter the second angle: "))
c = int (input("enter the third angle: "))
s = a+b+c
if (s == 180):
    print ("will form a triangle")
elif (a<=0 or b<=0 or c<=0):
    print ("not valid")
else:
    print ("will not form a triangle")