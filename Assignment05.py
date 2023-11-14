# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Jenna Ho,11/08/2023,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
import json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict[str:str] = {}  # one row of student data
students: list[dict[str]] = []  # a table of student data


try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    print("data loaded from the file")
except FileNotFoundError as e:
    print("file not found, creating new file")
    file = open(FILE_NAME, "w")
    json.dump(students, file)
except json.JSONDecodeError as e:
    print('wrong formatted file, please try again')
except Exception as e:
    print('no data in file, please try again')
finally:
    if not file.closed:
        file.close()


# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Error- First name can only be alphabetic")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Error- Last name can only be alphabetic")
            course_name = input("Please enter the name of the course: ")
        except ValueError as e:
            print(e)

        student_data = {"student_first_name": student_first_name, "student_last_name": student_last_name,
                        "course": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"{student_first_name} {student_last_name} is enrolled in {course_name}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except Exception as e:
            print('technical error found')
            file.close()
        finally:
            if not file.closed:
                file.close()
            continue
        print("The following data was saved to file!")
        for student in students:
            print(f"{Student["student_first_name"]}{student["student_first_name"]} "
                  f"is enrolled in {student["course_name"]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

    print("Program Ended")
