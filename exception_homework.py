a = 12
s = "hello"
try: 
    print(a+s)
except TypeError: print('error operand type(s) for +: "int" and "str"')
finally : print("hello word")