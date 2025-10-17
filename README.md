[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21077909)
# GPA Calculator
A GPA calculator to make it easier for you to see your over all GPA                                                                                                                                                    
Just enter in your grades and find your GPA

## Features
- Input multiple grades on a 0.0 – 4.0 scale.
- Validate input to prevent invalid entries.
- Calculate your GPA.
- Check for first and second semester
- Calculate what it will take to get to a goal of yours.

## Requirements
must have `python 3` installed

## Running the program
1. Clone the repository or download the Python file.
2. Open a terminal in the directory containing the file.
3. Run the program: `python gpa_calculator.py`
4. Follow the instructions it give you:
   - Enter the number of grades.
   - Input each grade (0.0 – 4.0).
   - Choose which half of the semester you want to check.
   - Enter your GPA goal to see if it’s achievable.
  
## Example
<img width="1044" height="433" alt="image" src="https://github.com/user-attachments/assets/3d973e90-8803-4dc0-ac8e-9fbe8658e122" />

## Notes
- Grades must be between 0.0 and 4.0.
- GPA goals are also limited to 0.0 – 4.0.
- The program gives suggestions to improve grades for achieving goals.

# Decision tree
Start                                                                                                                                                                              
 |                                                                                                                                        
main()                                                                                                                      
 |                                                                                                                              
print("GPA Calculator")                                                                                                          
 |                                                                                                      
grades = get_grades()                                                                                                  
 |                                                                                                      
Ask: "How many grades?"                                                                                            
 |                                                                                          
Invalid input? -> repeat                                                                                      
 |                                                                                                
Loop each grade -> get_valid_grade(index)                                                                                            
 |                                                                                                                
Ask: "Enter grade 0.0-4.0"                                                                                                    
 |                                                                                              
Invalid input? -> repeat                                                                                                                                          
 |                                                                                        
Valid grade? -> add to list                                                                                                                  
 |                                                                                                            
overall_gpa = calculate_gpa(grades)                                                                                    
 |                                                                                          
print overall_gpa                                                                                                                                                  
 |                                                                                                      
analyze_semester(grades, overall_gpa)                                                                                      
 |                                                                                      
Ask: "Focus on first or second half? (f/s)"                                                                                        
 |                                                                                                                                      
choice 'f'? first half : second half                                                                                                    
 |                                                                                                                            
sem_gpa = calculate_gpa(semester)                                                                                                        
 |                                                                                                
sem_gpa > overall_gpa? -> "You improved!"                                                                                                        
 |                                                                                                      
sem_gpa < overall_gpa? -> "Grades dipped, caffeine might help"                                                                                                    
 |                                                                                                        
sem_gpa == overall_gpa? -> "Consistent performance"                                                                                            
 |                                                                                                                    
goal_analysis(grades, overall_gpa)                                                                                            
 |                                                                                                
Ask: "Enter goal GPA 0.0-4.0"                                                                                                    
 |                                                                                                                        
Invalid input? -> repeat                                                                                                                                
 |                                                                                                                            
goal <= overall_gpa? -> "Goal already achieved"                                                                                                                              
 |                                                                                                                                
Loop grades                                                                                                                                  
 |                                                                                                                                                
Replace grade with 4.0                                                                                                                        
 |                                                                                                                    
new_gpa = calculate_gpa(test_grades)                                                                                                              
 |                                                                                                                                      
new_gpa >= goal? -> print advice                                                                                                                                
 |                                                                                                                                    
If none achievable? -> "Too late, better luck next semester"                                                                                                                                          
 |                                                                                                                                                      
End                                                                                                                          
