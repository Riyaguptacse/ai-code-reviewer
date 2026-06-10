🤖 AI Code Reviewer — Full-Stack GenAI System
Transform raw code into senior-level structured feedback in seconds using LLMs and disciplined prompt engineering.


🎯 What It Does
Most code review tools just lint your code. This system does what a senior engineer does — it analyzes your code and returns:

🐛 Bug Detection — identifies logical errors and edge cases
⚡ Performance Improvements — flags inefficiencies and suggests optimizations
📊 Big-O Complexity Analysis — explains time and space complexity
🔧 Refactored Code — returns production-ready rewritten code
💡 Actionable Feedback — structured, specific, not generic


🛠️ Tech Stack
Layer
Technology
LLM API
Groq API (LLaMA 3)
Backend
FastAPI (Python)
Frontend
Streamlit
Prompt Engineering
Structured output prompting
Deployment
Local / Docker-ready



🚀 How to Run
1. Clone the repo
git clone https://github.com/Riyaguptacse/ai-code-reviewer.git

cd ai-code-reviewer
2. Install dependencies
pip install -r requirements.txt
3. Set your API key
export GROQ_API_KEY=your_key_here
4. Run the app
# Start backend

uvicorn app.main:app --reload

# In a new terminal, start frontend

streamlit run frontend/app.py


🧠 How It Works
User pastes code
↓
FastAPI backend receives request
↓
Structured prompt sent to Groq API (LLaMA 3)
↓
LLM returns JSON with: bugs, improvements, complexity, refactored code
↓
Streamlit frontend renders structured feedback

The key insight: instead of asking the LLM to "review this code" (which gives generic responses), the prompt enforces a strict output schema — making the model behave like a senior engineer doing a structured PR review.


💡 Key Engineering Decisions
Why Groq? Ultra-low latency inference (vs OpenAI) — critical for a real-time code review tool.

Why FastAPI + Streamlit? FastAPI handles API logic cleanly; Streamlit enables rapid UI without frontend overhead.

Why structured prompting? Generic prompts return generic answers. Forcing JSON output with defined fields (bugs, complexity, refactored_code) produces consistent, actionable developer feedback every time.


📊 Results
Reduces code review turnaround from hours to seconds
Generates feedback at the quality level of a senior engineer review
Handles Python, JavaScript, and Java code


🗂️ Project Structure
ai-code-reviewer/

├── app/

│   ├── main.py          # FastAPI app

│   ├── reviewer.py      # LLM prompt logic

│   └── schemas.py       # Pydantic models

├── frontend/

│   └── app.py           # Streamlit UI

├── requirements.txt

├── .env.example

└── README.md


📬 Contact
Riya Gupta — AI/ML Engineer
📧 riyagupta9906@gmail.com
🔗 LinkedIn
🐙 GitHub

