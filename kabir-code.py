#data_types .py
a = 10
b = 3.14
c = "Hello"
d = True

print(f"{a} is a {type(a)}")
print(f"{b} is a {type(b)} ")
print (f"{c} is a {type(c)}")
print(f"{d} is a {type(d)}")
#Str
e= 'Kabir'
f= "humayun"
name = e + " " + f

g = name + " said, \"It's a beautiful day !"
h = ' " How \'ya doing\'today?"\n\t"GOOD!"'
print(g, "\n", h)

# Bool - only 0 or " " is False
i = True
j = False
k = bool(-1)
l = bool(a)
m = bool("")
n = bool(0)
o = bool(g)

print(i,j,k,l,m,n,o)