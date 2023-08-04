s1={1,'vijay',3}
s2={2,1,3,4,5}
print(type(s1))
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))


print("if else statements")
a=10
b=2
c=3
'''if a<b:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")    
else:print("a is greater") '''

print('************')
a=10
b=22
c=3
if(a>b & a>c):
    print("a is greatest")
elif(b>a & b>c):
    print("b is greatest")
else:
    print("c is greatest")  
tup=(1,2,3,4,5,6)
if 9 in tup:
    print("2 in tuple")
else:
    print("nope")
l1=[1,2,3,4,5,6]
print(l1[3])
if l1[1]==6:
    l1[2]=l1[4]+500
    print(l1)              
else:
    l1[2]=l1[4]+600 
    print(l1)   
print("###################")
d1={1:'vijay',2:'python','c':3}
print(d1)
if d1[2]=='python':
    d1[1]=d1[2]+'master'
    print(d1)