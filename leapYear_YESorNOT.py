# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


def leap_year_calculation(user_input):
    year_to_check = int(user_input)
    #Foarte important la conditia de IF cum verificam daca dupa ce impartim imputul la x numar
    #este un numar cu virgula sau nu,
    #se imparte inputu (ex 2100) la 400 = 5.25
    #apoi ii dam %1 pentru ca sa imparta 5.25 - 1 pana ramane cui 0.25 apoi punem conditia == 0 ca sa
    #verificam daca ne o impartit tot numarul pana la capat sau daca nu, ramanem cu .25 este float
    if (year_to_check / 4) % 1 == 0:
        if (year_to_check / 100) % 1 != 0:
            if (year_to_check / 400) % 1 != 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")

leap_year_calculation(year)


#exemplu de cum sa vezi daca un imput impartit la un numar este int sau float
#def isInt(x):
    #if x % 1 == 0:
        #print
        #"X is an integer"
    #else:
        #print
        #"X is not an integer"