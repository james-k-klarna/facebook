# Jira Landscape 3D Visualization

A 3D interactive visualization featuring Jira notifications floating around a central image with Matrix-style digital rain effects.

## 🚀 Deployment for Static Web Servers

### Option 1: GitHub Pages (Recommended)
1. **Upload files to GitHub repository:**
   - `jira-landscape.html` (main file)
   - `realjira.png` (your image)
   - `README.md` (this file)

2. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Select "Deploy from a branch" → main branch
   - Your site will be available at: `https://yourusername.github.io/repository-name/jira-landscape.html`

### Option 2: Netlify (Easy Drag & Drop)
1. **Visit [netlify.com](https://netlify.com)**
2. **Drag and drop your folder** containing the HTML and PNG files
3. **Your site is live instantly!**

### Option 3: Vercel
1. **Visit [vercel.com](https://vercel.com)**
2. **Import your GitHub repository** or upload files directly
3. **Deploy with one click**

## 📁 Required Files
- `jira-landscape.html` - Main 3D visualization
- `realjira.png` - Your central image (any PNG file works)

## 🎮 Controls
- **Mouse drag**: Rotate camera
- **Scroll wheel**: Zoom in/out
- **Space bar**: Toggle auto-rotation

## 🔧 Technical Details
- **Framework**: Three.js
- **No server required**: Pure client-side JavaScript
- **Image loading**: Automatic fallback if image fails to load
- **Responsive**: Works on desktop and mobile

## 🎨 Features
- **3D Jira notification cards** with realistic styling
- **Matrix-style digital rain** in multiple layers
- **Central rotating image** (your screenshot)
- **Interactive hover effects**
- **Dimensionless void** (no floor/ceiling)
- **Smooth animations** and lighting

## 📝 Customization
To change the central image:
1. Replace `realjira.png` with your image
2. Keep the same filename or update the path in the HTML
3. Recommended size: 800x600px or similar aspect ratio

The visualization will work with any static web hosting service that serves files over HTTP/HTTPS.
