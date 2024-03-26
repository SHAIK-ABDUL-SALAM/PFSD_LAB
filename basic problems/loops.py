'''
n=int(input("Enter the n value"))
if n==0:
    print("wrong input")
else:
    for i in range(n,n+2):
        val=n*(n*1)
        print(val)
'''
'''
#using the string value
print("///////////////////////////////////")

x=0;
str=""
s=int(input("enter the star design number"))
for i in range(s):
    str = str+"*"

str1="thisismycountryindia"
for i in str:
    x=x+1
    print(str[0:x])
for i in str:
    x=x-1
    print(str[0:x])
'''

a1=1023
a2=format(a1,'o')
print(a2)

