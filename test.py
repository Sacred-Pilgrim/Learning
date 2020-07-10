# ANSWERS FOR LOGICAL OPERATORS & DECISION MAKING EXERCISE QUIZ

# How many logical Operators can python support (including mathematical operations)?
# ANSWER: 9

# Which of the following variations of if-statements does python support?
# ANSWER: All except Switch statements

# Switch Statements are...Similar to if statements

# The and operator in python is...used to determine if whether both test conditions are true

# To simulate the use of switch statements in python one can...use functions, if-statements, dictionaries and any other possible technique needed



# Write a program that will print "You are now an adult" 
# if the user provides age that is greater than or equals to 18

# ANSWER
# inValue = input("Enter age: ")
# age = int(inValue)
# if age>=18:
#     print("You are now an adult")



# Extending the previous question, Write a program that will print 
# "You are now an adult" if the user provides age that is 
# greater than or equals to 18 or print "you are under age" 
# if the user provides any value greater 0.

# ANSWER
# inValue = input("Enter age: ")
# age = int(inValue)
# if age>=18:
#     print("You are now an adult")
# else:
#     print("You are under age")



# Write a program using nested if-statements that will print 
# "You can now apply for varsity" if the user provides age that is 
# greater than or equals to 16. The program must have an inner 
# if-statement that will check the value of a distinction variable like this: 
# if distinction:
#   print("You can now apply for varsity")    


# ANSWER
# inValue = input("Enter age: ")
# age = int(inValue)
# distinction = True
# if age>=16:
#     if distinction:
#         print("You can now apply for varsity")




# Write a program using chained if-statements that will print 
# "You are now a python programmer" if the user provides age that is 
# greater than 0, print ("invalid input") if age is less than or equal to 0 or 
# print(" you not to old to be a  programmer") if age is greater than 30

# ANSWER
# inValue = input("Enter age: ")
# age = int(inValue)
# if age>0:
#     print("You are now a python Programmer")
# elif age<=0:
#     print ("invalid input")
# elif age>30:
#     print(" you not to old to be a  programmer")
