import json



#playing with the value of 3 n

#variable assignment room

saved_array = []
start_with = "you have" + str(saved_array)
array = []
print("how many interations?")
val = input()

def value():
    value = 2

#ing fucc
def inter_n():    #test block 1 and this is a static func
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
        for looper in range(int(count_entry)):
            num = 0
            while num < 10:
                num = num + num #Yeah I AGREE this looks really bad
                num = num + value #I just can't fucking see how bad it looks
                return "this is your result" + num
                print("do you want to save them?")
                response = input()
                if response == "yes":
                    array.append(num)
                
                elif response == "no":
                    return "ok"

    elif str(count_entry) == "later":
        print("warning! The list might be empty")

    print("checking the list!")
    n = len(array)
    if int(n) == 0:
        return "it's empty"
    elif int(n) > 0:
        for something in range(int(n)):
            for lol in array:
                re_val = ["id" + str(something) + " list is" + str(lol)]

def inter_n1(arg):

                 
# fucktion interation down here

