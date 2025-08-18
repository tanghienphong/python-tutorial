import openai
import os
import time
from datetime import datetime

# 1. Cấu hình API Key (nên để ở biến môi trường cho bảo mật)
openai.api_key = os.getenv("OPENAI_API_KEY")  # export OPENAI_API_KEY=sk-...

# Đọc file diff và checklist
with open("git_diff.txt", "r", encoding="utf-8") as f:
    diff_content = f.read()

with open("php_symfony_code_review_checklist.txt", "r", encoding="utf-8") as f:
    checklist = f.read()

# Prompt cho GPT
system_prompt = """
You are a senior PHP/Symfony code reviewer.
Review the following Git diff according to the checklist provided.
Only focus on new or modified lines.
Return the results as:
- Group the issues by file
- For each file, list:
  - File name
  - Issues found
  - Suggestions to fix
- Use Markdown format for better readability
- Focus on:
  - Code quality
  - Security vulnerabilities
  - Performance issues
  - Best practices
  - Symfony-specific conventions

Make sure to provide:
- File name
- Issues found
- Suggestions to fix
- Use clear and concise language
- Avoid unnecessary technical jargon
- Provide actionable feedback
- Use bullet points for clarity
- Include line numbers where applicable

Format your response as follows:
- File name
- Issues found (if any)
  - Line number (if available)
  - Issue description
  - Suggestion to fix
- Suggestions to fix (if any)
  - Line number (if available)
  - Suggestion description
- Use Markdown for formatting
- Ensure the output is well-structured and easy to read

"""

user_prompt = f"""
## Checklist:
{checklist}

## Git Diff:
{diff_content}
"""

# ====== Thời gian bắt đầu ======
start_time = time.time()
start_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"⏳ Start time: {start_dt}")
print("🔍 Loading... Please wait while the AI reviews your code...")

# Gọi GPT API
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.2,
    max_tokens=3000
)

# ====== Kết quả và thông tin token ======
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