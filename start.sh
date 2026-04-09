#!/bin/bash

# Start script for scholarship bot
# Builds and starts the bot container

set -e

echo "🚀 Starting Scholarship Calculator Bot..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "📋 Creating .env from template..."
    cp .env.docker.example .env
    echo "⚠️  Please edit .env file and add your BOT_TOKEN"
    echo ""
    echo "To get a BOT_TOKEN:"
    echo "  1. Open Telegram and search for @BotFather"
    echo "  2. Send /newbot command"
    echo "  3. Follow the instructions"
    echo "  4. Copy the token to .env file"
    echo ""
    read -p "Press Enter after you've updated .env file..."
fi

# Check if BOT_TOKEN is set
BOT_TOKEN=$(grep BOT_TOKEN .env | cut -d '=' -f2)
if [ -z "$BOT_TOKEN" ] || [ "$BOT_TOKEN" = "your_bot_token_here" ]; then
    echo "❌ Error: BOT_TOKEN is not configured!"
    echo "Please edit .env file and add your bot token from @BotFather"
    exit 1
fi

# Build and start
echo "🔨 Building Docker image..."
docker compose build

echo "🚀 Starting services..."
docker compose up -d

# Wait for bot to start
echo "⏳ Waiting for bot to start..."
sleep 3

# Check status
if docker compose ps | grep -q "scholarship-bot.*Up"; then
    echo ""
    echo "✅ Bot started successfully!"
    echo ""
    echo "📱 To test the bot:"
    echo "  1. Open Telegram"
    echo "  2. Search for your bot by username"
    echo "  3. Send /start command"
    echo ""
    echo "📊 To monitor the bot:"
    echo "  docker compose logs -f"
    echo ""
    echo "🛑 To stop the bot:"
    echo "  docker compose down"
else
    echo ""
    echo "❌ Bot failed to start!"
    echo "Check logs with: docker compose logs"
    exit 1
fi
