stud_name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
dob = (input("Enter D.O.B: "))
school_name = input("Enter school name: ")

subject_list = []
marks_list = []
ch = int(input("Enter choice: \n 1. Enter subjects \n 2. Print Report Card \n"))
if ch == 1:
    subj = input("Subject: ")
    marks = int(input("Marks Obtained from 100: "))

    x = True
    while x == True:
        ch1 = int(input("Enter choice: \n 1. Enter more subjects \n 2. Print Report Card \n"))
        if ch1 == 1:
            subj = input("Subject: ")
            subject_list.append(subj)
            marks = int(input("Marks obtained from 100: "))
            marks_list.append(marks)
            continue
        if ch1 == 2:
            zip_iterator = zip(subject_list, marks_list)
            dictionary = dict(zip_iterator)
            print("                          Marksheet of class 10           ")
            print("                 Central Board of Secondary Education    ")
            print("Student Name:", stud_name)
            print("Roll Number: ", roll_no)
            print("Date of Birth: ", dob)
            print("School Name: ", school_name)
            print("-----------------------------------------")
            print("Subject_Name: ", subj)
            print("Marks_Obtained: ", marks)
            for key, value in dictionary.items():
                print(key,'-------', str(value))
        break

elif ch == 2:
    print("                          Marksheet of class 10           ")
    print("                 Central Board of Secondary Education    ")
    print("Student Name: ", stud_name)
    print("Roll Number: ", roll_no)
    print("Date of Birth: ", dob)
    print("School Name: ", school_name)

else:
    print("Incorrect option")
