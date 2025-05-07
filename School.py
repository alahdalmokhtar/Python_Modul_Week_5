class School:
    students = []
    teachers ={}
    def __init__(self , name , foundation_year ):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}
#add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.


    def add_new_student(self, student_name, student_class):
        self.students.append({'name': student_name, 'class': student_class})
        print(f"Added student: {student_name}, Class: {student_class}")

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        print(f"Added teacher: {teacher_name}, Branch: {branch}")

    def view_student_list(self):
        if not self.students:
            print("No students enrolled.")
        else:
            print("Student List:")
            for student in self.students:
                print(f"- {student['name']} (Class: {student['class']})")

    def view_teacher_list(self):
        if not self.teachers:
            print("No teachers employed.")
        else:
            print("Teacher List:")
            for name, branch in self.teachers.items():
                print(f"- {name} (Branch: {branch})")

    
school = School("ABC High School", 1990)
school.add_new_student("John Doe", "10th Grade")
school.add_new_student("Jane Smith", "11th Grade")
school.add_new_teacher("Mr. Brown", "Mathematics")
school.add_new_teacher("Ms. Green", "Science")

school.view_student_list()
school.view_teacher_list()