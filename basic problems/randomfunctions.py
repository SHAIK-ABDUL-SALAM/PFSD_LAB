import random
n=random.randbytes(4) #print the bytes
print(n)
print(random.randrange(1,1000)) #give random numebr form 1 to 1000, if we give in decresing order we get error message

print(random.randint(100,211))
mylist=("hi","hello","h") #tuple
mylist1={"HHH","hh","h"} #sets
print(random.choice(mylist))
#print(random.choice(mylist1))  #here sets dont work
#random.shuffle(mylist)  #only list supported

import string
import random
s=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=s))
print(ran)
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)




