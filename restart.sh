#!/bin/bash

# Restart script for scholarship bot
# Restarts the bot container

set -e

echo "🔄 Restarting Scholarship Calculator Bot..."

# Check if container is running
if docker compose ps | grep -q "scholarship-bot"; then
    echo "🔄 Restarting container..."
    docker compose restart bot
    
    # Wait for bot to restart
    echo "⏳ Waiting for bot to restart..."
    sleep 3
    
    echo "✅ Bot restarted successfully!"
    echo ""
    echo "📊 To monitor logs:"
    echo "  docker compose logs -f"
else
    echo "⚠️  Bot is not running. Starting now..."
    docker compose up -d --build
    echo "✅ Bot started!"
fi
