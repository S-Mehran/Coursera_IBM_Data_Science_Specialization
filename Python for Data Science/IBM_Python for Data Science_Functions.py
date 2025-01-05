def Addition(a, b):
    c= a+b
    print("a + b =", c)

Addition(2, 3)
Addition(100, 230)
Addition(50, 60)
Addition("Hello", "World")
lst1 = [1,2,3,4,5]
lst2 = [7,8,6,9,10]
Addition(lst1, lst2)
tup1 = (1,2,3,4,5,7)
tup2 = (6,8,9,10)
Addition(tup1, tup2)


def count(string):
    count = 0
    words = string.split()
    for word in words:
        if word == "little":
            count = count+1
            
            print("The number of required strings are:", count)
    

count("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go")


#TRY/EXCEPT

def safe_divide(x,y):
    try:
        z = x/y
        print(z)
    except ZeroDivisionError:
        print("not divisible by zero")


nom = int(input("Enter the value of nominator: "))
denom = int(input("Enter the value of denominator: "))
safe_divide(nom, denom)
import math 
def sq_root(s):
    try:
        sq = math.sqrt(s)
        print(sq)
    except ValueError:
        print("Square root cannot be obtained for negative values")

g = float(input("Enter the value: "))
sq_root(g)


def complex_calc(num):
    try:
        result = num/(num-5)
        print(result)
    except Exception as e:
        print("Some Error Found")


user_input = float(input("Enter a value for complex calculation: "))
complex_calc(user_input)

