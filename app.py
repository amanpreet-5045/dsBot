from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = "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"

@app.route('/analyze', methods=['POST'])
def analyze_data():
    query = request.json.get('query')
    # Call OpenAI's GPT-3 API to process the query
    # Perform data analysis based on the query
    # Return results as JSON response
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose appropriate GPT-3 engine
        prompt=query,
        max_tokens=100  # Adjust as needed
    )
    result = response.choices[0].text.strip()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
