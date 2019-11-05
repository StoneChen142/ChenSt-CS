### SRC - Good, but keep unsing the coding conventions!
def factorial(n,result):
   n=int(input("Enter a number: "))
   o=1
   if n>0:
      for i in range(1,n+1):
            o*=i
            i+=2
      result=o
      n=n
      print(n,result)
   elif n==0:
      print("1")
   else:
      print("Please enter a number greater or equal to 0")
      factorial(n,result)
   
def again():
   a=bool(input("Again? 1=Yes, 0=No : "))
   if a==True:
      factorial(n,result)
      again()

result=0
n=0

factorial(n,result)

again()
