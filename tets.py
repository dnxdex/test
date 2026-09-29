from traceback import print_tb

print("Enter Name")
name = input()
print (f"your name is {name}")

eyes = input("Enter custom eyes for robot: \n")
print("##########")
print(f"#  {eyes}  {eyes}  #")
print ("# ------ #")
print("##########")

age = str(input("Enter Age: \n"))
print(f"your age is {age}")

Lives = int(input("Enter Lives: \n"))
Energy_Level = int(input("Enter Energy Level: \n"))
Sheild = int(input("Enter Sheild: \n"))

print("Lives: ", end = " ")
for i in range(0,Lives):
    print("♥", end = " ")
print()

print("Energy Level: ", end = " ")
for j in range(0, Energy_Level):
    print("◆", end = " ")
print()

print("Sheild: ",end = " ")
for k in range(0, Sheild):
    print("❖", end = " ")
print()
