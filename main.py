students = {}

while True:
    print("\n===== ATTENDANCE MANAGER =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        students[name] = "Absent"
        print(name, "added!")

    elif choice == '2':
        name = input("Enter student name: ")
        if name in students:
            students[name] = "Present"
            print("Marked Present!")
        else:
            print("Not found!")

    elif choice == '3':
        for name, status in students.items():
            print(name, "-", status)

    elif choice == '4':
        break