import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("GROQ KEY:", os.getenv("GROQ_API_KEY"))
def review_code(language, code):

    prompt = f"""
You are a senior software engineer.

Review this {language} code.

Return:
1. Bugs
2. Improvements
3. Complexity (time & space)
4. Refactored code

Code:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return {
        "review": response.choices[0].message.content
    }