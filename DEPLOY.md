# 🚀 Deployment Guide - Signal Scout

This guide will help you deploy your app to the internet in about 10 minutes.

---

## Step 1: Push Code to GitHub

### Option A: Using GitHub Desktop (Easiest)

1. Download GitHub Desktop: https://desktop.github.com
2. Sign in with your account (yasrim07)
3. Click "File" → "Add Local Repository"
4. Select this folder: `/Users/yasirmohammad/Side Projects`
5. Click "Publish repository"
6. Name it: `signal-scout` (or whatever you want)
7. Make sure "Keep this code private" is UNCHECKED (so Render can access it)
8. Click "Publish repository"

### Option B: Using Terminal (Command Line)

Open Terminal and run these commands:

```bash
cd "/Users/yasirmohammad/Side Projects"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Signal Scout app"

# Add your GitHub repo (replace YOUR_REPO_NAME with what you want)
git remote add origin https://github.com/yasrim07/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**First time?** You might need to:
1. Create the repo on GitHub first: https://github.com/new
2. Name it: `signal-scout` (or whatever you want)
3. Don't initialize with README
4. Copy the repo URL and use it in the `git remote add` command above

---

## Step 2: Deploy Backend on Render

1. **Go to Render:** https://render.com
2. **Sign up/Login** (use "Sign in with GitHub" - easiest!)
3. **Click "New" → "Web Service"**
4. **Connect your repository:**
   - Click "Connect account" if needed
   - Find your `signal-scout` repo
   - Click "Connect"
5. **Configure the service:**
   - **Name:** `signal-scout-backend`
   - **Environment:** `Python 3`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** `backend` ⚠️ **IMPORTANT!**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. **Add Environment Variables:**
   - Click "Advanced" → "Add Environment Variable"
   - Add these three:
     ```
     OPENAI_API_KEY = your_openai_api_key_here
     SERP_API_KEY = your_serpapi_key_here
     FIRECRAWL_API_KEY = (leave empty or add if you have one)
     ```
7. **Click "Create Web Service"**
8. **Wait 5-10 minutes** for deployment
9. **Copy your backend URL** (looks like: `https://signal-scout-backend.onrender.com`)

---

## Step 3: Update Frontend to Use Your Backend

1. **Open:** `frontend/index.html`
2. **Find this line** (around line 87):
   ```javascript
   const API_URL = "http://localhost:8000";
   ```
3. **Replace with your Render backend URL:**
   ```javascript
   const API_URL = "https://signal-scout-backend.onrender.com";
   ```
   (Use the actual URL from Step 2)
4. **Save the file**
5. **Commit and push to GitHub:**
   ```bash
   git add frontend/index.html
   git commit -m "Update frontend to use deployed backend"
   git push
   ```

---

## Step 4: Deploy Frontend on Render

1. **In Render dashboard, click "New" → "Static Site"**
2. **Connect your repository** (same `signal-scout` repo)
3. **Configure:**
   - **Name:** `signal-scout-frontend`
   - **Branch:** `main`
   - **Root Directory:** `frontend` ⚠️ **IMPORTANT!**
   - **Build Command:** (leave empty)
   - **Publish Directory:** `frontend`
4. **Click "Create Static Site"**
5. **Wait 5 minutes**
6. **You'll get a URL like:** `https://signal-scout.onrender.com`

**🎉 Your app is now live!** Share that URL with anyone!

---

## Troubleshooting

### Backend won't deploy:
- Check that "Root Directory" is set to `backend`
- Verify environment variables are set correctly
- Check Render logs for errors

### Frontend can't connect:
- Make sure you updated `API_URL` in `index.html`
- Check browser console (F12) for errors
- Verify backend URL is correct (no trailing slash)

### CORS errors:
- Backend should already have CORS enabled
- If issues persist, check `backend/app/main.py` has CORS middleware

---

## Updating Your App

Whenever you make changes:

1. **Make your changes locally**
2. **Test locally** (run backend, open frontend)
3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
4. **Render will automatically redeploy** (takes 5-10 minutes)

---

## Cost

**Free tier on Render:**
- ✅ Free for both backend and frontend
- ⚠️ Backend spins down after 15 min of inactivity (wakes up on first request)
- ⚠️ Free tier has some limits, but fine for testing/small usage

**For production:** Consider paid tier ($7/month) for always-on backend.

---

## Need Help?

If something goes wrong:
1. Check Render logs (in dashboard)
2. Check browser console (F12)
3. Verify all environment variables are set
4. Make sure Root Directory is correct for both services

Good luck! 🚀

