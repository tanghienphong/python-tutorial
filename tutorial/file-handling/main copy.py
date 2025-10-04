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
			'student_id': self.student_id,
			'name': self.name,
			'age': self.age,
			'gpa': self.gpa
		}

class StudentManager:
	def __init__(self, file_name):
		self.file_name = file_name
		self.students = []
		self.load_students()

	def load_students(self):
		try:
			with open(self.file_name, 'r', encoding='utf-8') as f:
				data = json.load(f)
				self.students = [Student(**stu) for stu in data]
		except (FileNotFoundError, json.JSONDecodeError):
			self.students = []

	def save_students(self):
		with open(self.file_name, 'w', encoding='utf-8') as f:
			json.dump([stu.to_dict() for stu in self.students], f, ensure_ascii=False, indent=4)

	def add_student(self, student):
		if self.find_student(student.student_id):
			print("Student ID already exists!")
			return False
		self.students.append(student)
		self.save_students()
		print("Student added successfully.")
		return True

	def find_student(self, student_id):
		for stu in self.students:
			if stu.student_id == student_id:
				return stu
		return None

	def delete_student(self, student_id):
		stu = self.find_student(student_id)
		if stu:
			self.students.remove(stu)
			self.save_students()
			print("Student deleted successfully.")
			return True
		print("Student not found!")
		return False

	def display_all_students(self):
		if not self.students:
			print("No students found.")
		else:
			for stu in self.students:
				print(stu)

def main():
	manager = StudentManager('students.json')
	while True:
		print("\n===== Student Management System =====")
		print("1. Add new student")
		print("2. View all students")
		print("3. Find student by ID")
		print("4. Delete student by ID")
		print("5. Exit")
		choice = input("Enter your choice (1-5): ")

		if choice == '1':
			student_id = input("Enter student ID: ")
			name = input("Enter name: ")
			try:
				age = int(input("Enter age: "))
				gpa = float(input("Enter GPA: "))
			except ValueError:
				print("Invalid age or GPA!")
				continue
			student = Student(student_id, name, age, gpa)
			manager.add_student(student)
		elif choice == '2':
			manager.display_all_students()
		elif choice == '3':
			student_id = input("Enter student ID to search: ")
			stu = manager.find_student(student_id)
			if stu:
				print(stu)
			else:
				print("Student not found!")
		elif choice == '4':
			student_id = input("Enter student ID to delete: ")
			manager.delete_student(student_id)
		elif choice == '5':
			print("Exiting...")
			break
		else:
			print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
	main()
