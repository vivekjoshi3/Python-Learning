"""
DICTIONARY IS A COLLECTION OF KEY VALUE PAIRS.
EACH KEYS WHICH ARE PRESENT SHOULD BE UNQIUE AND SHOULD BE USED FOR THE GETTING THE VALUES IN THE DICTIONARY.
THEY CAN BE OF ANY DATA TYPE OR EVEN OTHER COLLECTIONS.
THIS STRUCTURE ALLOWS FOR EFFICIENT DATA RETRIEVAL BASED ON THE KEY.
UNLIKE LISTS WHICH REQUIRE ACCESSING ELEMENTS BY INDEX.

PROPERTIES OF DICTIONARY
1. Dcitionaries in Python are unordered colletion of items. Unlike the lists which are ordered 
and that order is preserved.
2. Dictionaries are mutable, meaning you can modify their contents by adding, removing, or updating key-value pairs.
3. Keys in a dictionary are mutable which says that the keys cannot be changed only values can be changed.
4. Retriving a value from a dictionary is highly efficient typically taking constant time on average


There are different ways to create a dictionary. You can create dictionary in Python using the curly braces{}and 
specifying the key-value pairs seperated by colons ':'. Dictionary can also be created 
by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}.

"""

Dict = {}
print("Empty dictionary")

#declaring the dictionary which is present and you can also use the structure
#to get the data from the list

Dict = dict({1: 'Data', 2 : 'Science ', 3 : 'Python'})
print(Dict)

Dict = dict([(1,'Data'),(2,'Science')])
print("Dictionary with the item pair is ")
print(Dict)


Dict = dict([(1,'Data'),(2,'Vivekanand Joshi')])
print(Dict)


#In the given dictionary
dct = {1:"Ashish",2:"Avneet",3:"Riya",4:"Sakshi",3:"Joshi Vivekanand"}
print(len(dct))
print(dct)


my_dict = {'name':'Rose','age':23}
print(my_dict)
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('name','Unknown'))
print(my_dict.get('city','Unknown'))

#add the data in the dictionary
"""
YOU CAN ADD ELEMENTS IN A DICTIONARY IN MULTIPLE WAYS.
ONE VALUE AT A TIME CAN BE ADDED TO DICTIONARY BY DEFININGVALUE ALONG WITH THE KEY
, FOR INSTANCE Dict[key] = 'Value'. Update an exisiting value in a Dictionary
can be done by using the built-in update() method

Note : If the key doesn't exist it create a new key-value pair and if the key
already exists in the dictionary then the new value will be replaced.

"""

Dict = {}

Dict['Name'] = 'Rose'
Dict['Age'] = 24
Dict['city'] = 'Pune'

print("Dictionary after adding/ modifying the elements ")

#Modify the dictionary

Dict['Name']= 'Vivekanand Joshi'
print(Dict)

Dict.update({'age':26 , 'city':'Noida'})
print(Dict)


#Removing the elements from the Dictionary
Dict = {'name':'Rose', 'age':24, 'gender':'Male'}

#remove the value from the dictionary
removed_value = Dict.pop('gender')
print(removed_value)

#Removing a key from the dictionary
del(Dict['age'])
print(Dict)


#cleaning the dictionary
#In python you can remove all the elements of a dictionary using the 
#clear() method. This is useful when you want to reuse the dictionary but
#dont't need its current contents

dct.clear()
print("Dictionary is cleared ")

#Checking if a key is present in the Dictionary
dct = {1 : "Ashish ",2:"Avneet",3:"David",4:"Ankur",5:"Sakshi"}
print(dct)
print(1 in dct)
print('1' in dct)


#Use of update in the dictionary
dct_1 = {1:'A' , 2: 'B' , 3: 'C'}
dct_2 = {1:'a', 2: 'b', 3: 'c'}
dct_1.update(dct_2)
print(dct_1)

