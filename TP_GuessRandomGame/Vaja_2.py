"""
print("HelloWorld");

x = 2;
print(x)
print(type(x))


for i in range(5):
    print(x)
"""
"""
x = input("Vnesi vrednost za X = ") 
y = input("Vnesi vrednost za Y = ") 

if x < y:
    print("Woah x = " + str(x) + "is < than y = " + str(y))
else:
    print("Woah x = " + str(x) + "is > than y = " + str(y))

"""
import random

x = random.randint(0, 30)

print("Ugani stevilo med 1 in 30")
xtry = 0


while xtry < 5:
    y = int (input("Vnesi pravo stevilo "))

    if y == x:
        print("Uganil si pravilno")
        break
    else:
        print("Uganil si napacno\n")
        if (y < x):
            print("Ugibaj vec od " + str(y))
        else:
            print("Ugibaj manj od " + str(y))
    
    xtry = xtry + 1

print("U LOST")