t1=[]
x=int(input("Enter the no : "))

s=1
while x>=s:
    t2=[]
    num=int(input(f"Enter element {s}: "))
    p=num**2
    t2.append([num ,p])
    t4=tuple(t2)
    t1.append(t4)
    s+=1
t3=tuple(t1)
print(t3)