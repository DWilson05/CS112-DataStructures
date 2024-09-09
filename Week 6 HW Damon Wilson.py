student_list = []   # list to store linked lists


class Node:
    def __init__(self, pname, cname):  # add two pieces of data prof and course names
        self.pname = pname
        self.cname = cname
        self.ref = None


class RegistrarProgram:
    # ---------------Create an empty linked list -------------

    def __init__(self, stuname):   # store data about the student name
        self.student_name = stuname
        self.start_node = None

    # --------------- View and print out course  ----------------------

    def view_registration(self):
        if self.start_node is None:
            print(" This student has not enrolled for any classes\n")
            return
        else:
            n = self.start_node
            while n is not None:
                print(f""" Class Name: {n.cname}
 Professor: {n.pname}
""")
                n = n.ref

        #  ------------- Insert at start  ----------------------

    def insert_course(self, pname, cname):
        new_node = Node(pname, cname)
        new_node.ref = self.start_node
        self.start_node = new_node

        #  ------------- Search for a course  ------------

    def search_course(self, courseName):
        if self.start_node is None:
            print(" This student has not enrolled for any classes")
            return
        n = self.start_node
        while n is not None:
            if n.cname == courseName:
                return True
            n = n.ref
        print(f" This student was not enrolled in {courseName}")
        return False

        #  ------------- delete the course  ------------

    def delete_course(self, courseName):
        if self.start_node is None:
            print(" This student has not enrolled for any classes")
            return
        if self.start_node.cname == courseName:   # if it is the correct course
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:   # until last node
            if n.ref.cname == courseName:
                break
            n = n.ref
        if n.ref is None:
            print("Course was not found")
        else:
            n.ref = n.ref.ref


# ----------------------- Search if student is present in list -----------------------------

def search_student(student_name):   # search for the student in the list and in the linked list
    if len(student_list) == 0:  # if the list is empty
        print("There are no students in the system yet")
    for name in student_list:   # for each student
        if name.student_name == student_name:   # if the name matches
            return True
    print(f" The student {student_name} was not found")
    return False


# ----------------------- add the course to student -----------------------------

def add_course(student_name):    # add the course to the specific student in the list
    if search_student(student_name):    # if the student is in the list return true
        for name in student_list:       # for every student in the list
            if name.student_name == student_name:   # if it is the correct student
                course = input(" Enter the name of the course: ")
                professor = input(" Enter the name of the professor: ")
                name.insert_course(professor, course)   # the student gets a course and professor added
                print(f"\nExiting registration for {student_name}")


# ----------------------- MAIN -----------------------------

choice = 0
while choice != 6:
    print("""
------------------------------------
   ~~ Course Registration 2024 ~~
------------------------------------

1 = Add new student
2 = Register for courses
3 = Withdraw from a course
4 = View a student registration
5 = View All
6 = Exit""")
    choice = int(input("\n Enter Choice: "))
    if choice == 1:
        newStudent = input("\n Enter Student's Name: ")
        new_student = RegistrarProgram(newStudent)
        student_list.append(new_student)    # add new student to list
        print("", newStudent, " has been added")
    elif choice == 2:
        student = input("\n Enter the name of the student to register: ")
        add_course(student)
    elif choice == 3:
        student = input("\n Enter the name of the student to withdraw: ")
        if search_student(student):   # if student is in the system
            course = input(" Enter the name of the course: ")
            for eachStudent in student_list:   # checks every student
                if eachStudent.student_name == student:   # if the names match
                    if eachStudent.search_course(course):   # if the student has the course
                        eachStudent.delete_course(course)   # the course is removed
                        print(f" {course} was removed from registration")
    elif choice == 4:
        student = input("\n Enter the name of the student to view: ")
        if search_student(student):   # if student is in the system
            for eachStudent in student_list:   # checks every student
                if eachStudent.student_name == student:  # if the names match
                    print(f"""\n------------------------------------   
 Student: {eachStudent.student_name}\n""")  # The name of the student will only print once
                    eachStudent.view_registration()   # print courses
                    print("------------------------------------")  # formatting
    elif choice == 5:
        for student in student_list:  # For every student now in the list
            print(f"""\n------------------------------------   
 Student: {student.student_name}\n""")    # The name of the student will only print once
            student.view_registration()   # in view registration it will print the cname and pname of every course
            print("------------------------------------")  # formatting

print("""
------------------------------------
~~ Closing the Registrar Program ~~
------------------------------------""")
