b = 1
c = 'jjk'
d = [1,2]

print(type(b))
print(type(c))

if type(b) is int:
    print(f"'{b}' is an integer")

if type(c) is str:
    print(f"'{c}' is a string")
    
print(f"type of {d} is: {type(d)}")