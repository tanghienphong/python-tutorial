from PIL import Image, ImageDraw, ImageFont
import os

# Đường dẫn tới file ảnh nền
background_path = 'background-series-php.png'

# Danh sách ký tự cần in lên ảnh
text_list = ['A', 'B', 'C', 'D', 'E']

# Thư mục lưu ảnh kết quả
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Font chữ (có thể thay đổi đường dẫn tới font phù hợp)
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font_size = 80

for text in text_list:
    # Mở ảnh nền
    img = Image.open(background_path).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Tạo font
    font = ImageFont.truetype(font_path, font_size)

    # Tính toán vị trí để căn giữa chữ
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    img_width, img_height = img.size
    x = (img_width - text_width) // 2
    y = (img_height - text_height) // 2

    # Vẽ chữ lên ảnh
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    # Lưu ảnh mới
    output_path = os.path.join(output_dir, f'{text}.png')
    img.save(output_path)

print("Đã tạo xong ảnh!")