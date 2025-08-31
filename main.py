from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.concurrency import run_in_threadpool
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = FastAPI()

# Templates & Static files mount
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Debug check: API Key
print("🔑 GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))

# Gemini API setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, prompt: str = Form(...)):
    try:
        print("🚀 /generate endpoint hit with prompt:", prompt)

        # Prompt for Gemini
        full_prompt = f"""
        Create a TikTok Challenge Idea.
        Theme: {prompt}

        Format response like this:
        🎯 Generated Challenge for: [Challenge Name]
        Steps:
        Step 1: ...
        Step 2: ...
        Step 3: ...
        Hashtags:
        #hashtag1 #hashtag2 #hashtag3
        """

        model = genai.GenerativeModel("gemini-1.5-flash")

        # Run Gemini in threadpool (safe for FastAPI)
        response = await run_in_threadpool(model.generate_content, full_prompt)

        ai_text = response.text if response and response.text else "❌ No response from AI"
        print("✅ Gemini Response:\n", ai_text)

        return templates.TemplateResponse("result.html", {"request": request, "challenge": ai_text})

    except Exception as e:
        print("❌ Error in /generate:", e)
        return templates.TemplateResponse("result.html", {"request": request, "challenge": f"Error: {str(e)}"})
