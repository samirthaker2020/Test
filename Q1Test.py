import numpy as np
list_of_numbers = list(np.arange(1,1001))
# delete first two digit
del list_of_numbers[0:2]
# delete last digit
list_of_numbers.pop(len(list_of_numbers)-1)
print(list_of_numbers)