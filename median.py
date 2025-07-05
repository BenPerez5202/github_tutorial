import math
def median(input):
  list = len(input)
  if list % 2 == 1:
    return input[list // 2]
  else:
    a = input[list // 2- 1]
    b = input[list // 2]
  return (a + b) / 2

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))