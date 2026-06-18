def calculate_average(grades: list[int|float]) -> float:
    try:
        average_grade = round(sum(grades) / len(grades), 2)
        return average_grade
    except ZeroDivisionError:
        return 0.0


def get_status(average_grade: float) -> str:
    return "Успешный" if average_grade >= 75 else "Отстающий"


def update_average_grade(students: list[dict]) -> None:
    average_grades = []
    for student in students:
        average_grade = calculate_average(student["grades"])
        average_grades.append(average_grade)

    print(f"\nОбщий средний балл: {calculate_average(average_grades)}")
    print("------------------")


def print_students(students: list[dict]) -> None:
    for student in students:
        average_grade = calculate_average(student["grades"])
        print(f"Студент: {student["name"]}",
              f"Средний балл: {average_grade}",
              f"Статус: {get_status(average_grade)}",
              "------------------",
              sep="\n")


def validate_name(name: str) -> bool:
    return True if name and type(name) is str else False


def validate_grades(grades: list[int]) -> bool:
    if type(grades) is not list:
        return False

    for grade in grades:
        if type(grade) is not int or not (grade >= 0 and grade <= 100):
            return False
    return True


def validate_student(student: dict) -> bool:
    return True if validate_name(student["name"]) and validate_grades(student["grades"]) else False


def add_student(students: list[dict], name: str, grades: list[int]) -> None:
    student = {"name": name, "grades": grades}
    if validate_student(student):
        students.append(student)
        print(f"\nСтудент {name} добавлен.")
    else:
        print("\nВведены некорректные данные при добавлении студента.\n")
        return

    update_average_grade(students)


def delete_worst_student(students: list[dict]) -> None:
    if not students:
        print("Студенты в списке отсутствуют.")
        return

    min_average_grade = 101
    min_index = -1
    for index in range(len(students)):
        average_grade = calculate_average(students[index]["grades"])
        if average_grade < min_average_grade:
            min_average_grade = average_grade
            min_index = index

    if min_index != -1:
        print(f"\nСтудент {students[min_index]["name"]} удален.")
        students.pop(min_index)

    update_average_grade(students)


students = [
    {"name": "Vlad", "grades": [20, 90]},
    {"name": "Vladik", "grades": [50]},
    {"name": "Vlados", "grades": [20, 30, 40]}
]

update_average_grade(students)
print_students(students)

add_student(students, "Vladosik", [70, 80, 90])
print_students(students)

delete_worst_student(students)
print_students(students)
