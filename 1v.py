#hallo

#print("you start on 1,1 you can go N")
#initial_in = input("input your direction")
position = 1

while True:
    if position == 4:
        new_position = input("You can travel: (N)orth or (E)ast or (S)outh. ")
        if new_position.upper() == "N":
            print(" your position is 1,3")
            position = 7
        elif new_position.upper() == "S":
            print(" your position is 1,1")
            position = 1
        elif new_position.upper() == "E":
            print(" your position is 2,2")
            position = 5
        else:
            print("Not a valid direction!")

    if position == 1:
        new_position = input("You can travel: (N)orth ")
        if new_position.upper() == "N":
            print(" your position is 1,2")
            position = 4
        else:
            print("Not a valid direction!")

    if position == 5:
        new_position = input("You can travel: (S)outh or (W)est. ")
        if new_position.upper() == "S":
            print(" your position is 2,2")
            position = 2
        elif new_position.upper() == "W":
            print(" your position is 1,2")
            position = 4
        else:
            print("Not a valid direction!")

    if position == 2:
        new_position = input("You can travel: (N)orth. ")
        if new_position.upper() == "N":
            print(" your position is 2,2")
            position = 5
        else:
            print("Not a valid direction!")

    if position == 7:
        new_position = input("You can travel: (S)outh or (E)ast. ")
        if new_position.upper() == "S":
            print(" your position is 1,2")
            position = 4
        elif new_position.upper() == "E":
            print(" your position is 2,3")
            position = 8
        else:
            print("Not a valid direction!")

    if position == 8:
        new_position = input("You can travel: (E)ast or (W)est. ")
        if new_position.upper() == "E":
            print(" your position is 3,3")
            position = 9
        elif new_position.upper() == "W":
            print(" your position is 1,3")
            position = 7
        else:
            print("Not a valid direction!")

    if position == 9:
        new_position = input("You can travel: (S)outh or (W)est. ")
        if new_position.upper() == "S":
            print(" your position is 3,2")
            position = 6
        elif new_position.upper() == "W":
            print(" your position is 2,3")
            position = 8
        else:
            print("Not a valid direction!")

    if position == 6:
        new_position = input("You can travel: (N)orth or (S)outh. ")
        if new_position.upper() == "N":
            print(" your position is 3,3")
            position = 9
        elif new_position.upper() == "S":
            print(" your position is 3,1")
            position = 3
        else:
            print("Not a valid direction!")

    if position == 3:
        print("Victory!")
        break





