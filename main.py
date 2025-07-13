import random

    

x=int(input("Enter the max  value of Target:  "))
attempts=0
def check(x):
    
    target = (random.randint(1,x))
    global attempts
    attempts=0
    while True: 
        try:
            inp=int(input("Enter your guess:  "))
            attempts+=1
            if inp==target:
                print("You won!")
                print(f"attempts={attempts}")
                
                break
            elif inp< target:
                print ("Target is larger than your guess.")
            elif inp> target:
                print ("Target is smaller than your guess.")
        except ValueError :
            print("Invalid input")   
            
while True:
    check(x)
    try:
        a=int(input("Press 1 to play again or any other key to quit:  "))

        if a!=1:
            print("Bye Bye")
            break
    except ValueError:
        print("Bye Bye")
        break