import pandas as pd
import sys

class Extractor:
    def __init__(self, file_name):
        self.file_name = file_name 
        
    def get_data(self):

        # check file exists
        try:
            self.df = pd.read_csv(self.file_name)
            return self.df
        except FileNotFoundError:
            print(f"File {self.file_name} not found")
            # Terminal process
            sys.exit(1)   
            

class Transformer:
    def __init__(self, df):
        self.df = df
        
    # Tổng giá trị giao dịch
    def get_total_transaction_value(self):
        self.df['amount'] = self.df['quantity'] * self.df['unitPrice']
        return self.df
    
    # Chuẩn hóa tên khách hàng (viết hoa chữ cái đầu)
    def customize_name(self):
        self.df['customerName'] = self.df['customerName'].str.title()
        return self.df
    
    # Tính tổng doanh thu theo từng ngày
    def get_total_amount_everyday(self):
        self.df.groupby('transactionDate')['amount'].sum()
        return self.df[['transactionDate', 'amount']]

    # Tính tổng doanh thu theo từng danh mục sản phẩm (category)
    def get_total_amount_by_category(self):
        self.df.groupby('category')['amount'].sum()
        return self.df[['category', 'amount']]

    # Tìm top 3 khách hàng có tổng chi tiêu cao nhất.
    def get_top_3_customers(self):
        self.df.groupby('customerName')['amount'].sum().nlargest(3)
        return self.df[['customerName', 'amount']]

class Loader:
    def __init__(self, df):
        self.df = df

    # Ghi báo cáo doanh thu theo ngày ra file daily_revenue.csv
    def load_to_csv(self, filename):
        self.df.to_csv(filename, index=False)
        print(f"Data đã được export thành công ra file {filename}!")


file_name = 'transactions.csv'
# Tạo đối tượng Extractor
extractor = Extractor(file_name)
df = extractor.get_data()

print(df)

# Tạo đối tượng Transformer
transformer = Transformer(df)
df = transformer.get_total_transaction_value()
df = transformer.customize_name()

# Tạo đối tượng Transformer
transformer = Transformer(df)
dfTotal = transformer.get_total_amount_everyday()
dfCategory = transformer.get_total_amount_by_category()
dfTopCustomers = transformer.get_top_3_customers()


# Tạo đối tượng Loader

# Ghi báo cáo doanh thu theo ngày
loader = Loader(dfTotal)
loader.load_to_csv('daily_revenue.csv')

# Ghi báo cáo doanh thu theo danh mục
loader = Loader(dfCategory)
loader.load_to_csv('category_revenue.csv')

# Ghi danh sách top 3 khách hàng
loader = Loader(dfTopCustomers)
loader.load_to_csv('top_customers.csv')

