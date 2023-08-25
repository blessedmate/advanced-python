# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    # print(next(i))
    # print(next(i))

    # TODO: iterate using a function and a sentinel
    # Sentinel is the end of the iterator
    with open("02 BuiltIn Functions/testfile.txt") as fp:
        for line in iter(fp.readline, ""):
            print(line)

    # TODO: use regular iteration over the days
    for m in range(len(days)):
        print(m, days[m])

    # TODO: using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # TODO: use zip to combine sequences
    # Returns a tuple with the values of each list inside the zip
    # If lists length is different, it stops with the shortest list last element
    for m in zip(days, daysFr):
        print(m)
    for i, m in enumerate(zip(days, daysFr)):
        print(i, m[0], "=", m[1], "in French")


if __name__ == "__main__":
    main()
