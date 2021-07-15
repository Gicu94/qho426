#Declare an empty list
red = []

#Declare a on-empty lis
amber = ["Poland", "Portugal", "Romania", "Fiji", "Bulgaria"]

#Printing full list
print(amber)

#Print a single element
print(amber[3])

#Add elements to a list
red.append("Brazil")
red.append("Somalia")
red.append("Malta")

# for i in range(3):
#   red.append(input("Enter new red list country:  "))
print(red)

#Insert data onto a list not at the end
red.insert(1, "Gana")
print(red)
red.insert(3, "Switzerland")
print(red)

#Remove an item for the list
#red.remove("Somalia") 
red.remove(input("Which country to delete:"))
print(red)

#REmove an item from list by index
red.pop(0)
print(red)
# red.pop(1)
# print(red)
# new_amber_country = red.pop(1)
# amber.append(new_amber_country)
# print(red)
# print(amber)

#Delete an item
del red[1]
print(red)

#Slicing
print("---Slicing---")
print(amber[0::3])#zero it's not necesarilly to be put

#Slicing allows you to specifynstart point(include), and point (excluded) and steps.
a = [1, 2 ,3]
print(a[::-1])

#Strings in puthon are lists!!!!!!`