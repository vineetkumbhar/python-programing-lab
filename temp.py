#Tempurature
#Name-Kanav Gupta
#Division-M
#Roll no-25
temp=int(input("Enter temperature:")) #input from user
dec=input("if value is in celius say 'y' or else say 'n'")
if 'y'==dec: #if-else statement
  f=9*temp/5 +32 
  print(f)
else: 
  c=5*temp/9 -32
  print(c)