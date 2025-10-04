# Xây dựng một hệ thống để xử lý các đơn hàng lớn được đọc từ một file, tính toán và báo cáo tổng doanh thu, tổng số lượng bán hàng theo từng sản phẩm

# "order_id", "product_name", "quantity", "price_per_unit"
# "A101", "Laptop", "2", "1200"
# "A102", "Mouse", "10", "25.50"
# "A103", "Keyboard", "5", "75"
# "A104", "Monitor", "3", "300"
# "A105", "Mouse", "8", "25.50"
# "A106", "Laptop", "1", "1200"
# "A107", "Keyboard", "2", "75"

# -Order(order_id, product_name, quantity, price_per_unit)
# - Viết Generator để đọc tệp tin
# Tạo một hàm generator độc lập có tên read_orders_from_file(file_path).
# Hàm này sẽ nhận đường dẫn của tệp tin chứa dữ liệu đơn hàng.
# Với mỗi dòng dữ liệu, tạo một đối tượng Order và yield đối tượng đó.
# -Tạo một decorator có tên order_report_generator.
# Decorator này sẽ nhận một hàm, mà hàm này sẽ trả về một generator chứa các đối tượng Order.
# Chức năng của decorator là:
# In ra tiêu đề báo cáo, ví dụ: "--- Báo cáo doanh số ---".
# Gọi hàm gốc để nhận về đối tượng generator.
# Lặp qua generator đó để tính tổng số lượng sản phẩm bán ra và tổng doanh thu.
# In ra các thông tin báo cáo 
# Ví dụ: "Thống kê số lượng theo sản phẩm"
#            Laptop : 2
# 		   Mouse: 10
# 	    Tổng doanh thu : 90000
# In ra một dòng kết thúc: "--- Kết thúc báo cáo ---".
import csv

class Order:
    def __init__(self, order_id, product_name, quantity, price_per_unit):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

def read_orders_from_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua tiêu đề
        # lặp từng dòng
        for row in reader:
            order_id, product_name, quantity, price_per_unit = row
            yield Order(order_id, product_name, int(quantity), float(price_per_unit))
            

def order_report_generator(func):
    def wrapper(*args, **kwargs):
        print("--- Báo cáo doanh số ---")
        orders = func(*args, **kwargs)
        product_stats = {}
        total_revenue = 0
        for order in orders:
            product_stats[order.product_name] = product_stats.get(order.product_name, 0) + order.quantity
            total_revenue += order.quantity * order.price_per_unit
        print("Thống kê số lượng theo sản phẩm:")
        for product, qty in product_stats.items():
            print(f"  {product}: {qty}")
        print(f"Tổng doanh thu: {total_revenue:,.2f}")
        print("--- Kết thúc báo cáo ---")
    return wrapper


@order_report_generator
def get_orders(file_path):
    return read_orders_from_file(file_path)

if __name__ == "__main__":
    file_path = "tutorial/decorator/order.csv"
    get_orders(file_path)