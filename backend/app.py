from flask import Flask, jsonify, request

app = Flask(__name__)

rankings = []  # This will hold our rankings data

@app.route('/rankings', methods=['GET'])
def get_rankings():
    return jsonify(rankings), 200

@app.route('/rankings/<position>', methods=['GET'])
def get_rankings_by_position(position):
    position_rankings = [rank for rank in rankings if rank['position'] == position]
    return jsonify(position_rankings), 200

@app.route('/update-rankings', methods=['POST'])
def update_rankings():
    data = request.get_json()  # Expecting JSON data
    rankings.extend(data.get('rankings', []))  # Update rankings
    return jsonify({'message': 'Rankings updated!'}), 200

if __name__ == '__main__':
    app.run(debug=True)