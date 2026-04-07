print("Attendance Analyzer")

days = int(input("Enter total days: "))
i = 1
present = 0

while i <= days:
    status = int(input("Enter 1 for present, 0 for absent: "))

    if status == 1:
        present = present + 1
    elif status == 0:
        pass
    else:
        print("Invalid entry")

    i = i + 1

percentage = present * 100 / days
print("Attendance %:", percentage)

if percentage >= 75:
    print("Allowed for exam")
else:
    print("Not allowed")

if percentage > 100:
    print("Error in data")
