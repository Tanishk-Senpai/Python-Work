i = int(input("Enter a number from 1 to 50: "))
while i<51:
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
        break
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print("Try again!")
    break