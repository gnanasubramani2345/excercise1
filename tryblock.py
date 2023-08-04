"""try:
    a=10/0
except Exception as e:
    print(e)    
else:
    print("a value",a)    
finally:
    print("thank you")
print(dir(locals()['__builtins__']))   
print(len(dir(locals()['__builtins__'])))
print("name error")
try:
    print(a)
except Exception as e:
    print(e)    
else:
    print("value of a",a)
finally:
    print("thank you")  
try:
    print (int("vijay"))
except Exception as e:
    print(e)    
else:
    print("value of a",a)
finally:
    print("thank you")
try:
    a=[10,20,30,40]
    i=90
    print(a[i])
except Exception as e:
    print(e)    
else:
    print("value of a",a[i])
finally:
    print("thank you")

try:
    f=open("test.txt")
    print(f.read())
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print("thank you") """
try:
    a=10/0
    print(a)  
except Exception as e:
    print(e)
try:
    b=[10,20,30,40]
    i=0
    print(b[i])
except Exception as e:
    print(e)            

         
