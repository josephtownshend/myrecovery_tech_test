from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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
  }
]

class Team(Resource):
    def get(self):
        return {'team': team}

api.add_resource(Team, '/myrecovery/api/v1.0/team')

if __name__ == '__main__':
    app.run(debug=True)
