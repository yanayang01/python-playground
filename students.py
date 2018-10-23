# simple data entry program to practice manipulating data structures

# track the english and math grades of n students
# prints the average grade of the class
def calculate_average(marks):
    average = sum(marks) / len(marks) * 1.0
    return average

def grades():
    n = int(input("Enter the number of students: "))
    data = {}  # dictionary to store the data
    subjects = ('English', 'Math')  # subjects that we're going to track

    # nested for loops to get the marks for the students
    for i in range(0, n):
        name = input(f"Enter name of student {i+1}: ")
        marks = []  # list of marks
        
        for j in subjects:
            s = int(input(f"Enter student {i+1}'s mark in {j}: "))
            marks.append(s)
        
        data[name] = marks
    
    # for loop to calculate each student's average
    for i, j in data.items():
        student_average = calculate_average(j)
        print(f"{i}'s grade average is {student_average:.1f}")



grades()
# print(calculate_average(4, [90, 100, 90, 95]))