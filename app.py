import os
from flask import Flask, request, jsonify, render_template # Added render_template
from flask_cors import CORS
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# Tell Flask to look for templates in the 'templates' folder
app = Flask(__name__, template_folder='templates')
CORS(app)

# Initialize Clients
try:
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
except Exception as e:
    print("⚠️ API Keys missing!")

conversation_context = ""

# --- NEW ROUTE FOR HOME PAGE ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_workflow', methods=['POST'])
def run_workflow():
    global conversation_context
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({"status": "error", "message": "Query is empty"})

    try:
        # Step 1: Tool Execution (Tavily Search)
        print(f"🔎 Searching Tavily for: {query}")
        
        # We use .search() which is the standard method
        search_result = tavily_client.search(query=query, search_depth="basic", max_results=3)
        
        # Format the results into a single string
        results_text = ""
        for result in search_result.get('results', []):
            results_text += f"- {result['content']}\n"
        
        if not results_text:
            results_text = "No results found."

        # Step 2: Agent Execution (Groq Summarizer)
        print("🤖 Sending to Groq...")
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant. Summarize the search results for the user."
                },
                {
                    "role": "user",
                    "content": f"User Query: {query}\n\nSearch Results:\n{results_text}"
                }
            ],
            model="llama-3.1-8b-instant",
        )

        agent_response = chat_completion.choices[0].message.content
        
        # Store context for follow-up chat
        conversation_context = f"Previous Query: {query}\nSearch Data: {results_text}\nAgent Answer: {agent_response}"

        return jsonify({
            "status": "success",
            "tool_output": results_text,
            "agent_response": agent_response
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_context
    data = request.json
    user_msg = data.get('message')

    try:
        completion = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Answer based on the previous context."},
                {"role": "user", "content": f"Context:\n{conversation_context}\n\nUser Question: {user_msg}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"response": "Error processing chat."})

if __name__ == '__main__':
    app.run(port=5000, debug=True)