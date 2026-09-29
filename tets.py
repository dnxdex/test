from operator import truediv
from traceback import print_tb

def check_name():
    print("Enter Name")
    name = input()
    print (f"your name is {name}")

def create_custom_robot():
    eyes = input("Enter custom eyes for robot: \n")
    print("##########")
    print(f"#  {eyes}  {eyes}  #")
    print ("# ------ #")
    print("##########")

def check_age():
    age = str(input("Enter Age: \n"))
    print(f"your age is {age}")

def set_player_data():
    lives = int(input("Enter Lives: \n"))
    energy_level = int(input("Enter Energy Level: \n"))
    shield = int(input("Enter Shield: \n"))

    print("Lives: ", end = " ")
    for i in range(0,lives):
        print("♥", end = " ")
    print()

    print("Energy Level: ", end = " ")
    for j in range(0, energy_level):
        print("◆", end = " ")
    print()

    print("Shield: ",end = " ")
    for k in range(0, shield):
        print("❖", end = " ")
    print()

def create_file():
    print("h")

while True:
    print("\n1. Check name \n"
          "2. Check age \n"
          "3. Set Player data \n"
          "4. Create custom robot \n"
          "5. Exit \n")
    print("Enter your number for task:")
    selected_task = int(input())
    if selected_task == 1:
        check_name()
    elif selected_task == 2:
        check_age()
    elif selected_task == 3:
        set_player_data()
    elif selected_task == 4:
        create_file()
    else :
        exit()