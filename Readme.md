## Cấu trúc

Đặt các files và folder theo cấu trúc sau:

```
root
    |
    |-- git_diff.sh
    |
    |-- review
        |
        |-- .env
        |-- git_diff.txt
        |-- php_symfony_code_review_checklist.txt
        |-- review.py
```
---
## Hướng dẫn cài đặt Python3 trong Ubutun (WSL)

1. Cài đặt Python3:

```bash
    sudo apt install python3-full
```

2. Install thư viện Pip3:
```bash
	sudo apt install python3-pip
```

3. Vào thư mục review tạo môi trường ảo cho Python3 (chỉ dành cho Ubutun và Debian) với tên **python-virtual-env**:
```bash
	python3 -m venv python-virtual-env
```

4. Kích hoạt môi trường ảo (trong folder review):
```bash
	source python-virtual-env/bin/activate
```

5. Install thư viện openai (trong môi trường ảo):

```bash
    pip install openai==0.28
```

6. Install thư viện dotenv:

```bash
    pip install dotenv
```

7. Thoát môi trường ảo (trong folder review):
```bash
deactivate
```

---
## Giải thích

- **git_diff.sh**: dùng để so sánh nội dung của nhánh hiện tại và 1 nhánh khác (ví dụ: nhánh develop), sau đó xuất ra file git_diff.txt trong folder review.

- **.env**: dùng để khai báo các biến constant

    - **OPENAI_API_KEY**: khai báo key OpenAI

    - **GIT_DIFF_FILE**: tên file chứa nội dung git diff

    - **PHP_SYMFONY_CODE_REVIEW_CHECKLIST**: tên file chứa nội dung review checklist.

- **git_diff.txt**: là kết quả sau khi chạy git_diff.sh, chứa nội dung so sánh khác nhau giữa 2 nhánh.

- **php_symfony_code_review_checklist.txt**: chứa nội dung review checklist

- **review.py**: file thực thi review code và trả kết quả ra file review_feedback.md
---
## Cách sử dụng:

### 1. Tạo file git_diff.txt

 1. Vào thư mục **root** chạy lệnh: **`git fetch`**.

 2. Vào file **git_diff.sh** điều chỉnh thông số sau:

    - `BRANCH_SOURCE="feature/base_front_web_branch_2"`: khai báo lại nhánh cần so sánh.

    - `BRANCH_TARGET=$(git rev-parse --abbrev-ref HEAD)`: mặc định đang lấy nhánh hiện tại trong folder. Nếu muốn chọn nhánh khác, thì khai báo tại đây.

3. Vào Terminal chạy lệnh sau để tạo file gif_diff.txt trong folder review.

```bash
    sh gif_diff.sh
```

### 2. Review code
1. Kiểm tra và thêm OpenAI key vào file .env
2. Vào thư mục review, chạy lệnh để review code:
```bash
	python3 review.py
```

### 3. Kết quả
> [!note]
> (python-virtual-env) phongth@LT096:~/diskunion/review$ python review.py
> ⏳ Start time: 2025-08-11 11:24:04
> 🔍 Loading... Please wait while the AI reviews your code...
> 
> ✅ Done! Output saved to: review_feedback.md
> 🕒 End time: 2025-08-11 11:24:14
> ⏱️ Duration: 10.45 seconds
> 📊 Token usage: 4760 total (Prompt: 4331, Completion: 429)

---

## Issuses:

### package openAi chưa tương thích version:
1. **Hiện tượng:**
> [!note]
> ⏳ Start time: 2025-08-11 10:43:58
> 🔍 Loading... Please wait while the AI reviews your code...
> Traceback (most recent call last):
>   File "/home/phongth/diskunion/review/review.py", line 56, in <module>
>     response = openai.ChatCompletion.create(
>                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/lib/python3/dist-packages/openai/lib/_old_api.py", line 39, in __call__
>     raise APIRemovedInV1(symbol=self._symbol)
> openai.lib._old_api.APIRemovedInV1:
> 
> You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.
> 
> You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface.
> 
> Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
> 
> A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

2. **Lý do:**
> [!note]
> Lỗi **"externally-managed-environment"** là một tính năng an toàn trong các phiên bản Python và các bản phân phối Linux mới, đặc biệt là Ubuntu và Debian. Nó ngăn bạn dùng `pip` để thay đổi hệ thống Python của cả máy, điều này có thể gây ra xung đột và làm hỏng các công cụ của hệ thống phụ thuộc vào một phiên bản gói cụ thể.
> 
> Lý do là trình quản lý gói của hệ thống (`apt`) chịu trách nhiệm quản lý các thư viện Python cần thiết cho hệ điều hành hoạt động. Khi bạn dùng `pip` để cài đặt các gói một cách toàn cục, nó có thể ghi đè hoặc can thiệp vào các gói do hệ thống quản lý, dẫn đến sự thiếu ổn định. Lỗi này là một lời cảnh báo để ngăn điều đó xảy ra.


3. **Cách khắc phục**:
> [!note]
> Giải pháp được đề xuất là dùng **môi trường ảo (virtual environment)**. Môi trường ảo tạo ra một không gian biệt lập cho dự án Python của bạn, cho phép bạn cài đặt các gói bằng `pip` mà không ảnh hưởng đến toàn bộ hệ thống Python.


