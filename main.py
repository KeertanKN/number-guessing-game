import random 
number = random.randint(1,100)
k=0
while True:
    guess = int(input("Enter the guess : "))
    k = k+1
    if guess > number:
        print("to high! ")
    elif guess < number:
        print("too low!")
    else:
        print("Correct guess! ")
        print("You got number in "+str(k)+" ateempts")
        break