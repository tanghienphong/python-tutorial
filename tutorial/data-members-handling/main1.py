# Xử lý dữ liệu nhân viên

# Cho một danh sách các nhân viên, mỗi nhân viên là một dictionary chứa name, role và salary. 
# Thực hiện các tác vụ sau:

# Lọc ra các nhân viên ở vị trí "Developer".
# Tính toán mức lương thưởng cho mỗi nhân viên đủ điều kiện (thưởng 10% nếu lương trên 6000).
# Sắp xếp danh sách nhân viên theo mức lương mới từ cao xuống thấp.

# employees = [
#     {'name': 'Alice', 'role': 'Developer', 'salary': 7000},
#     {'name': 'Bob', 'role': 'Manager', 'salary': 9000},
#     {'name': 'Charlie', 'role': 'Developer', 'salary': 5500},
#     {'name': 'David', 'role': 'Analyst', 'salary': 6500},
#     {'name': 'Eve', 'role': 'Developer', 'salary': 8000}
# ]

# sắp xếp dùng hàm sorted
# new_list = sorted(list, key (function), reverse=True)

employees = [
    {'name': 'Alice', 'role': 'Developer', 'salary': 7000},
    {'name': 'Bob', 'role': 'Manager', 'salary': 9000},
    {'name': 'Charlie', 'role': 'Developer', 'salary': 5500},
    {'name': 'David', 'role': 'Analyst', 'salary': 6500},
    {'name': 'Eve', 'role': 'Developer', 'salary': 8000}
]

# Lọc ra các nhân viên theo vị trí
def filter_employees_by_role(employees, role):
    employees_in_role = list(filter(lambda emp: emp['role'] == role, employees))
    return employees_in_role

#Lọc ra các nhân viên ở vị trí "Developer"
print("=======================================")
print("Nhân viên ở vị trí Developer:")
print(filter_employees_by_role(employees, 'Developer'))

#Tính toán mức lương thưởng cho mỗi nhân viên đủ điều kiện (thưởng 10% nếu lương trên 6000).
## Lọc ra các nhân viên theo lương
def filter_employees_by_salary(employees, salary):
    return list(filter(lambda emp: emp['salary'] >= int(salary), employees))


def apply_bonus(employees):
    """
    Pure function: Trả về danh sách mới với lương đã cộng thưởng 10% nếu lương > 6000.
    Không thay đổi danh sách đầu vào.
    """
    # return list(map(lambda emp: {**emp, 'salary': int(emp['salary'] * 1.1)} if emp['salary'] > 6000 else emp, employees))
    return list(map(lambda emp: {**emp, 'salary': int(emp['salary'] * 1.1)}, employees))

def bonus_for_employees(employees):
    eligible_employees = filter_employees_by_salary(employees, 8000)
    # list(map(lambda emp: emp.update({'salary': int(emp['salary'] * 1.1)}), eligible_employees))
    updated_employees = apply_bonus(eligible_employees)    
    print("===============")
    print(employees)
    print("===============")
    return updated_employees

print("=======================================")
print("Nhân viên đủ điều kiện nhận thưởng:")
print(sorted(bonus_for_employees(employees), key=lambda emp: emp['salary'], reverse=True))
