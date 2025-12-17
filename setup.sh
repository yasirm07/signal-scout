#!/bin/bash
# Complete setup script for Signal Scout
# Run this from the project root: bash setup.sh

echo "🚀 Setting up Signal Scout..."
echo ""

# Navigate to backend
cd backend

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file with your API keys..."
    echo "⚠️  .env file will be created, but you need to add your API keys manually"
    echo "   See backend/.env.example for the format"
    cat > .env << 'EOF'
# API Keys for Signal Scout
# Add your actual keys here (get them from the setup guides)
OPENAI_API_KEY=your_openai_api_key_here
SERP_API_KEY=your_serpapi_key_here
FIRECRAWL_API_KEY=
EOF
    echo "✅ .env file created!"
else
    echo "⚠️  .env file already exists, skipping..."
fi

echo ""
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Test locally: cd backend && uvicorn app.main:app --reload --port 8000"
echo "2. Open frontend/index.html in your browser"
echo "3. Follow GITHUB_SETUP.md to push to GitHub"
echo "4. Follow DEPLOY.md to deploy to Render"
echo ""

