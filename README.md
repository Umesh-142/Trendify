# 🚀 TikTok Challenge Generator

Create viral‑ready TikTok challenge ideas in seconds. The app shows **Top 5 trends** on the left and lets users **generate fresh challenge prompts** (steps + hashtags) on the right. Built with **FastAPI + TailwindCSS**, powered by **Gemini**.

---

## ✨ Features

* 🔥 **Live Trends Panel** — Curated Top 5 trends with a sleek, animated UI
* 🎯 **Challenge Generator** — Generates steps + hashtag pills instantly
* 📱 **Fully Responsive** — Mobile‑first, stacks elegantly on small screens
* 🌈 **Modern UI/UX** — Glassmorphism, soft shadows, micro‑interactions
* ⚡ **FastAPI Backend** — Clean endpoints (`/`, `/generate`)
* 🤝 **Plug‑and‑Play** — Works with CDN Tailwind; optional production build

---

## 🧱 Tech Stack

**Frontend**: HTML5, TailwindCSS (CDN or CLI build)

**Backend**: Python 3.10+, FastAPI, Uvicorn

**AI**: Google Gemini (`gemini‑1.5‑flash`)

---

## 📦 Project Structure

```
GenAi/
├─ main.py
├─ .env
├─ templates/
│  ├─ index.html
│  └─ result.html
└─ static/
   └─ (optional assets)
```

---

## 🔧 Setup (Local)

> Prereq: Python 3.10+, pip, a Google Gemini API key.

1. **Clone & enter**

```bash
git clone https://github.com/your-username/tiktok-challenge-generator.git
cd tiktok-challenge-generator  # or your folder name (GenAi)
```

2. **Create venv & install deps**

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install fastapi uvicorn python-dotenv google-generativeai jinja2
```

3. **Add secrets** → `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

4. **Run dev server**

```bash
uvicorn main:app --reload
```

5. Open: `http://127.0.0.1:8000/`

---

## 🧠 Environment Notes

* Ensure your key is loaded in the process environment (`python-dotenv` reads `.env`).
* If you see `models/gemini-pro not found`, switch to `gemini-1.5-flash` (already used here).

---

## 🗺️ API Routes

* `GET /` → Renders **index.html** (Trends + Generator)
* `POST /generate` → Accepts `prompt` → Returns **result.html** with parsed **Steps** + **Hashtags**

**Sample Request (form POST):**

```
prompt = "Comedy"
```

**Sample Parsed Response:**

```json
{
  "steps": "Step 1: ...\nStep 2: ...\nStep 3: ...",
  "hashtags": ["#trending", "#fun", "#tiktokchallenge"]
}
```

---

## 🎨 UI/UX Highlights

* Gradient backgrounds: dark neon vibe
* Glassmorphism container with backdrop blur
* Cards with accent left borders
* Hashtags rendered as rounded pills
* Smooth hover & scale micro‑interactions
* Mobile: generator card first, trends below (reversed via `order-*` classes)

---

## 🛡️ Production Build (Tailwind)

CDN is perfect for quick demos. For production:

1. **Install build toolchain**

```bash
npm init -y
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

2. **Create input CSS** → `static/tailwind.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

3. **Build (minified)**

```bash
npx tailwindcss -i ./static/tailwind.css -o ./static/output.css --minify
```

4. **Use in templates**

```html
<link rel="stylesheet" href="/static/output.css">
```

---

## 🧩 Troubleshooting

* **Blank AI response** → Check `GEMINI_API_KEY` and console logs in `main.py`.
* **CORS / 404 on static** → Ensure `app.mount("/static", StaticFiles(directory="static"), name="static")` is present.
* **Model 404** → Prefer `gemini-1.5-flash`, confirm library version `google-generativeai`.
* **Emoji/Unicode issues** → Make sure templates have `<meta charset="UTF-8">`.

---

## 📸 Screenshots / Demo

> Drop screenshots or a GIF here for instant context.

* **Home**: Trends + Generator
* **Result**: Steps + Hashtag pills

---

## 🧭 Roadmap

* ⏱️ Loading state & skeletons
* 💬 Copy‑to‑clipboard for steps/hashtags
* 🔄 Regenerate button on result page
* 🔗 Share card (Open Graph friendly)
* 🌍 i18n (Hinglish/Hindi toggle)
* 🧠 Cache last N generations

---

## 🤝 Contributing

PRs welcome! Please:

1. Fork
2. Create feature branch: `git checkout -b feat/your-idea`
3. Commit, push, open PR

---

## 📜 License

MIT © 2025 — Your Name

---

## 🙌 Credits

* UI: TailwindCSS
* Backend: FastAPI
* AI: Gemini (`gemini-1.5-flash`)

> Made with ❤️ for creators. Go make something viral!
