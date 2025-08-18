import openai
import os
from dotenv import load_dotenv
load_dotenv()
import time
from datetime import datetime

# ====== Cấu hình API Key ======
openai.api_key = os.getenv("OPENAI_API_KEY")  # Hoặc thay trực tiếp API Key tại đây

# ====== Hàm xử lý diff: giữ lại dòng thêm hoặc context ======
def extract_relevant_diff(diff_text: str) -> str:
    relevant_lines = []
    for line in diff_text.splitlines():
        if line.startswith('+++') or line.startswith('@@'):
            relevant_lines.append(line)
        elif line.startswith('+') and not line.startswith('+++'):
            relevant_lines.append(line)
        # Các dòng - (bị xóa) sẽ bị loại bỏ
    return "\n".join(relevant_lines)

# ====== Đọc file diff và checklist ======
with open(os.getenv("GIT_DIFF_FILE"), "r", encoding="utf-8") as f:
    raw_diff_content = f.read()
    diff_content = extract_relevant_diff(raw_diff_content)

with open(os.getenv("PHP_SYMFONY_CODE_REVIEW_CHECKLIST"), "r", encoding="utf-8") as f:
    checklist = f.read()

# ====== Prompt cho GPT ======
system_prompt = """
You are a senior PHP/Symfony code reviewer.
Review the following Git diff according to the checklist provided.
Only focus on ADDED or MODIFIED lines. Skip deleted ones.
Return the results grouped by file with Markdown format, listing:
- File name
- Issues found (line number if available)
- Suggestions to fix (actionable, concise, no jargon)
"""

user_prompt = f"""
## Checklist:
{checklist}

## Git Diff (Added/Modified only):
{diff_content}
"""

# ====== Ghi log thời gian bắt đầu ======
start_time = time.time()
start_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"⏳ Start time: {start_dt}")
print("🔍 Loading... Please wait while the AI reviews your code...")

# ====== Gọi OpenAI API ======
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.2,
    max_tokens=3000
)

# ====== Nhận kết quả và thông tin token ======
review_output = response["choices"][0]["message"]["content"]
usage = response.get("usage", {})
total_tokens = usage.get("total_tokens", "N/A")
prompt_tokens = usage.get("prompt_tokens", "N/A")
completion_tokens = usage.get("completion_tokens", "N/A")

# ====== Ghi ra file Markdown ======
output_file = "review_feedback.md"
with open(output_file, "w", encoding="utf-8") as md_file:
    md_file.write("# 🔍 AI Code Review Feedback\n\n")
    md_file.write(review_output)

# ====== Thời gian kết thúc ======
end_time = time.time()
end_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
duration = round(end_time - start_time, 2)

# ====== Thông báo hoàn tất ======
print(f"\n✅ Done! Output saved to: {output_file}")
print(f"🕒 End time: {end_dt}")
print(f"⏱️ Duration: {duration} seconds")
print(f"📊 Token usage: {total_tokens} total (Prompt: {prompt_tokens}, Completion: {completion_tokens})")
