# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆


# Write your code below this line 👇


def bmi_formula(height_user, weight_user):
    height_in_number = float(height_user)
    weight_in_number = int(weight_user)
    height_in_number_calculated = height_in_number ** 2
    bmi_calculator_results = weight_in_number / height_in_number_calculated
    # print(float(bmi_calculator_results))
    if float(bmi_calculator_results) < 18.5:
        print(f"Your BMI is {round(bmi_calculator_results)}, you are underweight.")
    elif bmi_calculator_results > 18.5 and bmi_calculator_results < 25:
        print(f"Your BMI is {round(bmi_calculator_results)}, you have a normal weight.")
    elif bmi_calculator_results > 25 and bmi_calculator_results < 30:
        print(f"Your BMI is {round(bmi_calculator_results)}, you are slightly overweight.")
    elif bmi_calculator_results > 30 and bmi_calculator_results <35:
        print(f"Your BMI is {round(bmi_calculator_results)}, you are obese.")
    else:
        print(f"Your BMI is {round(bmi_calculator_results)}, you are clinically obese.")


bmi_formula(height, weight)