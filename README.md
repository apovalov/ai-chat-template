# Python Chatbot Template

A FastAPI application that provides a chat interface for any LLM which supports the OpenAI interface.

This is a clean, production-ready template for building chatbot applications with Python. It supports any LLM that implements the OpenAI API format.

It is expected that the client will handle the raised exceptions and provide a user-friendly error message to the user in case of invalid input (422).

## Prerequisites

### uv Package Manager

- We need to install the uv package manager locally to manage dependencies in the .venv
- To install follow: https://docs.astral.sh/uv/getting-started/installation/

### just

- To install follow: https://github.com/casey/just

### LLM

- To stay LLM agnostic, we use the OpenAI interface so that we can easily switch to any other LLM that supports the OpenAI interface.
  - You can even use the OpenAI API directly, adjust the .env file with the correct API key, host and model name.
- We recommend using Ollama for local development.
- To install Ollama follow: https://ollama.com/download

### pre-commit

- If you are planning to contribute to the project, you will need to install pre-commit hooks.
- To install follow: https://pre-commit.com/#install

## Setup

```
# Copy the .env.example file to .env and update the .env file with the correct LLM details.
cp .env.example .env

# Create .venv and install dependencies
uv sync

# Install pre-commit hooks
pre-commit install

# Start ollama
just ollama llama3.2
# You can use any model supported by ollama
# For OpenAI API, set LLM_HOST=https://api.openai.com/ and LLM_API_KEY=your_api_key

# Run server
just server
```

## Testing

```
just test  # runs unit tests

curl -X 'POST'   'http://0.0.0.0:8080/question'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "text": "Hello, how can you help me today?"
}'
```

If you open http://0.0.0.0:8080 you will be redirected to the SwaggerUI where you can test the API.

## Features

- RESTful API with FastAPI
- OpenAI-compatible interface (works with OpenAI, Ollama, and other compatible LLMs)
- Input validation and error handling
- Async/await support for better performance
- Retry logic with exponential backoff
- Comprehensive testing setup
- Load testing with Locust
- Pre-commit hooks for code quality
