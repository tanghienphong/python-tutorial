import json
class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, GPA: {self.gpa}"
    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "gpa": self.gpa
        }
        
class StudentManager:
    def __init__(self, file_name):  
        self.file_name = file_name
        self.students = []
        
    def load_students(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                # for item in data:
                #     student = Student(**item)
                #     self.students.append(student)
                self.students = [Student(**item) for item in data]
        except Exception as e:
            print(f"Lỗi loading students: {e}")
            
    def save_students(self):
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                # json.dump([student.to_dict() for student in self.students], file)
                json.dump([student.to_dict() for student in self.students], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi saving students: {e}")

    def add_student(self, student):
        try:
            self.students.append(student)
            self.save_students()
        except Exception as e:
            print(f"Lỗi adding student: {e}")
            
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def delete_student(self, student_id):
        try:
            student = self.find_student(student_id)
            if student:
                self.students.remove(student)
                self.save_students()
        except Exception as e:
            print(f"Lỗi deleting student: {e}")
            
    def display_all_students(self):
        if not self.students:
            print("Không tìm thấy sinh viên.")
            return
        for student in self.students:
            print(student)
            
def main():
    students = StudentManager('students.json')
    students.load_students()
    students.display_all_students()

    print("========Hệ Thống Quản Lý Sinh Viên========")
    print("1. Thêm sinh viên mới")
    print("2. Xem danh sách sinh viên")
    print("3. Tìm kiếm sinh viên theo ID")
    print("4. Xoá sinh viên theo ID")
    print("5. Thoát")
    choice = input("Chọn chức năng: ")

    if choice == "1":
        student_id = input("Nhập ID sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        gpa = float(input("Nhập GPA sinh viên: "))
        student = Student(student_id, name, age, gpa)
        students.add_student(student)
    elif choice == "2":
        students.display_all_students()
    elif choice == "3":
        student_id = input("Nhập ID sinh viên cần tìm: ")
        student = students.find_student(student_id)
        if student:
            print("Thông tin sinh viên:")
            print(student)
        else:
            print("Không tìm thấy sinh viên.")
    elif choice == "4":
        student_id = input("Nhập ID sinh viên cần xoá: ")
        students.delete_student(student_id)
    elif choice == "5":
        print("Thoát chương trình.")
        return
    else:
        print("Lựa chọn không hợp lệ.")

main()