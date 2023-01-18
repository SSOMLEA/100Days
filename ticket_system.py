print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
# ///////////////////////////////////////////////

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are  $7.")
    elif age <= 44:
        bill = 12
        print("Adult tickets are $12.")
    elif age >= 45 and age < 55:
        bill = 0
# /////////////////////////////////////////////////
    wants_photo = input("Do you want a photo ticket? Y or N")
    if wants_photo == "Y":
        bill += 3
# CODITION IF USER IS AN OLD HUMAN BETWEEN 45 - 55 EVERYTHING IS FREE

# ////////////////////////////////////////////////////
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
