# This is a sample Python script.
# function to calculate sum of list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
# list of numbers
noList=[100, 200, 300, 400, 0, 500]


total=sum(noList)
print("Sum of number list is: " + str(total))