# 📦 Quick GitHub Setup

Follow these steps to push your code to GitHub.

---

## Step 1: Create Repository on GitHub

1. Go to: https://github.com/new
2. **Repository name:** `signal-scout` (or whatever you prefer)
3. **Description:** "AI Business Presence Auditor - Find and fix online presence issues"
4. **Visibility:** Public (so Render can access it)
5. **DO NOT** check "Initialize with README" (we already have files)
6. Click "Create repository"

---

## Step 2: Push Your Code

### Using Terminal (Recommended)

Open Terminal and run:

```bash
# Navigate to your project
cd "/Users/yasirmohammad/Side Projects"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial commit - Signal Scout app"

# Add GitHub as remote (replace YOUR_REPO_NAME with what you created)
git remote add origin https://github.com/yasrim07/signal-scout.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**First time pushing?** GitHub will ask for your username and password/token:
- Username: `yasrim07`
- Password: Use a **Personal Access Token** (not your GitHub password)
  - Get one here: https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Check "repo" scope
  - Copy the token and use it as password

### Using GitHub Desktop (Easier Alternative)

1. Download: https://desktop.github.com
2. Sign in with `yasrim07`
3. File → Add Local Repository
4. Select: `/Users/yasirmohammad/Side Projects`
5. Click "Publish repository"
6. Name: `signal-scout`
7. Make sure "Keep this code private" is **UNCHECKED**
8. Click "Publish"

---

## Step 3: Verify

Go to: https://github.com/yasrim07/signal-scout

You should see all your files! ✅

---

## Next Steps

Now that your code is on GitHub, follow `DEPLOY.md` to deploy to Render!

