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

class FirstName(Resource):
    def get(self, firstNameInput):
        name = [name for name in team if name['firstName'] == firstNameInput]
        if len(name) == 0:
            abort(404)
        return {'name': name[0]}


api.add_resource(Team, '/myrecovery/api/v1.0/team')
api.add_resource(FirstName, '/myrecovery/api/v1.0/team/firstName/<string:firstNameInput>')

if __name__ == '__main__':
    app.run(debug=True)
