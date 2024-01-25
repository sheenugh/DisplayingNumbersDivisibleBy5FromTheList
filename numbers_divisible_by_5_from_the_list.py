

# ----- FUNCTIONS -----
# - This section is for the def function of divisibility by 5
def divisibility_by_5(given):
    for i in range(len(given)):
        if given[i] % 5 == 0:
            print(given[i])
        else:
            False


#>>>>>>>>>> PSEUDO CODE <<<<<<<<<<
#----- ACTUAL CODES -----
# - Given set of numbers
given_list_or_set_of_numbers = (10,20,33,46,55)

# - Printing the result
print("The given list/set of number is " + str(given_list_or_set_of_numbers) + " . Find the numbers whose divisible by 5.")
print("The numbers who are divisible by 5 are: ")

# - Caller in def function
divisibility_by_5(given_list_or_set_of_numbers)


