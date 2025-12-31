"""
MULTIDIMENSIONAL LIST IS USED FOR DIFFERENT PURPOSES 
AND WE CAN ACCESS THOSE USING THE FOR LOOP

"""

List1 = [[1,2,3,5],[4,6,7,9],[8,10,11,13],[12,13,14,17]]

for i in List1:
    print(i , end=' ----------  ')

#accessing the elements using the 2D-List
print("\n")
for i in range(len(List1)):
    for j in range(len(List1[i])):
        print(List1[i][j],end=" , ")

""" 
    MODIFY THE ELEMENTS IN A 2 DIMENSTION LIST
    WE WILL TRY TO MODIFY THE ELEMENT IN THE MATRIX 
    WE WILL TRY TO MODIFY THE ELEMENT NAMED L1[1][1]->
    THIS WILL UPDATE THE 2 ELEMENT IN THE LIST    
"""

L1 = [[1,2,3,5],[4,6,7,9],[8,10,11,13]]

L1[1][1]=9

print(L1[1][1])

#This will update the list in the second matrix.
L1[1]=['Ashish',25]
print(L1[1])

#append the data to the existing list 
L1.append([12,34,10,9,10])
print("Appending the items in the list ",L1)

#extend the list using extend function
L1[0].extend([12, 14, 16, 18]) 
print("Extend the list : ",L1)

#REVERSE THE ORDER OF A GIVEN LIST USING reverse() method
print(L1[::-1])
print(L1)

#CHALLENGE GALORE
def find_max_value(matrix):
    max_value = float('-inf')
    for row in matrix:
        max_value=max(max_value,max(row))
    return max_value

matrix = [

    [3,7,1,2],
    [8,5,6,4],
    [2,1,8,9]
]
max_value = find_max_value(matrix)
print("\Maximum Value : ",max_value)

# define the list
lst = [1,2,3,4,5,[1,2,3],5,6]
print("Length of the list : ",len(lst))


#Reverse the list
lst = [[1,2,3],[4,5,6],[7,8,9]]


m = [[2,4,6,8,10],
     [3,6,9,12,15],
     [4,8,12,16,20]]

#this will print the value 
print(m)


#This will have the data which we need ot print
m , n = 5,6

mat =[]

for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)

print(mat)


#accessing the data for multidimensional list
a = [[2,4,6,8] , [3,6,9,10], [4,8,16,20]]
for row in a:
    print(row)

#print the data for the nested loops
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] , end = " ")
    print()

#Methods on Multidimensional lists

#Using the append() function
a= [[2,4,6],[3,6,98,100]]
a.append([5,10,15])
print(a)

#using the extend function
a[0].extend([8,10])
print(a)

#using the reverse function
a[1].reverse()
print(a)

#using the indexing to write the data
print(a[0][1])

#using the list comprehension to write the data
b = [[x*2 for x in row] for row in a]
print(b)
