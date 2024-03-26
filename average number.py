a=int(input())
b=int(input())
g=a+b
avg=g/2
print(avg)

#list
a=[1,2,3,4,5,6,7]
avg=sum(a)/len(a)
print(avg)

#tuple
a = (1, 2, 3)
b = (3, 2, 1)
c = tuple(map(sum, zip(a, b)))
print(c)


numbers=[1,2,3,4,5]
n=int(input())
numbers.insert(2,8)
print(numbers)

while n>4:
    print("hi")
    n=n-1