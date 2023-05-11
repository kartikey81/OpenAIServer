import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
    # Get the destination and description from the JSON request
    data = request.get_json()
    destination = data['destination']
    description = data['description']

    # Generate recommendations using the OpenAI API
    prompt = f"I'm planning a trip to {destination} and I'm looking for {description}. Can you recommend some places to visit?"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    recommendations = response.choices[0].text.split('\n')

    # Return the recommendations as a JSON response
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
