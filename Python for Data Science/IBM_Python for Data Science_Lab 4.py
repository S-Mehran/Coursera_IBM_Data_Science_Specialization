a_list = [1, "hello", [1,2,3], True]
print(a_list)
print(a_list[1])
print(a_list[2])
print(a_list[1:4])


A = [1, 'a']
B = [2,1,'d']
C = A+B
print(C)

New_list = []
Shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]
Shopping_list.append("Football")
print(Shopping_list)
print(Shopping_list[0])
print(Shopping_list[-1])
print(Shopping_list[1:3])
Shopping_list[3] = "Notebook"
print(Shopping_list)
del(Shopping_list[4])
print(Shopping_list)

update = 'A,B,C,D'.split(',')
print("Update List is:", update)

X = update[:]
print("X is", X)

#TUPLES

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
R_sorted = sorted(Ratings)
print(R_sorted)

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print(NestedT[2][1])
print(NestedT[4][1][1])

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 
print(len(genres_tuple))
print(genres_tuple[3:6])
print("disco".find('s'))


#DICTIONARY

album_sales_dict = {"Back in Black": "50 Million", "The Bodyguard": "55 Million", "Thriller": "65 Million"}
print("Total sales of Thriller is:", album_sales_dict["Thriller"])

print(album_sales_dict.keys())

print(album_sales_dict.values())


inventory = {}

Product1_Name = "Mobile phone"
Product1_Quantity = 5
Product1_price = 20000
Product1_Release_Year = 2020

inventory["Product1_Name"] = Product1_Name
inventory["Product1_Quantity"] = Product1_Quantity
inventory["Product1_price"] = Product1_price
inventory["Product1_Release_Year"] = Product1_Release_Year

print(inventory)


Product2_Name= "Laptop"
Product2_Quantity= 10
Product2_price = 50000
Product2_Release_Year= 2023

inventory["Product2_Name"] = Product2_Name
inventory["Product2_Quantity"] = Product2_Quantity
inventory["Product2_price"] = Product2_price
inventory["Product2_Release_Year"] = Product2_Release_Year

print(inventory)


print("Product2_price" in inventory)
del(inventory["Product1_Release_Year"])
del(inventory["Product2_Release_Year"])

print(inventory)


#SETS

updated_list = ['rap','house','electronic music', 'rap']
new_set = set(updated_list)
print(new_set)

A = [1, 2, 2, 1] 
B = set([1, 2, 2, 1])

Addition_A = sum(A)
Addition_B = sum(B)
print("A:", Addition_A)
print("B:", Addition_B)

if Addition_A == Addition_B:
    print("Yes, they are equal")
else:
    print("Sorry")

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1.union(album_set2)

print(album_set3)

print(album_set1.issubset(album_set3))

# CHEAT SHEET: https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstUFkwMTAxRU4tU2tpbGxzTmV0d29yay9sYWJzL2hhbmRvdXRzL0NoZWF0X1NoZWV0X1dlZWstMl9QYXJ0LTIubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzExNjM4NTk2fQ.luBpuMXe9qHg0AyG0CeoUDtX9HzrpDcLZMm6gP-p5Dw


