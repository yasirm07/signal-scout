# ⚡ Quick Start - Signal Scout

**Everything is set up!** Follow these steps to get your app running and live.

---

## 🧪 Test Locally (5 minutes)

### Step 1: Run Setup Script

```bash
cd "/Users/yasirmohammad/Side Projects"
bash setup.sh
```

This will:
- ✅ Create `.env` file with your API keys
- ✅ Install all Python dependencies

### Step 2: Start Backend

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

Keep this terminal open! You should see: `Uvicorn running on http://127.0.0.1:8000`

### Step 3: Test Frontend

1. Open `frontend/index.html` in your browser (double-click it)
2. Enter a business name (e.g., "Joe's Pizza")
3. Enter a city (e.g., "New York, NY")
4. Click "Analyze my business"
5. Wait 30-60 seconds for results!

**✅ If you see results, everything works!**

---

## 🌐 Make It Live (15 minutes)

### Step 1: Push to GitHub

**Option A: Use Terminal**
```bash
cd "/Users/yasirmohammad/Side Projects"

# Create repo on GitHub first: https://github.com/new
# Name it: signal-scout
# Then run:

git add .
git commit -m "Initial commit - Signal Scout"
git branch -M main
git remote add origin https://github.com/yasrim07/signal-scout.git
git push -u origin main
```

**Option B: Use GitHub Desktop** (easier)
- Download: https://desktop.github.com
- Sign in with `yasrim07`
- File → Add Local Repository → Select this folder
- Publish repository (name: `signal-scout`)

### Step 2: Deploy on Render

1. **Go to:** https://render.com
2. **Sign in with GitHub**
3. **Deploy Backend:**
   - New → Web Service
   - Connect `signal-scout` repo
   - Name: `signal-scout-backend`
   - Root Directory: `backend` ⚠️
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Add environment variables:
     - `OPENAI_API_KEY` = `your_openai_api_key_here`
     - `SERP_API_KEY` = `your_serpapi_key_here`
   - Create Web Service
   - Wait 5-10 min, copy the URL (e.g., `https://signal-scout-backend.onrender.com`)

4. **Update Frontend:**
   - Open `frontend/index.html`
   - Find: `const API_URL = "http://localhost:8000";`
   - Change to: `const API_URL = "https://signal-scout-backend.onrender.com";` (use your actual URL)
   - Save, commit, push:
     ```bash
     git add frontend/index.html
     git commit -m "Update frontend for production"
     git push
     ```

5. **Deploy Frontend:**
   - In Render: New → Static Site
   - Connect `signal-scout` repo
   - Name: `signal-scout-frontend`
   - Root Directory: `frontend` ⚠️
   - Publish Directory: `frontend`
   - Create Static Site
   - Wait 5 min

**🎉 Done! Your app is live!**

---

## 📚 More Details

- **Full setup guide:** `SETUP_GUIDE.md`
- **GitHub setup:** `GITHUB_SETUP.md`
- **Deployment guide:** `DEPLOY.md`
- **General info:** `README.md`

---

## 🆘 Need Help?

**Backend won't start?**
- Make sure you ran `bash setup.sh` first
- Check that `.env` exists in `backend/` folder

**Frontend can't connect?**
- Make sure backend is running on port 8000
- Check browser console (F12) for errors

**Deployment issues?**
- Check Render logs in dashboard
- Verify Root Directory is set correctly (`backend` for backend, `frontend` for frontend)
- Make sure environment variables are added

Good luck! 🚀

