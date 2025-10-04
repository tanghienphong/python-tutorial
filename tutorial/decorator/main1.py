# Tạo một decorator có tên permission để kiểm tra xem một người dùng có quyền cần thiết để chạy một hàm hay không

# yêu cầu: 
# -xây dựng class User (username, role)
# -permission nhận một tham số là chuỗi required_role ('admin', 'editor')
# -Hàm wrapper sẽ kiểm tra xem user có role có khớp với required_role hay không.
# Nếu quyền hợp lệ, thực thi hàm gốc và trả về kết quả.
# Nếu quyền không hợp lệ, in ra một thông báo lỗi (ví dụ: "Lỗi: Bạn không có quyền truy cập.") và không thực thi hàm gốc.
# -Áp dụng decorator requires_permission cho hai hàm: delete (chỉ dành cho 'admin') và edit(dành cho 'admin' và 'editor')

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Decorator kiểm tra quyền, cho phép truyền 1 role hoặc list role
def permission(required_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            # Hỗ trợ truyền 1 role hoặc list role
            if isinstance(required_roles, (list, tuple)):
                allowed = user.role in required_roles
            else:
                allowed = user.role == required_roles
            if allowed:
                return func(user, *args, **kwargs)
            else:
                print("Lỗi: Bạn không có quyền truy cập.")
        return wrapper
    return decorator

# Hàm delete chỉ cho admin
@permission('admin')
def delete(user):
    print(f"{user.username} đã xóa dữ liệu!")

# Hàm edit cho admin và editor
@permission(['admin', 'editor'])
def edit(user):
    print(f"{user.username} đã chỉnh sửa dữ liệu!")

# Ví dụ sử dụng
if __name__ == "__main__":
    u1 = User("Nguyễn Văn A", "admin")
    u2 = User("Nguyễn Văn B", "editor")
    u3 = User("Nguyễn Văn C", "viewer")
    delete(u1)   # hợp lệ
    delete(u2)   # không hợp lệ
    edit(u1)     # hợp lệ
    edit(u2)     # hợp lệ
    edit(u3)     # không hợp lệ
