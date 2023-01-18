# 1year = 365 days
# 1year = 52 weeks
# 1year = 12 months

age = input("whats your current age: ")


def age_calculator(user_age):
    # preDefined values for 90 years, values coming from the exercise
    max_life_age = 90
    max_life_days = max_life_age * 365
    max_life_weeks = max_life_age * 52
    max_life_months = max_life_age * 12
    # calculation of user input age in years/days/months

    days_calculated_by_year = int(user_age) * 365
    weeks_calculated_by_year = int(user_age) * 52
    months_calculated_by_year = int(user_age) * 12

    # calculation of remaning years/days/month using max years 90 - values inputed by user

    remaining_days_of_living = max_life_days - days_calculated_by_year
    remaining_weeks_of_living = max_life_weeks - weeks_calculated_by_year
    remianing_months_of_living = max_life_months - months_calculated_by_year

    print(
        f"You have {remaining_days_of_living} days, {remaining_weeks_of_living} weeks, and {remianing_months_of_living} months left.")


age_calculator(age)