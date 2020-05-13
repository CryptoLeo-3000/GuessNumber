import random

def guessing():
    n = random.randint(-10,10)
    print(n)
    k = 0
    m = 0
    while k != 4:
        un = int(input("Enter your guess"))
        if un == n:
            print("You have Guessed the Correct Number")
            m = 0
            break
        elif un < n:
            print("The Number you have guessed is small compared to the number generated")
        else:
            print("The Number guessed is larger")

        m = m + 1
        k = k + 1
    
    if m != 0:
        print(f"Number Generated : {n}")

guessing()