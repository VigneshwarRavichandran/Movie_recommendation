from flask import request, Flask, jsonify
from response import *

app = Flask(__name__) 

@app.route('/recommend', methods=['POST'])
def recommend():
  data = request.get_json()
  movie = data['name']
  response = get_recommendation(movie)
  return jsonify({
    'Recommendation' : response
  })

if __name__ == '__main__':
    app.run(debug=True)
