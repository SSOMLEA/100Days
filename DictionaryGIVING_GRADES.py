student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {

}



for key_checker in student_scores:
    student_grades[key_checker] = " "
    if student_scores[key_checker] <= 70:
        result = "FAIL"
        student_grades[key_checker] = result
    elif student_scores[key_checker] > 70 and student_scores[key_checker] <= 80:
        result = "Acceptable"
        student_grades[key_checker] = result
    elif student_scores[key_checker] > 80 and student_scores[key_checker] <= 90:
        result = "Exceeds Expectations"
        student_grades[key_checker] = result
    elif student_scores[key_checker] > 90 and student_scores[key_checker] <= 100:
        result = "Outstanding"
        student_grades[key_checker] = result





# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)