
def calculate_statistics(*grades, **student_info):
    if not grades:
        return 0, 0, 0, {}

    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return minimum, maximum, average, distribution


# Student details using keyword arguments
student = {
    "name": "Rahul",
    "roll_no": 101
}

# Assessment grades using positional arguments
minimum, maximum, average, distribution = calculate_statistics(
    85, 92, 78, 66, 95,
    **student
)

print("Student Name:", student["name"])
print("Roll Number:", student["roll_no"])
print("Minimum Grade:", minimum)
print("Maximum Grade:", maximum)
print("Average Grade:", round(average, 2))
print("Letter Grade Distribution:", distribution)
