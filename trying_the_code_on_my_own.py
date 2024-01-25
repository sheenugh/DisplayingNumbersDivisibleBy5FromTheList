def is_even(given):
    for i in range(len(given)):
        if given[i] % 2 == 0:
            print(given[i])
        else:
            print("invalid")

given = (10,20,33,46,55)
is_even(given)