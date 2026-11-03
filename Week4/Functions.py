import random as rnd


def random_number(min,max):
    num = rnd.randint(min, max)
    return num


min = 0
max = 0


def get_min_max():
    min = int(input("Enter the minimum number: "))
    max = int(input("Enter the maximum number: "))
    return (min, max)


continue_ = True
while continue_ :
    min, max = get_min_max()
    print(f"I am thinking of a number between {min} and {max}. Can you guess what it is?\n")
    num = random_number(min,max)
    guess = 0
    while guess != num:
        guess = int(input("Enter guess: "))
        if guess < num:
            print("num too low")
        elif guess > num:
            print("num too high")
        else:
            print("You have guessed the correct number")
    if input("Continue y,n: ") != "y":
        continue_ = False
