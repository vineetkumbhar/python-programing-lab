#vineet kumbhar
#roll no :-32
# GR NO:- 11811198
#division :- M

f=1
n=input("enter a number:")
if n<0:
  print("enter positive")
elif n==0 or n==1:
  print('1')
else:
  while n>1:
   f=f*n
   n=n-1
  print(f)



