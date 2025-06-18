from flask import Flask, request, jsonify, render_template
from app2 import wikipedia_summary  # 👈 function from your app2.py

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("prompt")

    # Check if user asked for a book or science fiction
    if "science fiction" in user_input.lower():
        return jsonify({"reply": "📚 You can read amazing Sci-Fi books here:\nhttps://www.gutenberg.org/ebooks/bookshelf/76"})
    
    # Otherwise, respond using your Wikipedia logic
    try:
        reply = wikipedia_summary(user_input)
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
