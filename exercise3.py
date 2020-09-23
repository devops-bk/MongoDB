Student = [{"SNo" : 1, "Name" : "Bhavya", "Last_name" : "Kothari", "Class" : "12", "Section" : "A", "Subjects":
    [{"Sub_name": "Math", "Total_marks" : "100", "Marks" : "95", "Rating": "A+"},
     {"Sub_name": "English", "Total_marks" : "100", "Marks" : "85", "Rating": "B+"},
     {"Sub_name": "Science", "Total_marks" : "100", "Marks" : "84", "Rating": "B"}
     ]
            },
           {"SNo" : 2, "Name" : "Minul", "Last_name" : "Jain", "Class" : "10", "Section" : "B", "Subjects":
               [{"Sub_name": "Math", "Total_marks" : "100", "Marks" : "85", "Rating": "B+"},
                {"Sub_name": "English", "Total_marks" : "100", "Marks" : "88", "Rating": "B+"},
                {"Sub_name": "Science", "Total_marks" : "100", "Marks" : "74", "Rating": "C"}
                ]
            },
           {"SNo" : 3, "Name" : "Palak", "Last_name" : "Mishra", "Class" : "8", "Section" : "C", "Subjects":
               [{"Sub_name": "Math", "Total_marks" : "100", "Marks" : "78", "Rating": "C+"},
                {"Sub_name": "English", "Total_marks" : "100", "Marks" : "81", "Rating": "B"},
                {"Sub_name": "Science", "Total_marks" : "100", "Marks" : "88", "Rating": "B+"}
                ]
            }
           ]

def add_student():
    data = {}
    SNo1 = int(input("Enter S.No: "))
    Name1 = input("Enter Student Name: ")
    Last_name1 = input("Enter Last name: ")
    Class1 = input("Enter Class: ")
    Section1 = input("Enter Section: ")
    data["SNo"]=SNo1
    data["Name"]=Name1
    data["Last_name"]=Last_name1
    data["Class"]=Class1
    data["Section"]=Section1
    Student.append(data)
    print("--------------------------")
    print("Student Data Inserted successfully")
    print("--------------------------")
    return

def update_student():
    x = True
    while x == True:
        A = int(input("Enter your choice of updation accordingly \n 1. Name updation \n 2. Last_Name Updation \n 3. Class updation \n 4. Section Updation\n 5. Exit \n"))
        if A == 1:
            Name = input("Enter the name you want it to get updated: ")
            up_name = input("Enter the updated name: ")
            index = 0            # Python's indexing starts at zero
            for i in Student:
                if i["Name"] == Name:
                    Student [index]["Name"] = up_name
                    index+=1
                else:
                    index+=1

        elif A == 2:
            Last_name = input("Enter the last name you want it to get updated: ")
            up_lname = input("Enter the updated last name: ")
            index = 0
            for i in Student:
                if i["Last_Name"] == Last_name:
                    Student[index]["Last_Name"] = up_lname
                    index+=1
                else:
                    index+=1


        elif A == 3:
            Class = input("Enter the class you want it to get updated: ")
            up_class = input("Enter the updated class: ")
            index = 0
            for i in Student:
                if i["Class"] == Class:
                    Student[index]["Class"] = up_class
                    index+=1
                else:
                    index+=1


        elif A == 4:
            Section = input("Enter the section you want it to get updated: ")
            up_section = input("Enter the updated section: ")
            index = 0
            for i in Student:
                if i["Section"] == Section:
                    Student[index]["Section"] = up_section
                    index+=1
                else:
                    index+=1

        elif A==5:
            break


def show_student():
    SNo = int(input("Enter serial no: "))
    for i in Student:
        if i["SNo"] == SNo:
            print("S.No: " + str(i["SNo"]))
            print("Name: " + i["Name"] + " " +i["Last_name"])
            print("Class: " + i["Class"])
            print("Section: " + i["Section"])

x = True
while x == True:
    ch1 = int(input("Enter choice: \n 1. Add new record of student \n 2. Update the record \n 3. Display the record \n 4. Exit \n"))
    if ch1 == 1:
        add_student()
    elif ch1 == 2:
        update_student()
    elif ch1 == 3:
        show_student()
    elif ch1 == 4:
        break