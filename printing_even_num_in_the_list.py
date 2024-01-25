

# ----- FUNCTIONS -----
def is_even(given):
    for i in range(len(given)):
        if given[i] % 5 == 0:
            print(given[i])
        else:
            False

# ----- PSEUDO CODE -----
# - Actual Code
given_list_or_set = (10,20,33,46,55)

print("Given list/set is " + str(given_list_or_set) + " . Find the numbers whose divisible by 5.")
print("The numbers who are divisible by 5 are: ")

is_even(given_list_or_set)



# - Result