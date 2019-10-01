from flask import Flask, jsonify

app = Flask(__name__)

team = [
  {
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

@app.route('/myrecovery/api/v1.0/team/firstName/mary', methods=['GET'])
def get_mary():
    return jsonify({'firstName': 'Mary'})

if __name__ == '__main__':
    app.run(debug=True)
