#This is how we learned to concatenate strings in the ITF+ class.
a = "String 1"
b = "String 2"
print("a =" + a + " and  b=" + b)

#This syntax utilizes the concept of the f-string, which makes things a bit easier. No + sign needed!
x = "String 3"
y = "String 4"
print(f"x = {x} and y = {y}")

#We could also use an f-string like this:
print("c = {c} and d = {d}".format(c=1, d=2))
