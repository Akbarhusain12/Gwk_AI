# AI Workflow Builder 🤖🔗

A visual, drag-and-drop platform that empowers users to create and execute AI workflows without writing code. This prototype demonstrates a "Search & Summarize" pipeline, connecting a web search tool to an LLM agent via a graphical interface.

[cite_start]Submitted for the **AI Engineering Intern Assignment (Project Option 2)**[cite: 15].

## 🚀 What I Built
[cite_start]This project is a **Drag-and-Drop Agentic UI Platform**[cite: 15]. [cite_start]It solves the problem of allowing non-technical teams to visualize AI processes[cite: 17].

**Key Features:**
* **Visual Canvas:** A drag-and-drop interface built with vanilla HTML5/JS (no heavy frontend frameworks) to place nodes and draw connections.
* [cite_start]**Tool Integration:** Uses **Tavily API** for optimized, real-time web searching[cite: 22].
* [cite_start]**AI Agent:** Uses **Groq (Llama 3.1)** for ultra-fast summarization and reasoning[cite: 21].
* [cite_start]**Interactive Chat:** A built-in chat interface that retains context, allowing users to ask follow-up questions about the workflow results[cite: 12].

## 🛠️ Tools & Models Used
* **Backend:** Python, Flask (lightweight API).
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (for canvas logic and state management).
* **AI Model:** `llama-3.1-8b-instant` via **Groq** (chosen for low latency).
* **Search Tool:** **Tavily API** (chosen for high-quality, LLM-ready search results).
* **Libraries:** `flask-cors` (frontend-backend communication), `dotenv` (security).

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Akbarhusain12/Gwk_AI.git
cd <YOUR_REPO_NAME>
```

### 2. Set Up Environment Variables
``` Create a .env file in the root directory and add your API keys:

Code snippet

GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

