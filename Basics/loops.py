"""
PYTHON FOR LOOPS ARE USED TO TITERATE ON THE FOLLOWING THINGS
1. LISTS
2. SETS
3. TUPLES
4. STRING
5 RANGE

"""

#here the list is defined and checked how the strings can be traversed using the for loop

"""
the syntax used for the for loop is 

for var in iterable:
    #statements
    pass
    
"""
s =["Geeks ","COde academy ","Vivekanand Joshi"]
for i in s:
    print(i)

#Python for loop using string

s = "Vivekanand Joshi "

for i in s:
    print(i)

"""

USE OF RANGE IN THE FOR LOOP
WITH THE HELP OF RANGE YOU CAN TRAVERSE THROUGH THE DATA PROPERLY


range(stop) - Generates number from 0 to stop-1
range(start, stop) - Generates number from start to stop-1
range (start , stop , step) - Generates the number from start to stop-1, incrementing by the step

"""

#this will use as start and stop and will use this range only to traverse through the data
for i in range(10,20):
    print(i)

#this will use step as an increment to solve the issues
for j in range(0, 10,20):
    print(j)

    """
    CONTINUE STATEMENT 
    WHEN EXECUTION LEAVES THE SCOPE ALL AUTOMATIC OBJECTS WHICH ARE DEFINED OR CREATED IN THE SCOPE ARE DESTROYED AGAIN AND THE CONTROL GOES BACK TO LOOP AGAIN
    
    """

    for i in "geeksforgeeks":

        if i =="e" or i =="s":
            continue
        print(i)


        #break statement
        #this will be used when we want to break some statement which is present or if the condition is met
    
    for i in "geeksforgeeks":
        if i =="e" or i =='s':
            break
    
    print("Value after i : ",i)

#pass statement is used to write the empty control statements, functions and classes.
for i in "geeksforgeeks":
    pass
print(i)


#use of else statements in for loop
for i in range(1,5):
    print(i)
else:
    print("No break/n ")


print("---------------------------------------------------------------------")
#use of enumerate with the help of for loop
"""
This will traverse through each and every transaction properly and will also 
give the number which are present at the start

0. Data
1. Data
2. Data
3. Data
"""
li = ["eat","sleep","repeat"]
for i,j in enumerate(li):
    print(i+1,j)

print("-------------------------------------------------------------")

""" we can also use nested for loops """
for i in range (1,4):
    for j in range(1,4):
        print(i,j)
