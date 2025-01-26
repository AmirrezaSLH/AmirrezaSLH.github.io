from flask import Flask, request, jsonify
from your_script import send_query_to_gemini  # Import your function

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get('query')
    if question:
        result = send_query_to_gemini(question)
        # Assuming the result contains the answer in a specific format
        answer = result.get('some_key', 'No answer available.')
        return jsonify({'answer': answer})
    else:
        return jsonify({'error': 'No query provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
