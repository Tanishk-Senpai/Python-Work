while(True):
    inp = int(input("Enter any number: "))
    if inp >= 0:
        print("Try again")
        continue
    else:
        print("This number is less than 0") 
        break

