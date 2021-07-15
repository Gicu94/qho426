# print("Hello World\nGheorghe")
# status = int(input("Enter status: "))
# #starting if comand
# if status == 1:
#  print("The status was 1")
#  print("This always prints")

# #another example

# age = int(input("What is your age: "))

# if age < 20:
#   print("You are a child")
# elif age > 65:
#   print("You are old mate")
# elif age < 30 and age >= 20:
#   print("You are a grown up child")
# else:
#   print("You are an adult")


#example nr3
while True:
  print("Please choose an option\n\n1-Nice message\n2-Area of a rectangle\n3-Area of a triangle\n4-Multiplication table")

  option = int(input())

  if option == 1:
    print("You don't smell so bad today")
  elif option == 2:
    print("Enter the length of the rectangle ")
    l = float(input())
    w = float(input("Enter the height of the rectangle "))
    print("Are of this rectangle is {:.2}" .format(l*w))
  elif option == 3:
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    print("Area of this triangle is {:.2f}" .format(b*h/2))
  elif option == 4:
    pass
#     n = int(input("Enter the number: "))
#  counter = 1


#  n2 = int(input("Enter te limit of the table: "))

# while counter <= n2:
#     print(f"{n}x{counter} = {counter*n}")
#     counter +=1

  else:
    print("Go to Specsavers!")