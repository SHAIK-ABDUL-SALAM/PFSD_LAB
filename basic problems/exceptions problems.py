'''while True:
    try:
        n=int(input("enter a int"))
        m=int(input("enter a int"))
        o=n/m
        break

    except Exception as e:
        print("not int")
        print(e)
    except ValueError:
        print("not")
    finally:
        print("n")'''

try:
    a=open("file.txt","w")
    try:
     a.write("this is pfsf class")
    finally:
     a.close()
except IOError:
     print("file not found")
else:
     print("the file open")
     a.close()