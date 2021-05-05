
a=open("number.txt","r")
b=a.read()
c=len(b)
l=0
f=""
for i in range(0,c):
    if b[i]!=" ":
        f=f+b[i]
    else :
        try:
            l=int(f)
            print(l)
        except ValueError:
            print("it is not int")
        f=""