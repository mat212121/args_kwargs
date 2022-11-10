# def my_sum(*args):
#   print(*args)

# print(my_sum(3,4,5))
# #args are for entering
# #as many arguments as possible
# def a_sum(*args):
#   for num in args:
#     print (num)

# print(a_sum(1))
# print(a_sum(1,3))
# print(a_sum(1,3,4,5,6))
list = [2,4,6,3,7,1,5,8,9]
def sum_numbers(list):
  # sum = 0
  # for num in list:
  #   sum = sum + num
  # return sum 
  return sum(list)
print(sum_numbers(list))

#args
def a_sum(*args):
  # total = 0
  # for num in args:
  #   total += num  
  return sum(args)

  
  print(a_sum(3,5,23,1,6,7,42,27))