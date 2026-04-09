#!/bin/bash

# Stop script for scholarship bot
# Stops and removes the bot container

set -e

echo "🛑 Stopping Scholarship Calculator Bot..."

# Check if container is running
if docker compose ps | grep -q "scholarship-bot"; then
    echo "🔄 Stopping container..."
    docker compose down
    
    echo "✅ Bot stopped successfully!"
else
    echo "⚠️  Bot is not running"
fi

echo ""
echo "To start the bot again:"
echo "  ./scripts/start.sh"
echo "  or"
echo "  docker compose up -d"
