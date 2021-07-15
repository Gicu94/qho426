def room_area(width, length):
  return width*length

def room_name():
  return input("What is the name of the room? ")

def price(name, area):
  if name == "bathroom":
    return 20*area
  elif name == "bedroom":
    return 10*area
  elif name == "kitchen":
    return 5*area
  else:
    return 30*area

def run():
  name = room_name()
  print("What is the width of the room?")
  w = float(input())
  print("What is the length of the room?")
  l = float(input())
  area = room_area(w,l)
  cost = price(name, area)
  print("To paint {} you need to pay £{:.2f}".format(name, cost))