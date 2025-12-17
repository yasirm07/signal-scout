# Signal Scout - AI Business Presence Auditor

A simple tool that helps small business owners quickly identify and fix online presence issues. Enter your business name and location, get a health score and prioritized recommendations in under 60 seconds.

---

## 🚀 Quick Start (Local Testing)

### Step 1: Get API Keys

You'll need these API keys to make the app work with real data:

1. **OpenAI API Key** (you already have this!)
   - Get yours from: https://platform.openai.com/api-keys

2. **SerpAPI Key** (for Google Maps/search)
   - Sign up at: https://serpapi.com/users/sign_up
   - Free tier: 100 searches/month
   - Get your API key from: https://serpapi.com/manage-api-key

3. **Firecrawl API Key** (optional - for website crawling)
   - Sign up at: https://firecrawl.dev
   - Free tier available
   - Get your API key from your dashboard

### Step 2: Set Up Backend

1. **Navigate to the backend folder:**
   ```bash
   cd backend
   ```

2. **Create a `.env` file** (this stores your API keys securely):
   ```bash
   # On Mac/Linux:
   touch .env
   
   # Or just create a file named ".env" in the backend folder
   ```

3. **Add your API keys to `.env`:**
   Open the `.env` file and paste this (replace with your actual keys):
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SERP_API_KEY=your_serpapi_key_here
   FIRECRAWL_API_KEY=your_firecrawl_key_here
   ```

4. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Note:** If you get errors, try: `pip3 install -r requirements.txt` or `python -m pip install -r requirements.txt`

5. **Start the backend server:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   
   You should see: `Uvicorn running on http://127.0.0.1:8000`

### Step 3: Open the Frontend

1. **Open the HTML file in your browser:**
   - Navigate to: `frontend/index.html`
   - Right-click → "Open with" → Your browser (Chrome, Safari, etc.)
   - OR drag the file into your browser window

2. **Test it:**
   - Enter a business name (e.g., "Joe's Pizza")
   - Enter a city (e.g., "New York, NY")
   - Click "Analyze my business"
   - Wait ~30-60 seconds for results

---

## 🌐 Making It Live (Deployment)

To turn this into a real website that anyone can access, you need to deploy both parts:

### Option 1: Render.com (Easiest - Recommended)

**Why Render?** Free tier, simple setup, handles both backend and frontend.

#### Deploy Backend:

1. **Create account:** https://render.com (sign up with GitHub)

2. **Create a new Web Service:**
   - Click "New" → "Web Service"
   - Connect your GitHub repo (or upload the code)
   - Settings:
     - **Name:** `signal-scout-backend`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
     - **Root Directory:** `backend`

3. **Add Environment Variables:**
   In Render dashboard, go to "Environment" tab and add:
   - `OPENAI_API_KEY` = (your key)
   - `SERP_API_KEY` = (your key)
   - `FIRECRAWL_API_KEY` = (your key)

4. **Deploy!** Render will give you a URL like: `https://signal-scout-backend.onrender.com`

#### Deploy Frontend:

1. **Update the frontend to use your backend URL:**
   - Open `frontend/index.html`
   - Find the line: `const API_URL = 'http://localhost:8000';`
   - Change it to: `const API_URL = 'https://signal-scout-backend.onrender.com';`

2. **Deploy to Render Static Site:**
   - In Render, click "New" → "Static Site"
   - Connect your repo
   - **Root Directory:** `frontend`
   - **Build Command:** (leave empty)
   - **Publish Directory:** `frontend`
   - Deploy!

3. **You'll get a URL like:** `https://signal-scout.onrender.com`

### Option 2: Railway.app (Alternative)

Similar to Render, but different interface:
- Sign up: https://railway.app
- Create new project → Deploy from GitHub
- Add environment variables
- Deploy backend and frontend separately

### Option 3: Vercel (Frontend) + Render (Backend)

- **Frontend on Vercel:** Free, super fast
  - Sign up: https://vercel.com
  - Import your repo → Set root to `frontend` → Deploy
- **Backend on Render:** (as described above)

---

## 📁 Project Structure

```
Side Projects/
├── backend/              # Python FastAPI server
│   ├── app/
│   │   ├── main.py      # API endpoints
│   │   ├── config.py    # Settings
│   │   ├── schemas.py   # Data models
│   │   ├── integrations/ # API clients (SerpAPI, Firecrawl)
│   │   └── services/    # Business logic
│   └── requirements.txt # Python packages
│
└── frontend/
    └── index.html       # Web interface
```

---

## 🔧 Troubleshooting

### Backend won't start:
- Make sure you're in the `backend` folder
- Check that `.env` file exists and has your keys
- Try: `python -m uvicorn app.main:app --reload --port 8000`

### Frontend can't connect:
- Make sure backend is running on port 8000
- Check browser console (F12) for errors
- Update `API_URL` in `index.html` to match your backend URL

### API errors:
- Verify your API keys are correct in `.env`
- Check SerpAPI/Firecrawl dashboards for usage limits
- The app will work with sample data if keys are missing (for testing)

### Port already in use:
- Change port: `uvicorn app.main:app --reload --port 8001`
- Update frontend `API_URL` to match

---

## 💰 Cost Estimate

**Free tier should be enough for testing:**
- OpenAI: ~$0.01-0.10 per analysis (depends on usage)
- SerpAPI: 100 free searches/month
- Firecrawl: Free tier available
- Render: Free tier (spins down after inactivity, but free)

**For production:** Expect $10-50/month depending on traffic.

---

## 🎯 What You Need From Me

To help you deploy, I need to know:

1. **Do you have a GitHub account?** (Makes deployment easier)
2. **Which deployment option do you prefer?** (Render is easiest)
3. **Do you want me to:**
   - Create a `.env.example` file (template for API keys)?
   - Update the frontend to work with deployed backend?
   - Create a deployment script?

Just let me know and I'll help you get it live! 🚀

