from PIL import Image, ImageDraw, ImageFont
import os

def create_images_from_text(
    background_path,
    text_list,
    output_dir='output_images',
    font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    font_size=40
):
    # Tạo thư mục lưu ảnh nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    for text in text_list:
        # Mở ảnh nền và chuyển sang RGBA
        img = Image.open(background_path).convert('RGBA')
        draw = ImageDraw.Draw(img)
        # Tạo font chữ
        font = ImageFont.truetype(font_path, font_size)
        # Chuẩn bị nội dung text, thêm dòng mô tả
        text1 = text + "\n trong chuỗi hàm PHP"
        # Tính toán kích thước text để căn giữa
        bbox = draw.multiline_textbbox((0, 0), text1, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        img_width, img_height = img.size
        x = (img_width - text_width) // 2
        y = (img_height - text_height) // 2
        # Vẽ text lên ảnh với khoảng cách dòng
        line_spacing = int(font_size * 0.8)
        draw.multiline_text((x, y), text1, font=font, fill=(255, 255, 255, 255), align="center", spacing=line_spacing)
        # Tạo tên file thân thiện SEO: chữ thường, thay khoảng trắng bằng gạch ngang
        seo_name = text.replace("function ", "function-").replace("()", "-").replace(" ", "-").replace("_", "-").lower()
        if seo_name.endswith("-"):
            seo_name = seo_name[:-1]
        # Đường dẫn file PNG xuất ra
        output_path = os.path.join(output_dir, f'{seo_name}.png')
        # Xóa metadata không cần thiết (nếu có)
        if 'exif' in img.info:
            img.info.pop('exif')
        # Lưu ảnh dưới dạng PNG, tối ưu nén
        img.save(output_path, format='PNG', optimize=True)
    print("Đã tạo xong ảnh PNG tối ưu SEO!")

def create_images_webp_from_text(
    background_path,
    text_list,
    output_dir='output_images',
    font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    font_size=40,
    quality=80
):
    # Tạo thư mục lưu ảnh nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    for text in text_list:
        # Mở ảnh nền và chuyển sang RGBA
        img = Image.open(background_path).convert('RGBA')
        draw = ImageDraw.Draw(img)
        # Tạo font chữ
        font = ImageFont.truetype(font_path, font_size)
        # Chuẩn bị nội dung text, thêm dòng mô tả
        text1 = text + "\n trong chuỗi hàm PHP"
        # Tính toán kích thước text để căn giữa
        bbox = draw.multiline_textbbox((0, 0), text1, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        img_width, img_height = img.size
        x = (img_width - text_width) // 2
        y = (img_height - text_height) // 2
        # Vẽ text lên ảnh với khoảng cách dòng
        line_spacing = int(font_size * 0.8)
        draw.multiline_text((x, y), text1, font=font, fill=(255, 255, 255, 255), align="center", spacing=line_spacing)
        # Tạo tên file thân thiện SEO: chữ thường, thay khoảng trắng bằng gạch ngang
        seo_name = text.replace("function ", "function-").replace("()", "-").replace(" ", "-").replace("_", "-").lower()
        if seo_name.endswith("-"):
            seo_name = seo_name[:-1]
        # Đường dẫn file webp xuất ra
        output_path = os.path.join(output_dir, f'{seo_name}.webp')
        # Xóa metadata không cần thiết (nếu có)
        if 'exif' in img.info:
            img.info.pop('exif')
        # Lưu ảnh dưới dạng webp với chất lượng tối ưu cho SEO
        img.save(output_path, format='WEBP', quality=quality, method=6)
    print("Đã tạo xong ảnh webp tối ưu SEO!")

# Đường dẫn tới file ảnh nền
background_path = 'output_images/background-series-php-watermarked.png'

# Danh sách ký tự cần in lên ảnh
text_list = [
    'function range()',
    'function array()',
    # ...existing code...
    'function unlink()',
]

create_images_from_text(background_path, text_list)

create_images_webp_from_text(background_path, text_list)