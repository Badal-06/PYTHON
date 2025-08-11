nums =(1,4,9,16,25,36,49,64,81,100)
x=49
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding")
    i+=1