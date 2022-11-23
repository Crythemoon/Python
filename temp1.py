def display():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("find - Find movies by year")
    print("exix - Exit program")
    print()

def list(movies):
    x = 1
    if len(movies) == 0:
        print("There is no movie in the database.")
    else:
        for movie in movies:
            print(str(x) + ".", movie[0], "(" + str(movie[1]) + ") @", str(movie[2]) )
            x += 1
    print()

def add(movies):
    name = input("Name: ")
    for movie in movies:
        if name.lower() in movie.lower():
            print("this movie was already added")
    year = int(input("Year: "))
    price = float(input("Price: "))
    movie = [name, year, price]
    movies.append(movie)
    print(name, "was added")
    print()

def delete(movies):
    num = int(input("Number: "))
    li = len(movies)
    if num >= 1 and num <= li:
        item = movies.pop(num - 1)
        print(item[0], "was deleted.\n")
    else:
        print("Invalid movie number\n")
    print()

def find(movies):
    year = int(input("Year: "))
    for movie in movies:
        if year in movie:
            print(movie[0], "was released in", str(movie[1]))
            output = movie[0], "was released in", str(movie[1])
    if not output in locals():
        print("There are no movies in", year)
    print()

def command():
    movies = [["Monty Python and the Holy Grail", 1975, 9.95],
              ["On the Waterfront", 1954, 5.59],
              ["Cat on a Ilot Tin Roof", 1958, 7.95],
        ]
    choice = "y"
    while choice.lower() != "exit":
        choice = input("Command: ")
        if choice.lower() == "list":
            list(movies)
        elif choice.lower() == "add":
            add(movies)
        elif choice.lower() == "del":
            delete(movies)
        elif choice.lower() == "find":
            find(movies)
        else:
            print("Invalid choice, please try again.")
            print()

def main():
    display()
    command()

if __name__ == "__main__":
    main()