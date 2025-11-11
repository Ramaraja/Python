print ("test")

def test():
	print ("this is from test def")


# numbers

a = 1
b = "A"
# c = a + b



print (type(b))



s = "python training!"

'0 1 2 3 . . . 15'



print (len(s))

print (s[7])

print (s[15])

print (s[-16])



# list

l = [1, 2, 3, 4]

l1 = ["a", "test", 1]

print ("max:", max(l))
print ("min:", min(l))

print (dir(l))

l.append(5)





# tuple

t = ("test", 1)

print (type(t))

print (t[1])

lt = [(1,2),(3,4)]


# boolean

bool = False

if bool:
	print ("this is true")


if not bool:
	print ("this is false")


# set

s = set([1,2,3,4,5])

s1 = set([5,6,7,8])

print (s.difference(s1))


# dict

d = {}

d1 = {"name": "ram", "role":"dev", "age": 36}

print (d1)
print (d1.get("name"))

d1.update({"dept":"cloud"})

print (d1)
# d1["dept"] = "cloud"



