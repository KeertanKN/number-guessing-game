import random 
while True:
    print("Choose Difficulty")
    print("1. Easy")
    print("2. medium")
    print("3. hard")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        number = random.randint(1,100)
    elif choice == 2:
        number = random.randint(1.400)
    elif choice == 3:
        number = random.randint(1, 800)
    else:
        print("Invalid input enter between(1 - 3)")
        continue
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
            print(f"You got number in {k} attempts")
            break