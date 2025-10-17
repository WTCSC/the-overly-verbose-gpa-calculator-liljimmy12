def get_valid_grade(index):
    while True:
        try:
            grade = float(input(f"enter grade (0.0 - 4.0): "))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("grade must be inbetween 0.0 and 4.0")
        except ValueError:
            print("invalid input. please enter a number.")


def get_grades():
    while True:
        try:
            count = int(input("how many grades do you want to enter? "))
            if count > 0:
                break
            else:
                print("you have to have at least one class to get a GPA dummy.")
        except ValueError:
            print("enter a number.")
    grades = [get_valid_grade(i) for i in range(count)]
    return grades

def calculate_gpa(grades):
    return sum(grades) / len(grades)

def analyze_semester(grades, overall_gpa):
    choice = input("focus on first or second half of semester? (f/s): ").lower()
    mid = len(grades) // 2
    if choice == "f":
        semester = grades[:mid]
    else:
        semester = grades[mid:]
    sem_gpa = calculate_gpa(semester)
    print(f"semester GPA: {sem_gpa:.2f}")

    if sem_gpa > overall_gpa:
        print("you improved this semester!")
    elif sem_gpa < overall_gpa:
        print("grades dipped a bit, caffeine might help.")
    else:
        print("consistent performance. like a robot.")

def goal_analysis(grades, overall_gpa):
    while True:
        try:
            goal = float(input("enter your goal GPA (0.0 - 4.0): "))
            if 0.0 <= goal <= 4.0:
                break
            else:
                print("goal must be between 0.0 and 4.0. keep it realistic.")
        except ValueError:
            print("please enter a number, not a dream.")

    if goal <= overall_gpa:
        print(f"you’ve already achieved your goal GPA of {goal:.2f}. not that impressive.")
        return
    
    achievable = False
    for i in range(len(grades)):
        test_grades = grades.copy()
        test_grades[i] = 4.0
        new_gpa = calculate_gpa(test_grades)
        if new_gpa >= goal:
            print(f"if you raise grade #{i + 1} to 4.0, you’ll reach your goal GPA of {goal:.2f}. good luck.")
            achievable = True

    if not achievable:
        print(f"sorry its too late now, its not even possible to get {goal:.2f}. better luck next semester.")

def main():
    print("GPA Ccalculator (for dummies)")
    grades = get_grades()
    overall_gpa = calculate_gpa(grades)
    print(f"\ncalculating... give me a sec...okay all done, your GPA is: {overall_gpa:.2f}")

    analyze_semester(grades, overall_gpa)
    goal_analysis(grades, overall_gpa)


if __name__ == "__main__":
    main()



