
import os


class University:
    def __init__(self, university_name, university_discipline):
        self.university_name = university_name
        self.university_discipline = university_discipline

    def display_info(self):
        return f"University Name: {self.university_name}, Discipline: {self.university_discipline}"


class Courses(University):
    def __init__(self, course_code, course_name, university_name, university_discipline):
        University.__init__(self, university_name, university_discipline)
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, {super().display_info()}"


class Campus(University):
    def __init__(self, district_name, university_name, university_discipline):
        University.__init__(self, university_name, university_discipline)
        self.district_name = district_name

    def display_info(self):
        return f"District: {self.district_name}, {super().display_info()}"


class Student(Campus, Courses):
    def __init__(self, name, age, cgpa, district_name, course_code, course_name, university_name, university_discipline):
        Campus.__init__(self, district_name, university_name, university_discipline)
        Courses.__init__(self, course_code, course_name, university_name, university_discipline)
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        campus_info = super(Campus, self).display_info()
        courses_info = super(Courses, self).display_info()
        return f"Student Information : Name: {self.name}, Age: {self.age}, CGPA: {self.cgpa},{courses_info}, {campus_info} "


class Faculty(Campus, Courses):
    def __init__(self, faculty_name, qualification, pec, district_name, course_code, course_name, university_name, university_discipline):
        Campus.__init__(self, district_name, university_name, university_discipline)
        Courses.__init__(self, course_code, course_name, university_name, university_discipline)
        self.faculty_name = faculty_name
        self.qualification = qualification
        self.pec = pec

    def display_info(self):
        campus_info = super(Campus, self).display_info()
        courses_info = super(Courses, self).display_info()
        return f"Faculty Information : Faculty Name: {self.faculty_name}, Highest Qualification: {self.qualification}, PEC: {self.pec}, {courses_info}, {campus_info}"


class UniversitySystem:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_member_info(self, member):
        with open(self.file_name, 'a') as file:
            file.write(member.display_info() + '\n')

    def view_member_info(self):
        with open(self.file_name, 'r') as file:
            return file.read()

    def delete_member_info(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            return "File deleted successfully."
        else:
            return "File not found."

# Example usage:


university_system = UniversitySystem("Member1_Member2.txt")

# Creating instances of different classes
university = University("NUST", "ME")
campus = Campus("Rawalpindi", "NUST", "ME")
courses = Courses("CS101", "Object Oriented Programming", "NUST", "ME")
student = Student("Shahroz", 20, 3.1, "Rawalpindi", "CS101", "Object Oriented Programming", "NUST", "ME")
faculty = Faculty("Kamran", "Maters", True, "Rawalpindi", "CS101", "Object Oriented Programming", "NUST", "ME")

# Adding information to the text file
university_system.add_member_info(university)
university_system.add_member_info(campus)
university_system.add_member_info(courses)
university_system.add_member_info(student)
university_system.add_member_info(faculty)

# Viewing information from the text file
print("Information in the text file:")
print(university_system.view_member_info())

# Deleting the text file
print(university_system.delete_member_info())
