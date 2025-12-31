"""

A Multi dimension dictionary is used at the time when there are certain leves of data which has to be extracted 
There is also a multi-dimensional strcuture of the data which will help to extract the data
this information can contain private information about people and their data.

"""
#Checking if a key is present in the Dictionary
dct = {1 : "Ashish ",2:"Avneet",3:"David",4:"Ankur",5:"Sakshi"}
print(dct)
print(1 in dct)
print('1' in dct)

for k,v in dct.items():
    print("Value of keys is : ",k,v)


#Use of update in the dictionary
dct_1 = {1:'A' , 2: 'B' , 3: 'C'}
dct_2 = {1:'a', 2: 'b', 3: 'c'}
dct_1.update(dct_2)
print(dct_1)

 
#Going level deeper with the marks
data = {1 :{'name':'Ashish ','phone':1231412312, },
        2 :{'name':'Vivekanand Joshi','phone':7757014202, },
        3 :{'name':'Ashish ','phone':1267863781263, },
        }

#this will print all the items which are present in the dictionary

for i in data.items():
   print(i)


#this will print all the necessary keys from the list
for j in data.keys():
    print(j)

#this will print all the necessary values from the list
for k,i in data.items():
    print(k," : ",i)


print(data)
print('-'*50)


#Adding the data, updating and deleting the data

data[4] = {'name' : 'Payal' , 'phone' : 623738237}
print(data)
print('-'*50)

data[3]['name'] = 'Vivekanand Joshi' 
print(data)

#Delete the data from the dictionary
del (data[4])
print(data)

for i in data.keys():
    print(i,data[i]['name'], data[i]['phone'])
print('-'*50)


#Going level deeper with the dictionary 

data = {

    1 : {'name' : 'Vivekanand Joshi' , 'phone' : 2312356777 , 'marks': {'hindi':45 , 'math' : 97 , 'science ':78 }},
    2 : {'name' : 'Test' , 'phone' : 1238213123 , 'marks': {'hindi':55 , 'math' : 99 , 'science ':100 }},
    3 : {'name' : 'Abhishek Gawali' , 'phone' : 2312356744 , 'marks': {'hindi':89 , 'math' : 90 , 'science ':90 }},
    4 : {'name' : 'Riya Joshi' , 'phone' : 982313231 , 'marks': {'hindi':45 , 'math' : 99 , 'science ':78 }},

}
#printing the data
print(data)

#accessing all the elements from dictionary
for i in data.keys():
    print(i,data[i]['name'] , data[i]['marks'])
    
#Access the marks of hindi and also ensuring the data for the other products
total = 0
for i in data.keys():
    hindi_marks = data[i]['marks']['hindi']
    print(i,data[i]['name'] , data[i]['marks']['hindi'])
    total = total + hindi_marks

#this will print the data for the dictionary
print(total)

#Using default dict()
#The defaultdict from the collections module automatically creates sub-dictionaries
#whenever a new nested key is accessed

from collections import defaultdict
import json

d = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
d[2][3][4] = 1
print(json.dumps(d,indent=2))

#use of set default
#the set default method initializes a dictionary key with a default value if it doesn't already exists
d = {}
d.setdefault(1,{})[4] = 7
print(d)

#using the dictionary comprehension 
d = {i: {j : i*j for j in range(1,4)} for i in range(1,3)}
print(d)

#using manual initialization
#this mnethod will manually initialize each nested dictionary before assigning 
#values. It works, but it's more tedious as compared to the above approaches

d= {}
d[1] = {}
d[1][2] = {}
d[1][2][3] = 10
print(d)

