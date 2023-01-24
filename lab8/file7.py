faculty_list = []

def add_faculty():
    name = input("Enter name: ")
    department = input("Enter department: ")
    subject = input("Enter subject: ")
    faculty_list.append({"name": name, "department": department, "subject": subject})
    print("Faculty added successfully!")

def delete_faculty():
    name = input("Enter name of the faculty to be deleted: ")
    for i, faculty in enumerate(faculty_list):
        if faculty["name"] == name:
            del faculty_list[i]
            print("Faculty deleted successfully!")
            return
    print("Faculty not found.")

def update_faculty():
    name = input("Enter name of the faculty to be updated: ")
    for i, faculty in enumerate(faculty_list):
        if faculty["name"] == name:
            department = input("Enter new department: ")
            subject = input("Enter new subject: ")
            faculty_list[i] = {"name": name, "department": department, "subject": subject}
            print("Faculty updated successfully!")
            return
    print("Faculty not found.")

def display_faculty():
    name = input("Enter name of the faculty to be displayed (leave blank to display all): ")
    if name == "":
        for faculty in faculty_list:
            print(faculty)
    else:
        for faculty in faculty_list:
            if faculty["name"] == name:
                print(faculty)
                return
        print("Faculty not found.")

while True:
    print("1. Add Faculty")
    print("2. Delete Faculty")
    print("3. Update Faculty")
    print("4. Display Faculty")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_faculty()
    elif choice == "2":
        delete_faculty()
    elif choice == "3":
        update_faculty()
    elif choice == "4":
        display_faculty()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
