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

class Team(Resource):
    def get(self):
        return {'team': team}

class FirstName(Resource):
    def get(self, firstNameInput):
        name = [name for name in team if name['firstName'] == firstNameInput]
        if len(name) == 0:
            abort(404)
        return {'name': name[0]}

class LastName(Resource):
    def get(self, lastNameInput):
        name = [name for name in team if name['lastName'] == lastNameInput]
        if len(name) == 0:
            abort(404)
        return {'name': name[0]}


api.add_resource(Team, '/myrecovery/api/v1.0/team')
api.add_resource(FirstName, '/myrecovery/api/v1.0/team/firstName/<string:firstNameInput>')
api.add_resource(LastName, '/myrecovery/api/v1.0/team/lastName/<string:lastNameInput>')


if __name__ == '__main__':
    app.run(debug=True)
