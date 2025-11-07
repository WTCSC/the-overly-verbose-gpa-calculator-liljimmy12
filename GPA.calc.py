"""
------------------------------------------------------------
Description:
    This program allows a user to input their grades (0.0–4.0 scale),
    calculates their GPA, analyzes their semester performance,
    and checks if their GPA goal is achievable.

    It uses functions to:
        - Collect and validate user input for grades
        - Compute overall GPA
        - Analyze GPA performance for different parts of the semester
        - Evaluate what changes would help reach a goal GPA

Date: 2025-11-07
------------------------------------------------------------
"""

# Function to repeatedly ask for a valid grade between 0.0 and 4.0
def get_valid_grade(index):
    while True:
        try:
            grade = float(input(f"enter grade (0.0 - 4.0): "))
            # Ensure the grade is within valid bounds
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("grade must be inbetween 0.0 and 4.0")
        except ValueError:
            print("invalid input. please enter a number.")


# Function to gather all grades from the user
def get_grades():
    while True:
        try:
            count = int(input("how many grades do you want to enter? "))
            # Require at least one grade
            if count > 0:
                break
            else:
                print("you have to have at least one class to get a GPA dummy.")
        except ValueError:
            print("enter a number.")

    # Create a list of grades entered by the user
    grades = [get_valid_grade(i) for i in range(count)]
    return grades


# Function to calculate GPA by taking the average of all grades
def calculate_gpa(grades):
    return sum(grades) / len(grades)


# Function to compare the GPA of one half of the semester to the overall GPA
def analyze_semester(grades, overall_gpa):
    choice = input("focus on first or second half of semester? (f/s): ").lower()
    mid = len(grades) // 2  # midpoint for dividing semester

    # Split grades into first or second half based on user choice
    if choice == "f":
        semester = grades[:mid]
    else:
        semester = grades[mid:]

    sem_gpa = calculate_gpa(semester)
    print(f"semester GPA: {sem_gpa:.2f}")

    # Compare semester GPA to overall GPA
    if sem_gpa > overall_gpa:
        print("you improved this semester!")
    elif sem_gpa < overall_gpa:
        print("grades dipped a bit, caffeine might help.")
    else:
        print("consistent performance. like a robot.")


# Function to determine if the user can reach their goal GPA
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

    # If goal is already met
    if goal <= overall_gpa:
        print(f"you’ve already achieved your goal GPA of {goal:.2f}. not that impressive.")
        return
    
    achievable = False

    # Test if raising any single grade to 4.0 would reach the goal
    for i in range(len(grades)):
        test_grades = grades.copy()
        test_grades[i] = 4.0
        new_gpa = calculate_gpa(test_grades)
        if new_gpa >= goal:
            print(f"if you raise grade #{i + 1} to 4.0, you’ll reach your goal GPA of {goal:.2f}. good luck.")
            achievable = True

    # If no single grade change can achieve the goal
    if not achievable:
        print(f"sorry its too late now, its not even possible to get {goal:.2f}. better luck next semester.")


# Main driver function
def main():
    print("GPA Calculator (for dummies)")
    grades = get_grades()
    overall_gpa = calculate_gpa(grades)
    print(f"\ncalculating... give me a sec...okay all done, your GPA is: {overall_gpa:.2f}")

    analyze_semester(grades, overall_gpa)
    goal_analysis(grades, overall_gpa)


# Run program if file is executed directly
if __name__ == "__main__":
    main()

