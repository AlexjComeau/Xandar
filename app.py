from flask import Flask, render_template, jsonify, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    prompt = f"Edith, the helpful AI assistant: {message}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({"message": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)