from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

team = [
  {
    "id": 1,
    "profilePicture": "https://www.profilePictures.com/mary-edwards-walker",
    "firstName": "Mary",
    "lastName": "Edwards Walker",
    "type": "Surgeon",
    "onLeave": "false",
    "specialities": [
    "Orthopaedics",
    "Renal"
    ],
    "biography": "American abolitionist, prohibitionist, prisoner of war and surgeon."
  },
  {
    "id": 2,
    "profilePicture": "https://www.profilePictures.com/florence-nightingale",
    "firstName": "Florence",
    "lastName": "Nightingale",
    "type": "Nurse",
    "onLeave": "false",
    "specialities": [
    "Orthopaedics",
    "Renal",
    "Paediatrics"
    ],
    "biography": "English social reformer and statistician, and the founder of modern nursing."
  },
  {
    "id": 3,
    "profilePicture": "https://www.profilePictures.com/joan-rivers",
    "firstName": "Joan",
    "lastName": "Rivers",
    "type": "Admin Assistant",
    "onLeave": "false",
    "specialities": [
    "Orthopaedics",
    ],
    "biography": "American comedian, actress, writer, producer, and television host."
  }
]

@app.route('/myrecovery/api/v1.0/team', methods=['GET'])
def get_team():
    return jsonify({'team': team})

@app.route('/myrecovery/api/v1.0/team/id/<int:person_id>', methods=['GET'])
def get_name(person_id):
    name = [name for name in team if name['id'] == person_id]
    if len(name) == 0:
        abort(404)
    return jsonify({'name': name[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404) 

if __name__ == '__main__':
    app.run(debug=True)
