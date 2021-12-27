import random
computer = random.randint(1,10)
user = 0
again = True

while again == True:
    while user != computer:
        user = int(input("please guess between 1-10:"))   
        if user < computer:
            print("The number is higher")
            pass
        elif user > computer:
            print("The number is lower")
            pass
    print("you win!")
    if again == True:
       x = input("Would you like to go again?")
       if x == "yes":
           break

    