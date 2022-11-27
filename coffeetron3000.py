coffee_types = ["ESPRESSO", "DOPPIO", "LUNGO", "RISTERTTO", "MACCHIATO", "CORRETO",
                "CON PANNA", "ROMANO", "CAPPUCCINO", "AMERICANO", "CAFFELATTE",
                "FLAT WHITE", "MAROCCHINO", "MOCHA", "BICERIN", "BREVE", "raf coffee",
                "MEAD RAF", "VIENNA COFFEE", "CHOCOLATE MILK", "LATTE MACCHIATO",
                "GLACE", "FREDDO", "IRISH COFFEE", "FRAPPE", "CAPPUCCINO FREDDO",
                "CARAMEL FRAPPE", "ESPRESSO LACCINO"]

print("\x1B[3m" + "Hello you! Im Coffeetron-3000" + "\x1B[0m")
print("\x1B[3m" + "I use a secret and super difficult calculation" + "\x1B[0m")
print("\x1B[3m" + "to decipher what coffee you need depending on" + "\x1B[0m")
print("\x1B[3m" + "the time of day you need it. all you need is" + "\x1B[0m")
print("\x1B[3m" + "to answer some questions for me:" + "\x1B[0m")

name =  input("first, how shall I call you?")
time = input("Now, please insert time HH:MM format: ")
# time input validation ------------------------------------------------------------------------------------------------
while True:
    if len(time) == 5:
            if time[2] != ":":
                print("Invalid format, Please insert time HH:MM format:")
                time = input()
            else:
                hours, minutes= time.split(":")
                if hours.isdigit() and minutes.isdigit():
                    hours = int(hours)
                    minutes = int(minutes)
                    if hours < 0 or 23 < hours:
                        print("Impossible amount of hours, please insert time again:")
                        time = input()
                    elif minutes < 0 or 59 < minutes:
                        print("Impossible amount of minutes, please insert time again:")
                        time = input()
                    else:
                        break
                else:
                    print("Can't read this format, Please insert time HH:MM format:")
                    time = input()
    elif len(time) == 4 and ":" not in time and time.isdigit():
        time = time[:2] + ":" + time[2:]
    else:
        print("Can't read this format, Please insert time HH:MM format:")
        time = input()

# amount of coffees in order row_check -------------------------------------------------------------------------------------
while True:
    amount_of_friends = input("How many coffees do we need?")
    if amount_of_friends.isdigit():
        amount_of_friends = int(amount_of_friends)
        if amount_of_friends < 1:
            print("I think you had a typo, it has to be at least 1")
        else:
            break
    else:
        print("I need a number here, let's try again!:")

# Bonus 2 - enabling user to pop out a type of coffee from the types list-----------------------------------------------

hate_it = input("Is there any type of coffee you don't want to have?").lower()
while hate_it != "yes" and hate_it != "no":
    hate_it = input(" It's more of a yes or no kinda question...?").lower()
while hate_it == "yes":
    pop_num = input("Really? which one?")
    if pop_num.isdigit():
        pop_num = int(pop_num)
        if 0 < pop_num <= 28:
            coffee_types.pop(pop_num-1)
            hate_it = input("another one?").lower()
            if hate_it == "no":
                break
            else:
                continue
        print("should be between 1-28")
    else:
        print("invalid input lets try again")

#Bonus 1 - enabling user to start the count from a different type of coffee in the list---------------------------------

option = input("you know the list... wanna choose a starting number?").lower()
while option != "yes" and option != "no":
    option = input(" It's more of a yes or no kinda question...?").lower()
while option == "yes":
    add_hours = int(input("now choose a number between 1-28:"))
    if 0 < add_hours < 28:
        hours = hours +(add_hours-1)
        break
    else:
        print("should be between 1-28")
        continue

# building the order in a new list first making calculating which coffee when minutes are over 28 -----------------------

order = []
friends_counter = 0
if hours == 0:
    hours = 24
what_coffee = hours - 1
order.append(what_coffee)
while friends_counter < amount_of_friends-1:
    friends_counter = friends_counter + 1
    what_coffee = what_coffee + minutes
    if what_coffee > len(coffee_types):
        what_coffee = what_coffee % len(coffee_types)
        order.append(what_coffee)
    else:
        order.append(what_coffee)

# crossing the order with the (maybe edited) coffee types list (seen a way to use list comprehension so I tried it,-----
# not sure if its actually more useful than a 3 liner for loop) -------------------------------------------------------
final = [coffee_types[x] for x in order]
# refining the list by making sure if the same coffee is printed twice it prints it in a comfortable way to read--------
realfinal=[]
for x in final:
    if final.count(x) == 1:
        realfinal.append(x)
        realfinal.append(final.count(x))
    elif final.count(x) > 1:
        if x in realfinal:
            pass
        else:
            realfinal.append(final.count(x))
            realfinal.append(x)
print(name, "'s order is", realfinal)



