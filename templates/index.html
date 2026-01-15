import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates')
CORS(app)

# Initialize Clients
try:
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
except Exception as e:
    print("⚠️ API Keys missing!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_workflow', methods=['POST'])
def run_workflow():
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({"status": "error", "message": "Query is empty"})

    try:
        # Step 1: Tavily Search
        print(f"🔎 Searching: {query}")
        search_result = tavily_client.search(query=query, search_depth="basic", max_results=3)
        
        results_text = ""
        for result in search_result.get('results', []):
            results_text += f"- {result['content']}\n"
        
        if not results_text:
            results_text = "No results found."

        # Step 2: Groq Summarization
        print("🤖 Summarizing...")
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
        
        # Create the Context String to send back to the user
        new_context = f"Previous Query: {query}\nSearch Data: {results_text}\nAgent Answer: {agent_response}"

        return jsonify({
            "status": "success",
            "tool_output": results_text,
            "agent_response": agent_response,
            "context": new_context  # <--- SENDING CONTEXT TO FRONTEND
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message')
    # Get the context provided by the frontend
    context = data.get('context', 'No context provided.')

    try:
        completion = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Answer based on the provided Context."},
                {"role": "user", "content": f"Context:\n{context}\n\nUser Question: {user_msg}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"response": "Error processing chat."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)