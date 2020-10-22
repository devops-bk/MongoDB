import pymongo

# CONNECT TO DATABASE
connection = pymongo.MongoClient("localhost", 27017)

# CREATE DATABASE
db = connection['my_database']
print("Database connected")


# function to add data into mongo db
def add():
    try:
        cust_Id = input('Enter Customer id : ')
        cust_Name = input('Enter Name : ')
        cust_dob = input('Enter date of birth : ')
        cust_address = input('Enter address: ')
        cust_phno = input('Enter Phone Number: ')
        cust_Country = input('Enter Country : ')

        db.Customers.insert_one(
            {
                "id": cust_Id,
                "name": cust_Name,
                "dob": cust_dob,
                "address": cust_address,
                "phno": cust_phno,
                "country": cust_Country
            })
        print("Inserted data successfully\n")

    except (Exception, e):
        print(str(e))


# function to update record to mongo db
def update():
    try:
        criteria = input('\nEnter id to update\n')
        c_name = input('\nEnter name to update\n')
        c_dob = input('\nEnter age to update\n')
        c_address = input('\nEnter address to update\n')
        c_phno = input('\nEnter Phone Number to update\n')
        c_country = input('\nEnter country to update\n')

        db.Customers.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name": c_name,
                    "dob": c_dob,
                    "address": c_address,
                    "phno": c_phno,
                    "country": c_country
                }
            }
        )
        print("\nRecords updated successfully\n")

    except (Exception, e):
        print(str(e))


# function to read records from mongo db
def read():
    try:
        custCol = db.Customers.find()
        print('\n All data from My_Database \n')
        for cust in custCol:
            print(cust)

    except (Exception, e):
        print(str(e))



# Function to delete record from mongo db
def delete():
    try:
        criteria = input('\nEnter customer id to delete\n')
        db.Customers.delete_many({"id": criteria})
        print('\nDeletion successful\n')
    except (Exception, e):
        print(str(e))

while (1):
    # chossing option to do CRUD operations
    selection = input('\nSelect 1 to Add, 2 to Update, 3 to Read, 4 to Delete, 5 to Exit\n')

    if selection == '1':
        add()
    elif selection == '2':
        update()
    elif selection == '3':
        read()
    elif selection == '4':
        delete()
    else:
        print('\n Good Day !!! \n')
        break

# CLOSE DATABASE
connection.close()