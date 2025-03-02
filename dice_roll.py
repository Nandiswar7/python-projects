# import random
# x = "y"
# while x == "y":
#     no = random.randint(1,6)

#     if no == 1:
#         print("[-----]")
#         print("[     ]")
#         print("[  0  ]")
#         print("[     ]")
#         print("[-----]")
#     if no == 2:
#         print("[-----]")
#         print("[ 0   ]")
#         print("[     ]")
#         print("[   0 ]")
#         print("[-----]")
#     if no == 3:
#         print("[-----]")
#         print("[ 0   ]")
#         print("[  0  ]")
#         print("[   0 ]")
#         print("[-----]")
#     if no == 4:
#         print("[-----]")
#         print("[ 0 0 ]")
#         print("[     ]")
#         print("[ 0 0 ]")
#         print("[-----]")
#     if no == 5:
#         print("[-----]")
#         print("[ 0 0 ]")
#         print("[  0  ]")
#         print("[ 0 0 ]")
#         print("[-----]")
#     if no == 6:
#         print("[-----]")
#         print("[ 0 0 ]")
#         print("[ 0 0 ]")
#         print("[ 0 0 ]")
#         print("[-----]")
#     print()
#     x = input("enter y to roll again and n for exit : ")
#     print("\n")


#or 
#another code for dice roll

import random
x = "y"
while(x == "y"):
    no = random.randint(1,6)
    if no == 1:
        print("1")
    if no == 2:
        print("2")
    if no == 3:
        print("3")
    if no == 4:
        print("4")
    if no == 5:
        print("5")
    if no == 6:
        print("6")
    x = input("enter the y for roll and no for exit : ")
    print()