# AI ChatBot Frontend

A modern React frontend for the AI ChatBot Agent with support for math, weather, web search, code execution, and email integration.

## Features

- 💬 Real-time chat interface
- 🧮 Math tools (addition, subtraction, calculus, scientific calculations)
- 🌤️ Weather information
- 🔍 Web search integration
- 🐍 Python code execution
- 📧 Gmail integration
- 📊 CSV data analysis
- 💾 Session-based chat history
- 🎨 Modern, responsive UI with Tailwind CSS

## Prerequisites

- Node.js 16+ 
- Backend running on `http://localhost:8000`

## Installation

```bash
cd frontend
npm install
```

## Development

Start the development server:

```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Building

Build for production:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ChatHeader.jsx      # Header with title and clear button
│   │   ├── ChatInput.jsx       # Message input component
│   │   ├── LoadingDots.jsx     # Loading animation
│   │   ├── Message.jsx         # Individual message display
│   │   └── ToolsInfo.jsx       # Available tools information
│   ├── api/
│   │   └── chatApi.js          # API service for backend communication
│   ├── App.jsx                 # Main app component
│   ├── main.jsx                # Entry point
│   └── index.css               # Tailwind CSS styles
├── index.html
├── vite.config.js              # Vite configuration
├── tailwind.config.js          # Tailwind configuration
└── package.json
```

## Available Commands

Ask the chatbot to:

### Math Operations
- "Calculate 2 + 2"
- "What is 10 * 5?"
- "Integrate x^2"
- "Differentiate 3x^2 + 2x"

### Weather
- "What's the weather in London?"
- "Tell me the weather in New York"

### Web Search
- "Search for Python programming tips"
- "What is the latest news about AI?"

### Code Execution
- "Execute Python: print('Hello World')"
- "Run Python code to calculate factorial of 5"

### Email
- "Send an email saying..."

## API Endpoints

The frontend communicates with these backend endpoints:

- `POST /chat` - Send a message to the chatbot
- `POST /email` - Send an email through the agent

## Configuration

Update the API base URL in `src/api/chatApi.js` if your backend is on a different port or host.

## Troubleshooting

**Cannot connect to backend:**
- Ensure the FastAPI backend is running on `http://localhost:8000`
- Check CORS settings if running on different domains
- Verify Redis is running (required for session history)

**Messages not persisting:**
- Ensure Redis server is running
- Check backend logs for errors

## Technologies Used

- React 18
- Vite
- Tailwind CSS
- Axios
- Lucide React Icons

## License

MIT
