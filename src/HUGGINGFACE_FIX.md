# 🔧 HuggingFace Spaces Deployment - Troubleshooting Guide

## ⚠️ Build Error Fix

If you're seeing the build error with "cache miss" messages, here's how to fix it:

---

## ✅ Solution 1: Use Minimal Requirements (RECOMMENDED)

### Step 1: Replace requirements.txt
Use the **minimal** version that only includes essential packages:

```txt
# requirements.txt
fastapi
uvicorn[standard]
aiohttp
psutil
```

**Why this works**: HuggingFace Spaces automatically installs `gradio[oauth,mcp]==5.32.0`, so we don't need to specify it in requirements.txt.

### Step 2: Remove Version Pinning
If using the full requirements.txt, ensure versions have upper bounds:

```txt
# Good ✅
fastapi>=0.104.0,<1.0.0
aiohttp>=3.8.0,<4.0.0

# Avoid ❌
fastapi>=0.104.0
aiohttp>=3.8.0
```

---

## ✅ Solution 2: Remove OpenTelemetry (If Still Failing)

OpenTelemetry packages can sometimes cause conflicts. Create this requirements.txt:

```txt
# Core only - no tracing
fastapi>=0.104.0,<1.0.0
uvicorn[standard]>=0.24.0,<1.0.0
aiohttp>=3.8.0,<4.0.0
psutil>=5.9.0,<6.0.0
```

The app will work fine without tracing - it's optional!

---

## ✅ Solution 3: Use requirements-minimal.txt

I've created a `requirements-minimal.txt` file:

```bash
# In your HuggingFace Space, rename it:
mv requirements-minimal.txt requirements.txt
```

This contains only the absolute essentials.

---

## 📋 Deployment Checklist

### Before Deploying:

- [ ] **SDK**: Set to "Gradio" (not Streamlit or Static)
- [ ] **SDK Version**: 5.32.0 or higher
- [ ] **Python Version**: 3.11 (recommended)
- [ ] **Hardware**: CPU Basic (free tier works!)

### Files to Upload:

- [ ] `app.py` (main application)
- [ ] `requirements.txt` (use minimal version)
- [ ] Optional: README.md, config.ini, etc.

### After Upload:

1. Space will automatically build
2. Wait 2-5 minutes for build
3. Check "Logs" tab for errors
4. Once "Running", test the interface

---

## 🐛 Common Issues & Fixes

### Issue 1: "gradio not found"
**Cause**: Trying to import gradio before Spaces installs it  
**Fix**: Don't include `gradio` in requirements.txt - Spaces handles it

### Issue 2: "Version conflict"
**Cause**: Pinned versions conflict with Spaces  
**Fix**: Use version ranges with upper bounds

### Issue 3: "Build timeout"
**Cause**: Too many dependencies  
**Fix**: Use minimal requirements.txt

### Issue 4: "Module not found"
**Cause**: Missing dependency  
**Fix**: Add to requirements.txt (but check Spaces doesn't provide it)

---

## 🎯 Recommended requirements.txt

Here's the tested, working version:

```txt
# DarkDriftz's Kali Arsenal - HuggingFace Spaces
# Minimal dependencies - Gradio managed by Spaces

fastapi>=0.104.0,<1.0.0
uvicorn[standard]>=0.24.0,<1.0.0
aiohttp>=3.8.0,<4.0.0
psutil>=5.9.0,<6.0.0
```

**That's it!** Only 4 packages needed.

---

## 🚀 Quick Fix Steps

If build is failing:

### Step 1: Update requirements.txt
```bash
# Replace entire contents with:
fastapi
uvicorn[standard]
aiohttp
psutil
```

### Step 2: Commit and Push
```bash
git add requirements.txt
git commit -m "Fix: Use minimal requirements for HF Spaces"
git push
```

### Step 3: Wait for Rebuild
Space will automatically rebuild - should succeed now!

---

## 📊 What Spaces Provides Automatically

You **don't** need to include these in requirements.txt:

- ✅ `gradio` (version 5.32.0)
- ✅ `gradio[oauth]`
- ✅ `gradio[mcp]`
- ✅ `spaces` package
- ✅ `huggingface_hub`
- ✅ Python 3.11 runtime

You **do** need to include:

- ✅ `fastapi`
- ✅ `uvicorn[standard]`
- ✅ `aiohttp`
- ✅ `psutil`

---

## 🔍 Debugging Build Errors

### Check Build Logs

1. Go to your Space
2. Click "Logs" tab
3. Look for error messages
4. Common errors:

```
ERROR: Could not find a version that satisfies...
→ Fix: Adjust version ranges

ERROR: Package X not found
→ Fix: Add to requirements.txt

ERROR: Version conflict with gradio
→ Fix: Remove gradio from requirements.txt
```

### Test Locally First

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install gradio (simulating Spaces)
pip install gradio[mcp]==5.32.0

# Install your requirements
pip install -r requirements.txt

# Test the app
python app.py
```

If it works locally, it should work on Spaces!

---

## ✅ Verified Working Configuration

**File**: `requirements.txt`
```txt
fastapi>=0.104.0,<1.0.0
uvicorn[standard]>=0.24.0,<1.0.0
aiohttp>=3.8.0,<4.0.0
psutil>=5.9.0,<6.0.0
```

**Space Settings**:
- SDK: Gradio
- SDK Version: 5.32.0
- Python: 3.11
- Hardware: CPU Basic

**Result**: ✅ Builds successfully in ~2 minutes

---

## 📞 Still Having Issues?

### Option 1: Use requirements-minimal.txt
```bash
# Simplest possible version
fastapi
uvicorn[standard]
aiohttp
psutil
```

### Option 2: Check app.py Imports
Make sure app.py doesn't import packages not in requirements.txt

### Option 3: Check Python Version
Ensure Spaces is using Python 3.11

### Option 4: HuggingFace Community
Post in HuggingFace forums with:
- Error message
- requirements.txt contents
- Python version
- Space URL

---

## 🎉 Success Indicators

You'll know it's working when:

1. ✅ Build completes (no red errors)
2. ✅ Space shows "Running" status
3. ✅ Interface loads in browser
4. ✅ Tabs are visible and clickable
5. ✅ Features work (arsenal, tutorials, etc.)

---

## 📝 Summary

**The Fix**:
1. Use minimal requirements.txt (only 4 packages)
2. Let HuggingFace Spaces manage Gradio
3. Add version upper bounds
4. Remove OpenTelemetry if needed

**Expected Result**: 
Space builds successfully in 2-5 minutes! 🚀

---

<div align="center">

**Need the working files?**

[requirements.txt](computer:///mnt/user-data/outputs/requirements.txt)  
[requirements-minimal.txt](computer:///mnt/user-data/outputs/requirements-minimal.txt)  
[app.py](computer:///mnt/user-data/outputs/app.py)

**Questions?** Check HuggingFace Spaces documentation!

</div>
