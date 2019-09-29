### SRC - Please use meaningful variable names and use coding conventions(Fixed)

base=int(input("Please input the base, a number greater or equal to 1 and less or equal to 20: "))
time=int(input("Please input the times, a number greater or equal to 1 and less or equal to 20: "))
v=False
v2=False
select=0
i=0
while v2==False:
    while v==False:
        if 0<base and base<21:
            v=True
        else:
            base=int(input("Invalid, please input the base, a positive number maximum 20: "))
    if 0<base and base<21:
        select=int(input("Is "+str(base)+" the number you want for the base? (1=Yes 0=No): "))
        if select==1:
            v2=True
        else:
            base=-1
    else:
        base=int(input("Please input the base, a positive number maximum 20: "))  

v=False
v2=False
select=0
while v2==False:
    while v==False:
        if 0<time and time<21:
            v=True
        else:
            time=int(input("Invalid, please input the times, a positive number maximum 20: "))
    if 0<time and time<21:
        select=int(input("Is "+str(time)+" the number you want for the times? (1=Yes 0=No): "))
        if select==1:
            v2=True
        else:
            time=-1
    else:
        time=int(input("Please input the times, a positive number maximum 20: "))  

for i in range(0,time+1):### SRC - You appear to be using n for the table and the rows...(Fixed)
    print(i*base)
