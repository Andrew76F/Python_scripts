number = int(input("Enter a number: ")) #input will be used as the argument for the function
def recurfunc(number):
    if number == 1: #the base, when number is reduced down to 1, this stops it.
        return 1
    else:
        return number + recurfunc(number - 1) # the main part, the first time it takes the unchanged number and adds it with itself - 1, from then on the second number is used then the third, etc, this continues until the base condition is met.
print(recurfunc(number))#calls the function with the input from earlier
