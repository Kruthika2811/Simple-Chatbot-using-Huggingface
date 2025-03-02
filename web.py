

# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# HF_API_KEY = "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"

# def chatbot(question):
#     API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
#     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
#     payload = {"inputs": question}

#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()[0]['generated_text']

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/ask', methods=['POST'])
# def ask():
#     try:
#         data = request.get_json()  # ✅ Ensure request is JSON
#         if not data or "message" not in data:
#             return jsonify({"error": "Invalid JSON input"}), 400
        
#         user_input = data["message"]
#         bot_response = chatbot(user_input)
#         return jsonify({"response": bot_response})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500  # Handle errors gracefully

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

HF_API_KEY = "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"

def chatbot(question):
    API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": question}

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
        return result[0]["generated_text"]
    else:
        return "Sorry, I couldn't generate a response."

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Invalid JSON input"}), 400
        
        user_input = data["message"]
        bot_response = chatbot(user_input)
        return jsonify({"response": bot_response})  # ✅ Ensure correct JSON format

    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == "__main__":
    app.run(debug=True)


