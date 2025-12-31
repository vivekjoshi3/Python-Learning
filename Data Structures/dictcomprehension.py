"""
Python comprehension is a very useful feature if you want to contruct dictionaries in one line of code.
We can construct the dictionary using a key : value mapping directly from an iterable object like lists

"""

dct = {i : i**3 for i in range(1,6)}
print(dct)

#Condition in dictionary comprehension and also this can be checked from the perspective of
# condition

numbers = {x : x**2 for x in range(1,11) if x%2 == 0}
print(numbers)

#Creating dictionary from lists
lst = ['Apple','Banana','Grapes']
dct = {item : len(item) for item in lst}

#this will print the length of all the values in the list
print(dct)

#You can also reverse the process by using the length of each string as the key and the string itself
dct = {len(item) : item for item in lst}
print(dct)

#Special keys with strings
dct = {'num : '+str(i) :i for i in range(1,11)}
print(dct)

#simple python code to demonstrate the values using the dictionary
keys = [1,2,3,4,5,6]
values = ['a','b','c','d','e']



#using the dictonary in the values
myDict = {k:v for(k,v) in zip(keys,values)}

for k,v in zip(keys,values):
    print(k,v)

#now we will use the fromlkey() method which will returns a dictionary with specific keys and values
dic = dict.fromkeys(range(5),True)
print(dic)

#using the dicitionary and also allowing the data to be used properly
#this will also emerge the data and will also help us in many ways in developing the relations with the people


