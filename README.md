# AI Advisory Panel

A powerful web application that allows users to get responses from multiple AI models simultaneously and optionally generate a summary of their combined responses.

## Features

- **Multiple AI Model Support**: Currently supports three AI models:
  - Gemini
  - DeepSeek
  - Llama
- **Parallel Processing**: Get responses from multiple AI models in a single request
- **Summary Generation**: Optionally generate a summary of all responses using any of the supported models
- **Markdown Support**: Responses are rendered with markdown formatting
- **Modern Web Interface**: Clean and intuitive user interface

## Prerequisites

- Python 3.x
- Flask
- OpenAI Python client
- python-dotenv

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sqasimalis/AI-Advisory-Panel.git
cd AI-Advisory-Panel
```

2. Create a `.env` file in the root directory with your API keys:
```
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:XXXX`

3. Enter your prompt and select the AI models you want to use

4. Optionally, you can:
   - Request a summary of all responses
   - Choose which model to use for the summary
   - Provide a specific prompt for the summary

## Project Structure

```
AI-Advisory-Panel/
├── app.py              # Main Flask application
├── services/           # AI model service implementations
│   ├── gemini.py
│   ├── deepseek.py
│   └── llama.py
├── templates/          # HTML templates
│   └── index.html
└── .env               # Environment variables (not tracked in git)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.