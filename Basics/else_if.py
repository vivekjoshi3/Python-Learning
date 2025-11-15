# if else condition apply
i=25

#checking whether the condition satisfies it or not
if i>15:
    print(i)
else:
    print("Finished traversing the no ")


#check and learn how you can write the ternary operator
a=-2

res = "Positive " if a>=2 else print("Negative")


#Logical operators with the If Else condition

age = int(input("PLease enter your age "))

output = "Age is bigger " if age>=25 else print("The age is smaller ")
print(output)


#check whether the nested if else statements can be worked upon

i=10
if i==10:

    #First if statement
    if i<15:
        print("i is smaller than 15 ")

    """
    NESTED IF ELSE CONDITION
    WILL ONLY BE EXECUTED  IF STATEMENTS ABOVE
    IT IS TRUE
    """
    if i<12:
        print(" i is smaller than 12 too ")
    else:
        print("i is bigger than 12  ")

else:
    print("i is not equal 10 ")


#WORKING ON THE ELIF CONDITION

i=10

if i==10:
    print(" i is equal to 10 ")

elif i==15:
    print(" i is equal to 15 ")

elif i==20: print("i is equal to 20 ")

else : print(" Neither of these values are correct  ")
