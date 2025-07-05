def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 5, 4, 6]
print(mean(my_list))