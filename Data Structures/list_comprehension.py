# """
# LIST COMPREHENSION PROVIDE A CONCISE WAY TO CREATE LISTS.
# THEY OFFER A COMPACT SYNTAX FOR GENERATING LIST BASED ON EXISTING ITERABLES.
# SUCH AS LISTS, STRINGS, RANGES

# """

# lst = [1,2,3,4,5,6]
# print(lst)

# lst = [i**2 for i in lst]
# print(lst)


# #check for even numbers with the help of condition
# #this will help to get whether the numbers which are present are even numbers
# even_numbers = [x for x in range(10) if x%2 == 0]
# print(even_numbers)

# #print the sqaure of the numbers
# print([i**2 for i in range(21) if i%2 == 0])

# #multi-dimensional lists 

# lst = [[j for j in range(1,4) for i in range(3)]]
# print(lst)


# lst = [[1,2,3],[4,5,6],[7,8,9]]
# print([num for row in lst for num in row])

lst = [1,2,34,45,67]
print(lst)


#use of list comprehensions
lst = [i**2 for i in lst]
print(lst)

#you can also use if condition for the lst
even_numbers = [x for x in range(10) if x%2 == 0]
print(even_numbers)

#you can also use multiple operations
print([i**2 for i in range(21)])

#multidimensional lists
lst = [[j for j in range(1, 4)] for i in range(3)]
print(lst)

#this will be used for the lists which are present
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for row in lst for num in row])
