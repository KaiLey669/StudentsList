def calculate_average(grades: list) -> float:
    try:
        average_grade = round(sum(grades) / len(grades), 2)
        return average_grade
    except ZeroDivisionError:
        return 0

def get_status(average_grade: float) -> str:
    global status
    return status[0] if average_grade >= 75 else status[1]

def update_average_grade(students: list) -> None:
    average_grades = []
    global common_average_grade
    for student in students:
        if validate_student(student):
            average_grade = calculate_average(student["grades"])
            average_grades.append(average_grade)

    common_average_grade = calculate_average(average_grades)
    print(f"\nОбщий средний балл: {common_average_grade}")
    print("------------------")

def print_students(students: list) -> None:
    for student in students:
        if validate_student(student):
            average_grade = calculate_average(student["grades"])
            print(f"Студент: {student["name"]}",
                  f"Средний балл: {average_grade}",
                  f"Статус: {get_status(average_grade)}",
                  "------------------",
                  sep="\n")
        else:
            print("Ошибка в данных.\n------------------")

def validate_name(name: str) -> bool:
    return True if len(name) > 0 else False

def validate_grades(grades: list) -> bool:
    if not len(grades):
        return True

    for grade in grades:
        if type(grade) not in [int, float] or not (grade >= 0 or grade <= 100):
            return False
    return True

def validate_student(student: dict) -> bool:
    return True if validate_name(student["name"]) and validate_grades(student["grades"]) else False

def add_student(students: list, name: str, grades: list) -> None:
    global common_average_grade
    student = {"name": name, "grades": grades}
    if validate_student(student):
        students.append(student)
        print(f"\nСтудент {name} добавлен.")
    else:
        print("Введены некорректные данные при добавлении студента.")
        return

    update_average_grade(students)

def delete_worst_student(students: list) -> None:
    if not students:
        return

    min_average_grade = 101
    average_grades = []
    for student in students:
        if validate_student(student):
            average_grade = calculate_average(student["grades"])
            average_grades.append(average_grade)
            if average_grade < min_average_grade:
                min_average_grade = average_grade

    for index in range(len(average_grades)):
        if average_grades[index] == min_average_grade:
            print(f"\nСтудент {students[index]["name"]} удален.")
            students.pop(index)
            break

    update_average_grade(students)


students = [
    {"name": "Vlad", "grades": [20, 90]},
    {"name": "Vladik", "grades": [50]},
    {"name": "Vlados", "grades": [20, 30, 40]}
]
status = ["Успешный", "Отстающий"]
threshold_grade = 75
common_average_grade = 0
update_average_grade(students)
print_students(students)

add_student(students, "Vladosik", [80, 100, 30])
print_students(students)

delete_worst_student(students)
print_students(students)
