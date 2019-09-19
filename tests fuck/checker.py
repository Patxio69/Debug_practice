import json

#variable assignment room
#int var

saved_array = []
start_with = "you have" + str(saved_array)
array = []
print("how many interations?")
val = input()

def value():
    value = 2

#ing fucc
def inter_n():    #test block 1
    n = 0
    while True:
        print("enter value")
        count = input(int())
        array.append(count)  #modify so if a string value is entred, it checkes
        if str(count) == "done":
            break  # after that the array is loaded
    print("enter how many times")
    count_entry = input(int())

    if int(count_entry) > 0:
        for looper in range(count_entry):
            num = 0
            while num == 10:
                num = num + value

    elif int(count_entry) == 0:
        return "write somethign"

    n = len(array)
    return n


                 
