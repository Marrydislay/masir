from flask import Flask
import openai

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 用你的 OpenAI API 密钥替换 "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"
openai.api_key = "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"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data["message"]
    chat_log = data.get("chat_log", [])

    chat_log.append({"role": "user", "content": message})

    model_response = openai.ChatCompletion.create(
        model="gpt-4-0314",  # 使用 GPT-4 模型
        messages=chat_log,
    ).choices[0].message["content"]

    chat_log.append({"role": "assistant", "content": model_response})

    return jsonify({"message": model_response, "chat_log": chat_log})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

