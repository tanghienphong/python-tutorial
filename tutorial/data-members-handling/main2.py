# Xây dựng một pipeline xử lý danh sách sinh viên theo phong cách functional, không dùng vòng lặp for, không thay đổi trạng thái (no mutation), và không dùng class.
# students = [
#     {'name': 'An', 'score': 8.5, 'major': 'CS'},
#     {'name': 'Binh', 'score': 6.0, 'major': 'Math'},
#     {'name': 'Chi', 'score': 9.0, 'major': 'CS'},
#     {'name': 'Dung', 'score': 5.5, 'major': 'Physics'},
#     {'name': 'Hoa', 'score': 7.5, 'major': 'Math'},
# ]

# Yêu Cầu
# - Lọc ra các sinh viên ngành "CS" có điểm >= 8.0.
# - Chuyển đổi danh sách thành dạng: ["An (8.5)", "Chi (9.0)"].
# - Sắp xếp theo điểm giảm dần.
# - Tính trung bình điểm của các sinh viên đã lọc.
# - Không dùng vòng lặp, chỉ dùng map, filter, reduce, sorted, lambda.
# from functools import reduce
from functools import reduce

students = [
    {'name': 'An', 'score': 8.5, 'major': 'CS'},
    {'name': 'Binh', 'score': 6.0, 'major': 'Math'},
    {'name': 'Chi', 'score': 9.0, 'major': 'CS'},
    {'name': 'Dung', 'score': 5.5, 'major': 'Physics'},
    {'name': 'Hoa', 'score': 7.5, 'major': 'Math'},
]

# Lọc ra sinh viên ngành CS và có điểm >= 8.0
def filter_cs_students(students):
    return list(filter(lambda student: student['major'] == 'CS' and student['score'] >= 8.0, students))

# Chuyển đổi danh sách thành dạng: ["An (8.5)", "Chi (9.0)"].
def format_students(students):
    return list(map(lambda student: f"{student['name']} ({student['score']})", students))

# Sắp xếp theo điểm giảm dần.
def sort_students(students):
    return sorted(students, key=lambda student: student['score'], reverse=True)

# Tính trung bình điểm của các sinh viên đã lọc.

def sum_scores(students):
    return reduce(lambda total, student: total + student['score'], students, 0)

def average_score(students):
    if not students:
        return 0
    return sum_scores(students) / len(students)

def main():
    filtered_students = filter_cs_students(students)
    formatted_students = format_students(filtered_students)
    sorted_students = sort_students(filtered_students)
    avg_score = average_score(filtered_students)

    print("Danh sách sinh viên ngành CS có điểm >= 8.0:")
    print(formatted_students)
    print("Danh sách sinh viên sau khi sắp xếp:")
    print(sorted_students)
    print("Điểm trung bình:", avg_score)

if __name__ == "__main__":
    main()