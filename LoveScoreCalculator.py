# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_case_combined_names = combined_names.lower()
t = lower_case_combined_names.count("t")
r = lower_case_combined_names.count("r") #1
u = lower_case_combined_names.count("u") #2
e = lower_case_combined_names.count("e") #1
true = t + r + u + e

l = lower_case_combined_names.count("l") #1
o = lower_case_combined_names.count("o")
v = lower_case_combined_names.count("v")
e = lower_case_combined_names.count("e") #1
love = l + o + v + e

love_score = int(str(true) + str(love))
if(love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")