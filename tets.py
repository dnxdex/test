import fileinput
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
    try:
        file_name = input("Enter file name: \n")
        file = open(file_name + ".txt","x")
        file.close()
        print("File created")
    except FileExistsError:
        print("File already exists")


def write_to_file():
    try:
        file_name = input("Enter file name: \n")
        file = open(file_name + ".txt", "wt")
        text_to_write = input("Enter text to write: \n")
        file.write(text_to_write)
        file.close()
        print("File written")
    except FileNotFoundError:
        print("File doesnt exist")


while True:
    print("\n1. Check name \n"
          "2. Check age \n"
          "3. Set Player data \n"
          "4. Create custom robot \n"
          "5. Create file \n"
          "6. Write file \n"
          "7. Append file \n"
          "8. Exit \n")
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
    elif selected_task == 5:
        create_file()
    elif selected_task == 6:
        write_to_file()
    else :
        exit()