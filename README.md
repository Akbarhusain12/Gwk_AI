# AI Workflow Builder

A visual, drag-and-drop platform that empowers users to create and execute AI workflows without writing code. This prototype demonstrates a "Search & Summarize" pipeline, connecting a web search tool to an LLM agent via a graphical interface.


## What I Built
This project is a **Drag-and-Drop Agentic UI Platform**. It solves the problem of allowing non-technical teams to visualize AI processes.

**Key Features:**
* **Visual Canvas:** A drag-and-drop interface built with vanilla HTML5/JS (no heavy frontend frameworks) to place nodes and draw connections.
* **Tool Integration:** Uses **Tavily API** for optimized, real-time web searching.
* **AI Agent:** Uses **Groq (Llama 3.1)** for ultra-fast summarization and reasoning.
* **Interactive Chat:** A built-in chat interface that retains context, allowing users to ask follow-up questions about the workflow results.

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
```

### 2. Set Up Environment Variables
``` Create a .env file in the root directory and add your API keys:
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```


### 4. Run the Application

Start the Flask backend server:

```bash
python app.py
```

You should see an output indicating the server is running (usually on `http://127.0.0.1:5000` or `http://localhost:5000`).

### 5. Launch the UI

Open your web browser and navigate to:
`http://localhost:5000`

---

## 🌐 Live Deployment (Heroku)

This project is deployed live on Heroku. You can access the working prototype here:

🔗 **Live Demo:** [https://gwk-ai-workflow-2229562f8361.herokuapp.com/](https://gwk-ai-workflow-2229562f8361.herokuapp.com/)

*(Note: If the app is sleeping, it may take 30-60 seconds to wake up on the first request.)*

---

## 🔮 Future Improvements

Per the submission guidelines, here is what I would improve with more time:

1. **Dynamic Graph Execution:** Currently, the backend logic is linear (Search → Summarize). I would implement a proper DAG (Directed Acyclic Graph) parser to execute nodes exactly as they are connected visually.
2. **Multi-Step Workflows:** Support chaining multiple agents (e.g., Search → Summarize → Email Draft).
3. **Save/Load Functionality:** Allow users to save their workflow configurations to a database.
4. **More Tools:** Add integrations for Calculator, Gmail, or Wikipedia APIs to expand the agent's capabilities.



## 📂 Project Structure

```text
/Gwk_AI
  ├── app.py              # Main Flask application (Backend API & Logic)
  ├── Procfile            # Heroku deployment configuration
  ├── requirements.txt    # Python dependencies
  ├── .env                # API Keys (Not pushed to GitHub)
  └── templates/
       └── index.html     # Frontend UI (Canvas, Drag & Drop, Chat)

```

