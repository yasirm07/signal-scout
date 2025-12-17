# 🎯 Step-by-Step Setup Guide

This is a simplified guide for non-technical users. Follow these steps in order.

---

## Part 1: Get Your API Keys

### ✅ OpenAI (You Already Have This!)
- Get yours from: https://platform.openai.com/api-keys
- ✅ Done!

### 🔑 SerpAPI (For Google Maps Search)

1. Go to: https://serpapi.com/users/sign_up
2. Sign up (free account gives 100 searches/month)
3. After signing up, go to: https://serpapi.com/manage-api-key
4. Copy your API key (looks like: `abc123def456...`)
5. **Save it somewhere safe** - you'll need it in Step 2

### 🔑 Firecrawl (Optional - For Website Crawling)

1. Go to: https://firecrawl.dev
2. Sign up for free account
3. Go to your dashboard and copy your API key
4. **Save it somewhere safe**

---

## Part 2: Set Up Backend (Local Testing)

### Step 1: Open Terminal

- **Mac:** Press `Cmd + Space`, type "Terminal", press Enter
- **Windows:** Press `Win + R`, type "cmd", press Enter

### Step 2: Navigate to Backend Folder

Type this command (press Enter after each line):

```bash
cd "/Users/yasirmohammad/Side Projects/backend"
```

> **Tip:** If that doesn't work, try: `cd ~/Side\ Projects/backend`

### Step 3: Create .env File

**On Mac/Linux:**
```bash
touch .env
```

**On Windows:**
```bash
type nul > .env
```

**Or manually:**
- Open the `backend` folder in Finder/File Explorer
- Create a new file named `.env` (yes, with the dot at the start)

### Step 4: Add Your API Keys to .env

Open the `.env` file in a text editor and paste this:

```
OPENAI_API_KEY=your_openai_api_key_here
SERP_API_KEY=paste_your_serpapi_key_here
FIRECRAWL_API_KEY=paste_your_firecrawl_key_here
```

Replace `paste_your_serpapi_key_here` with your actual SerpAPI key from Part 1.
Replace `paste_your_firecrawl_key_here` with your actual Firecrawl key (or leave it empty if you skip it).

### Step 5: Install Python Packages

In Terminal (still in the backend folder), type:

```bash
pip install -r requirements.txt
```

> **If you get an error:**
> - Try: `pip3 install -r requirements.txt`
> - Or: `python -m pip install -r requirements.txt`
> - Or: `python3 -m pip install -r requirements.txt`

Wait for it to finish (may take 1-2 minutes).

### Step 6: Start the Backend Server

Type:

```bash
uvicorn app.main:app --reload --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Keep this terminal window open!** The server needs to keep running.

---

## Part 3: Test the Frontend

### Step 1: Open the HTML File

1. Navigate to the `frontend` folder
2. Find `index.html`
3. Double-click it (or right-click → Open With → Chrome/Safari)

### Step 2: Test It

1. Enter a business name (e.g., "Joe's Pizza")
2. Enter a city (e.g., "New York, NY")
3. Click "Analyze my business"
4. Wait 30-60 seconds
5. You should see results!

---

## Part 4: Make It Live (Deploy to Internet)

### Option A: Render.com (Easiest)

#### 1. Create GitHub Account (if you don't have one)

- Go to: https://github.com
- Sign up (free)
- Create a new repository (call it "signal-scout" or similar)
- Upload your code to GitHub

#### 2. Deploy Backend on Render

1. Go to: https://render.com
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Fill in:
   - **Name:** `signal-scout-backend`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory:** `backend`
6. Go to "Environment" tab, add:
   - `OPENAI_API_KEY` = (your key)
   - `SERP_API_KEY` = (your key)
   - `FIRECRAWL_API_KEY` = (your key)
7. Click "Create Web Service"
8. Wait 5-10 minutes for deployment
9. Copy your URL (looks like: `https://signal-scout-backend.onrender.com`)

#### 3. Update Frontend

1. Open `frontend/index.html`
2. Find the line: `const API_URL = "http://localhost:8000";`
3. Change it to: `const API_URL = "https://signal-scout-backend.onrender.com";` (use your actual URL)
4. Save the file

#### 4. Deploy Frontend on Render

1. In Render, click "New" → "Static Site"
2. Connect your GitHub repo
3. Fill in:
   - **Root Directory:** `frontend`
   - **Build Command:** (leave empty)
   - **Publish Directory:** `frontend`
4. Click "Create Static Site"
5. Wait 5 minutes
6. You'll get a URL like: `https://signal-scout.onrender.com`

**🎉 Done! Your app is live!**

---

## Need Help?

**Common Issues:**

1. **"Module not found"** → Run `pip install -r requirements.txt` again
2. **"Port already in use"** → Change port to 8001 in the uvicorn command
3. **Frontend can't connect** → Make sure backend is running and check the URL
4. **API errors** → Check your `.env` file has correct keys

**Still stuck?** Let me know what error you're seeing and I'll help!

