movies = [["Monty Python and the Holy Grail", 1975, 9.95],
              ["On the Waterfront", 1954, 5.59],
              ["Cat on a Ilot Tin Roof", 1958, 7.95],
              ["Gone with the Wind", 1939, 14.95]]

name = input("Name: ")
a = []
for movie in movies:
    m = [str(x) for x in movie]
    a.append(m)


year = int(input("Year: "))
price = float(input("Price: "))
movie = [name, year, price]
movies.append(movie)
print(name, "was added")
print()