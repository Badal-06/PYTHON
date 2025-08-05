# Addition of two integers values :
a = 2
b = 4
sum =a+b  
print(sum) # 6
# Multiplication of integers and float :
a,b=5,2.4
c=a*b
print(c) # 12.0 (int * float = float)
# Multiplication of integers and a string :
a,b=2,3
txt="@"
print(a*txt*b) # @@@@@@
# multiplication + addition :
# Type 1:-
a,b="2",3
txt="@"
print((a+txt)*b) # 2@2@2@
# Type 2:-
a,b=2,4
c=5
print(a+b*c) #22
# Division :
a,b=2,3
c=a/b
print(c) # 0.666666
# Floor Division
a,b=2.5,5
c=a//b
print(c,a/b) # 0.0 , 0.5
# Remainder :
a,b=5,2
c=a%b
print(c) # 1