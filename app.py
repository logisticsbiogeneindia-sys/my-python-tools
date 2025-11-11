from flask import Flask, request, jsonify
from tools import tool1, tool2

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Python Tools API is running!"}

@app.route("/run_tool", methods=["POST"])
def run_tool():
    data = request.get_json()
    tool = data.get("tool")
    input_data = data.get("input")

    if tool == "tool1":
        result = tool1.run(input_data)
    elif tool == "tool2":
        result = tool2.run(input_data)
    else:
        result = "Invalid tool"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
