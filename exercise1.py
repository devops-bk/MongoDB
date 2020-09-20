Student = [{'name' : 'Bhavya', 'Mobile No.' : '9548763254', 'City' : 'Indore', 'State' : 'M.P', 'Country' : 'India'},
{'name' : 'Shalu', 'Mobile No.' : '9752143254', 'City' : 'Udaipur', 'State' : 'Rajasthan', 'Country' : 'India'},
{'name' : 'Pranshu', 'Mobile No.' : '8654793554', 'City' : 'Indore', 'State' : 'M.P', 'Country' : 'India'},
{'name' : 'Abhishek', 'Mobile No.' : '6547985423', 'City' : 'Indore', 'State' : 'M.P', 'Country' : 'India'},
{'name' : 'Aishwary', 'Mobile No.' : '7589645863', 'City' : 'Banglore', 'State' : 'Karnataka', 'Country' : 'India'},
{'name' : 'Minul', 'Mobile No.' : '6589742368', 'City' : 'Khandwa', 'State' : 'M.P', 'Country' : 'India'},
{'name' : 'Palak', 'Mobile No.' : '8756943658', 'City' : 'Hyderabad', 'State' : 'Telangana', 'Country' : 'India'},
{'name' : 'Bhavin', 'Mobile No.' : '9998754863', 'City' : 'Indore', 'State' : 'M.P', 'Country' : 'India'},
{'name' : 'Saumya', 'Mobile No.' : '8958769543', 'City' : 'Indore', 'State' : 'M.P', 'Country' : 'India'},
{'name' : 'Arpita', 'Mobile No.' : '8547621698', 'City' : 'Gurgaon', 'State' : 'Haryana', 'Country' : 'India'}]


name = input("Enter Name : ")

for i in Student:
    if i['name'] == name:
        print(i['name'] +"'s" +' ' +'mobile number is ' +i['Mobile No.'] + '.')
