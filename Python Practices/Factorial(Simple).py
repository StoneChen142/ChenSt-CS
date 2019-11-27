
### SRC - Can you convert into a function?
n=int(input("Please input a positive number: "))
sum=1
i=1
if n==0:
    print("0")
elif n<0:
    print("error")
else:
    for i in range(1,n):
        sum*=i
    print(sum)
