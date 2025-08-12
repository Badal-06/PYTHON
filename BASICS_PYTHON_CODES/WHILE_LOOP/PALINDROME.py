original=a=int(input(" enter the Number:"))
Reverse=0
while a>0:
    r=a%10
    Reverse=Reverse*10+r
    a//=10
if original==Reverse:
    print(f"{original} IS PALINDOME!!")
else: 
    print(f"{original} IS NOT PALINDROME??")
