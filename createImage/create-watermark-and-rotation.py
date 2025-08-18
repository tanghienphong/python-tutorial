from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text, font_path, font_size=12, opacity=20, spacing_x=150, spacing_y=150):
    # Mở ảnh gốc
    base = Image.open(input_image_path).convert('RGBA')
    width, height = base.size

    # Tạo layer watermark trong suốt
    watermark_layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark_layer)
    font = ImageFont.truetype(font_path, font_size)

    # Tạo watermark layer lớn hơn để khi xoay watermark vẫn bắt đầu từ (0,0)
    # Tạo watermark layer lớn hơn hình gốc 1.5 lần
    wm_width = int(width * 1.5)
    wm_height = int(height * 1.5)
    watermark_img = Image.new('RGBA', (wm_width, wm_height), (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark_img)

    # Vẽ watermark lặp lại trên layer watermark lớn
    for y in range(0, wm_height, spacing_y):
        for x in range(0, wm_width, spacing_x):
            watermark_draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

    # Xoay watermark layer 45 độ quanh tâm layer watermark lớn
    center = (wm_width // 2, wm_height // 2)
    rotated = watermark_img.rotate(45, resample=Image.BICUBIC, expand=False, center=center)

    # Crop lại đúng kích thước ảnh gốc từ giữa layer watermark lớn
    left = (wm_width - width) // 2
    top = (wm_height - height) // 2
    rotated_cropped = rotated.crop((left, top, left + width, top + height))

    # Ghép watermark đã crop lên ảnh gốc
    watermarked = Image.alpha_composite(base, rotated_cropped)
    watermarked.save(output_image_path)

# Ví dụ sử dụng
if __name__ == '__main__':
    add_watermark(
        input_image_path='background-series-php.png',
        output_image_path='output_images/background-series-php-watermarked.png',
        watermark_text='Thegioiphp.com',
        font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        spacing_x=200,
        spacing_y=100
    )