
def isPrime(number):
  for thing in range(2,number):
    if number % thing == 0:
      return False
  return True

def findPrime(start,end):
  for stuff in range(start, end+1):
    if isPrime(stuff):
      return stuff

def encrypt():
  x= int(input("Provide an integer: "))
  y= int(input("Provide a second integer (larger): "))
  p1 = findPrime(x,y)
  x1= int(input("Provide an integer: "))
  y1= int(input("Provide a second integer (larger): "))
  p2 = findPrime(x1,y1)
  return p1*p2
  
print(encrypt())