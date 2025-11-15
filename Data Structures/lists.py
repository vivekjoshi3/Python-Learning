#creating the lists
student_info = ['21',"Vivekanand Joshi",'CSE',20,30,50]
print(student_info)

#access every element present in the list
print("Student Roll No : ",student_info[0],end='')
print("Student Name : ",student_info[1],end='')
print("Student Subject: ",student_info[2],end='')
print("Student Marks : ",student_info[-1])

""" SLICING OF THE LISTS"""
student_info = [21, "Rose","CSE",20,30,40,50,120]
print(student_info[1:3])


#reverse a list using slicing
student_info = [21, "Rose","CSE",20,30,40,50,120]
print(student_info[::-1]) #Revesed list

#the answer for this will be that it will skip one element between and it will take the data with respect to next data.
print(student_info[::-2]) #Reversed List with the steps of 2

#Modifying lists
student_info = [21, "Rose","CSE",20,30,40,50,120]
student_info[2]="ME"
print(student_info)

#ADDING THE ELEMENTS IN THE LISt
student_info = [21, "Rose","CSE",20,30,40,50,120]
#append will add the data in the list which is present
student_info.append(70)
print(student_info)

#Removing the elements and for that we use remove()
student_info = [21, "Rose","CSE",20,30,40,50,120]
student_info.remove(50)
print(student_info)


#Concatenation
#Lists can be concatanated using the + operator
student_info = [21, "Rose","CSE",20,30,40,50,120]
student_info_1 = [22, "Vivekanand Joshi","Mechanical",40,50,60,80,120]
print(student_info+student_info_1)

#Repetition 
#LIsts can be repeated using the * operator
student_info= [21, "Rose","CSE",20,30,40,50,120]
print(student_info*2)
