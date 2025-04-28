#!/bin/sh

echo "Pulling model llama3:8b..."

pull_model_response=$(curl -s -X POST ollama.agentic-rag-app.orb.local/api/pull \
    -H "Content-Type: application/json" \
    -d '{"name": "llama3:8b", "stream": false}')

status=$(echo "$pull_model_response" | grep -o '"status":"[^"]*' | cut -d':' -f2 | tr -d '"')

if [ "$status" = "success" ]; then
    echo "Image pulled successfully!"

    health_check_response=$(curl -X POST ollama.agentic-rag-app.orb.local/api/generate -d '{"model": "llama3:8b", "prompt": "This is a health check. Respond with the number 200, if model is running", "stream": false}')

    health_status=$(echo "$health_check_response" | grep -o '"response":"[^"]*' | cut -d':' -f2 | tr -d '"')

    if [ "$health_status" = "200" ]; then
        echo "Model running!"
    else
        echo "Failed to connect to model"
    fi
else
    echo "Failed to pull the model. Status: $status"
fi
