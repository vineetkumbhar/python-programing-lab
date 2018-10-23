#vineet kumbhar
#roll no :-32
# GR NO:- 11811198
#division:- M

x=int(input("enter any number"))
s=0
z=x
while x>0:
  y=x%10
  s=y**3+5
  x=x//10
print(s)
if s==z:
  print('angstrom number')
else:
  print('not an angstrom number')

