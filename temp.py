def message():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - exit program")
    print()

def command_list(movie):
    x = 1
    num = len(movie)
    if num == 0:
        print("No movie in list.")
    else:
        for movies in movie:
            print(str(x) + ".", movies[0], "(" + str(movies[1]) + ")")
            x += 1
        print()

def command_add(movie):
    name = input("Name: ")
    year = int(input("Year: "))
    movies = []
    movies.append(name)
    movies.append(year)
    movie.append(movies)
    print(name, " was added.")
    print()

def command_del(movie):
    num = int(input("Number: "))
    li = len(movie)
    if num >= 1 and num <= li:
        item = movie.pop(num - 1)
        print(item[0], "was deleted.\n")
    else:
        print("Invalid movie number\n")
    print()

def command():
    choice = "list"
    cl = ["list", "add", "del", "exit"]
    movies = [
              ["Monty Python and the Holy Grail", 1975],
              ["On the Waterfront", 1954],
              ["Cat on a Hot Tin Roof", 1958]
             ]

    while choice.lower() != "exit":
        choice = input("Command: ")
        while True:
            if choice.lower() not in cl:
                print("Enter Valid Command.")
                print()
                choice = input("Command: ")
            else:
                break
        if choice.lower() == "list":
            command_list(movies)
        elif choice.lower() == "add":
            command_add(movies)
        elif choice.lower() == "del":
            command_del(movies)
    print("Good Bye!")

def main():
    message()
    command()

if __name__ == "__main__":
    main()
