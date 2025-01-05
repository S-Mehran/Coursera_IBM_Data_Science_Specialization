Rating_BackinBlack = 7

if Rating_BackinBlack > 8:
    print("The album is amazing")
elif Rating_BackinBlack <= 8:
    print("Album is Ok")

Album_Release_Year = 1991

if Album_Release_Year < 1980 or Album_Release_Year > 1990 and Album_Release_Year <= 1993:
    print(Album_Release_Year)
else:
    print("Not Found")

Years = [1991, 1992, 1993]
N = len(Years)

for year in range(N):
    print(Years[year])


for year in Years:
    print(year)


colours = ["red", "yellow", "blue", "white"]
for i, colour in enumerate(colours):
    print(i,colour)


count = 0

while count <= 5:
    print(count)
    count += 1


dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


for i in range(-5,5):
    print(i)


Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print("Genre:", Genre)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while i < len(PlayListRatings) and rating >= 6:
    print(rating)
    i = i+1
    rating = PlayListRatings[i]


print("It took", i, "repititions")

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
tmp = squares[i]

while tmp == "orange" and i < len(squares):
    new_squares.append(tmp)
    i = i+1
    


print(new_squares)

number = 0

for number in range(0,61):
    if number % 6 == 0:
        print(number)

multiple_seven = [] 

for n in range(0,71):
    if n % 7 == 0:
        print(n)
        multiple_seven.append(n)
        

print(multiple_seven)



print("Multiplication table of 6:")
for i in range (10):
    print("6*",i,"=",6*i)
print("Multiplication table of 7:")
for i in range (10):
    print("7*",i,"=",7*i)



Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_animals = []
for animal in Animals:
    if len(animal) == 7:
        print(animal)
        new_animals.append(animal)

print("For Loop:", new_animals)

Animals_n = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
i = 0
animal_n = Animals_n[i]
new_animals_n = []
while i <= len(Animals_n) and len(animal_n) == 7:
    new_animals_n.append(animal_n)
    i = i + 1
    
print(new_animals_n)

