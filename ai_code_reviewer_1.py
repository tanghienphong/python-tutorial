import openai
import os

# 1. Cấu hình API Key (nên để ở biến môi trường cho bảo mật)
openai.api_key = os.getenv("OPENAI_API_KEY")  # export OPENAI_API_KEY=sk-...

# 2. Đọc file diff và checklist
with open("git_diff.txt", "r", encoding="utf-8") as f:
    diff_content = f.read()

with open("php_symfony_code_review_checklist.txt", "r", encoding="utf-8") as f:
    checklist = f.read()

# 3. Prompt gửi vào GPT
system_prompt = """
You are a senior PHP/Symfony code reviewer.
Review the following Git diff according to the checklist provided.
Only focus on new or modified lines.
Return the results as:
- Line (if any)
- Issue found
- Suggestion to fix
"""

user_prompt = f"""
## Checklist:
{checklist}

## Git Diff:
{diff_content}
"""

# 4. Gọi GPT API
response = openai.ChatCompletion.create(
    model="gpt-4o",  # hoặc "gpt-4"
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.2,
    max_tokens=3000
)

# 5. In ra kết quả
print("\n📋 Code Review Output:\n")
print(response["choices"][0]["message"]["content"])
