# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


def odd_or_even_number(user_input):
    check_if_number_is_odd_or_not = user_input % 2
    if check_if_number_is_odd_or_not > 0:
        print("This is an odd number")
    else:
        print("This is an even number.")


odd_or_even_number(number)