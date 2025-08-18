from PIL import Image, ImageDraw, ImageFont
import os

def create_images_from_text(
    background_path,
    text_list,
    output_dir='output_images',
    font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    font_size=40
):
    os.makedirs(output_dir, exist_ok=True)
    for text in text_list:
        img = Image.open(background_path).convert('RGBA')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        text1 = text + "\n trong chuỗi hàm PHP"
        bbox = draw.multiline_textbbox((0, 0), text1, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        img_width, img_height = img.size
        x = (img_width - text_width) // 2
        y = (img_height - text_height) // 2
        line_spacing = int(font_size * 0.8)
        draw.multiline_text((x, y), text1, font=font, fill=(255, 255, 255, 255), align="center", spacing=line_spacing)
        text2 = text.replace("function ", "function-").replace("()", "-").replace(" ", "-").replace("_", "-")
        if text2.endswith("-"):
            text2 = text2[:-1]
        output_path = os.path.join(output_dir, f'{text2}.png')
        img.save(output_path)
    print("Đã tạo xong ảnh!")

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