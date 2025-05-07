a = int(input("enter your first num ="))
b = int(input("enter your sec num ="))
c = int(input("enter your third num = "))
d = int(input("enter your fourth num = "))
if(a>b and a>c and a>d):
    print("first num is the greatest",a)
elif(b>c and b>d):
    print("sec num is the greatest",b)
elif(c>d):
    print("third num is the greatest",c)
else:
    print("fourth num is the greatest",d)