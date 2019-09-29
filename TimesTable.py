### SRC - Please use meaningful variable names and use coding conventions

n=int(input("Please input a number greater or equal to 1 and less or equal to 20: "))
v=False
v2=False
select=0
i=0
while v2==False:
    while v==False:
        if 0<n and n<21:
            v=True
            n=round(int(n))
        else:
            n=int(input("Invalid, please input a positive number maximum 20: "))
    if 0<n and n<21:
        select=int(input("Is "+str(n)+" the number you want? (1=Yes 0=No): "))
        if select==1:
            v2=True
        else:
            n=-1
    else:
        n=int(input("Please input a positive number maximum 20: "))  ### SRC - You appear to be using n for the table and the rows...

        

for i in range(n+1):
    print(i*n)
