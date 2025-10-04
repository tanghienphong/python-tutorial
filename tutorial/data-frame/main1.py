import pandas as pd

class Extractor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)    
        
    def get_data(self):
        return self.df

class Transformer:
    def __init__(self, df):
        self.df = df
        
    # Lấy danh sách Member có mức lương cao hơn ngưỡng (threshold)
    def get_high_salary(self, threshold):
        return self.df[self.df['salary'] >= threshold]

    # Thêm cột Tax và cột Net
    def add_tax_and_net(self):
        self.df['tax'] = self.df['salary'] * 0.1
        self.df['net'] = self.df['salary'] - self.df['tax']
        return self.df
    
class Loader:
    def __init__(self, df):
        self.df = df

    # Xuất dữ liệu ra file Excel
    def load_to_excel(self, filename):
        self.df.to_excel(filename, index=False)
        print(f"Data đã được export thành công ra file {filename}!")
        
file_name = 'data.csv'
# Tạo đối tượng Extractor
extractor = Extractor(file_name)
df = extractor.get_data()

# thêm cột tax
transformer = Transformer(df)

# lấy danh sách salary >= 1000
df2 = transformer.get_high_salary(1000)
# print(df2)

df2 = transformer.add_tax_and_net()
print(df2)

# xuất ra file Excel
loader = Loader(df2)
loader.load_to_excel('data1.xlsx')

# print("=======Thêm Age==========")
# df2['age'] = [25, 45, '']
# print(df2)

# print("=================")
# print(df2.loc[1])
# print("=================")
# print(df2.loc[1, 'name'])
# print("=================")
# print(df2.iloc[1, 1])