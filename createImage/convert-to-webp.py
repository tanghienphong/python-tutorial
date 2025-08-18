import requests
from PIL import Image
from io import BytesIO
import os

def convert_images_to_webp(image_urls, width, height, output_dir='output_images', quality=80):
    # Tạo thư mục lưu ảnh webp nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    for url in image_urls:
        try:
            # Tải ảnh từ url
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Kiểm tra lỗi HTTP
            # Đọc dữ liệu ảnh vào bộ nhớ và mở bằng PIL
            img = Image.open(BytesIO(response.content)).convert('RGBA')
            # Resize ảnh về kích thước mong muốn
            # Sử dụng LANCZOS cho Pillow >= 10, ANTIALIAS cho bản cũ
            try:
                resample = Image.Resampling.LANCZOS
            except AttributeError:
                resample = Image.ANTIALIAS
            img = img.resize((width, height), resample)
            # Lấy tên file từ url, bỏ phần mở rộng
            filename = os.path.basename(url)
            name, _ = os.path.splitext(filename)
            # Đặt tên file thân thiện SEO: chữ thường, thay khoảng trắng bằng gạch ngang
            seo_name = name.lower().replace(' ', '-')
            # Đường dẫn file webp xuất ra
            output_path = os.path.join(output_dir, f'{seo_name}.webp')
            # Xóa metadata không cần thiết (nếu có)
            if 'exif' in img.info:
                img.info.pop('exif')
            # Lưu ảnh dưới định dạng webp với chất lượng tối ưu cho SEO
            img.save(output_path, format='WEBP', quality=quality, method=6)
            print(f"Saved SEO optimized: {output_path}")
        except Exception as e:
            # In lỗi nếu có vấn đề với url hoặc xử lý ảnh
            print(f"Error processing {url}: {e}")

convert_images_to_webp([
    'https://cdnv2.tgdd.vn/mwg-static/tgdd/Banner/60/19/6019df4064345d149d4ed9d618b39917.png'
], 800, 600)