n=int(input("Please input a number greater or equal to 1 and less or equal to 20: "))
v=False
v2=False
while v==False:
    if 0<round(int(n)) and round(int(n))<21:
        v=True
        n=round(int(n))
    elif str.isdigit(n)==False:
        n=input("Invalid, please input a positive number maximum 20: ")
    else:
        n=input("Invalid, please input a positive number maximum 20: ")

v2=input("Is "+str(n)+" the number you want? (1=Yes 0=No): ")
n=int(n)
if v2==True:
    for i in range(n+1):
        print(i*n)
