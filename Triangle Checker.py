# Program to check wheather sides taken as input are of triangle or not
while (True):
      Side1 = float(input("Enter the first side of triangle: ")) 
      Side2 = float(input("Enter the second side of triangle: "))
      Side3 = float(input("Enter the third side of triangle: "))
      if Side1+Side2>Side3:
            if Side2+Side3>Side1:
                  print("It is a triangle")
                  break
            else:
                  print("It is not a triangle")
                  break
      else:
            print("It is not a triangle")