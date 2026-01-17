import os
import g4f
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = "KOYEB_SECRET_VANTUS"

@app.route('/')
def index():
    return "Бот работает! Отправляй запросы через API."

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            provider=g4f.Provider.GPTalk,
            messages=[{"role": "user", "content": user_message}],
            stream=False
        )
        return jsonify({"response": str(response)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
