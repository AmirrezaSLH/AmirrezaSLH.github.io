from flask import Flask, request, jsonify
from your_script import send_query_to_gemini

app = Flask(__name__)
api_key = None  # Global variable to store the API key


@app.route('/save_api_key', methods=['POST'])
def save_api_key():
    global api_key
    data = request.json
    api_key = data.get('api_key')
    if api_key:
        return jsonify({'message': 'API key saved successfully.'}), 200
    else:
        return jsonify({'error': 'Invalid API key.'}), 400


@app.route('/query', methods=['POST'])
def query():
    global api_key
    if not api_key:
        return jsonify({'error': 'API key not set.'}), 400

    data = request.json
    question = data.get('query')
    if question:
        result = send_query_to_gemini(question, api_key=api_key)
        answer = result.get('some_key', 'No answer available.')
        return jsonify({'answer': answer})
    else:
        return jsonify({'error': 'No query provided.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
