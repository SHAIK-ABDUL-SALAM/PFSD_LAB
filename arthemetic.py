def vowel(c):
    switc={
      '+':a+b,
      '-':a-b,
      '/':a/b,
      '*':a*b
      }
    return switc.get(c,"Invalid input")


a=int(input('Enter the a value'))
b=int(input('Enter the b value'))
c=input('Enter the c value the arthemetic')
print(vowel(c))



