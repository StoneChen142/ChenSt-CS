def factorial(n):
   o=1
   for i in range(1,n+1):
         o*=i
         i+=2
   print(o)

n=int(input())

if n==0:
   print("1")
elif n>0:
   factorial(n)
else:
   print("Please enter a number greater or equal to 0")
   n=int(input())
   factorial(n)
