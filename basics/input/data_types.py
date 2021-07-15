print("What is your name human?")
name = input()
#when you use input() function, the default data type is a string!
print("How old are you (in years)?")
user_age = int(input())

print("How tall are you (in metres)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input()) 

bmi = weight / (height **2)

#print(f"{name} you are {user_age} years old and your bmi is {bmi}")
# another way to solve the task. concatenations of strings (join togheter)
#print(name + " you are " + str(user_age) + " years old and your bmi is " + str(bmi))
 # 3rd example
print ("{} you are {} years old and your bmi is {:.2f}".format(name, user_age, bmi))