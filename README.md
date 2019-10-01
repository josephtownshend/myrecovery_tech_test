# myrecovery_tech_test


### Strategy

I worked with data models briefly quite early on in the Makers course, so I feel a little unfamiliar with them at the moment. I am going to spend some time researching data models and from there start to draw up a diagram.

Notes...
- A data model is a logical representation of how the data will flow between different data entities and the relationships between them.
  - Entity Relationship Diagram
    - ERD cardinality is the style of notation used to declare relationship - one, many etc.

I have managed to draw up a ERD which I think is correct, I used Lucid Chart which is a great tool for this. I think from here I will try and workout the JSON data structure.
``` json
{
  "team": [
      {  
        "profilePicture": "https://www.profilePictures.com/mary-edwards-walker",
        "firstName": "Mary",
        "lastName": "Edwards Walker",
        "type": "Surgeon",
        "onLeave": false,
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
        "onLeave": false,
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
        "onLeave": false,
        "specialities": [
        "Orthopaedics",
        ],
        "biography": "American comedian, actress, writer, producer, and television host."
      }
  ]
}
```

At this point I want to start to look at Django and Flask, and make a decision which one to use. Flask might be the better option for me at the moment as it is a lighter weight framework than Django, so its simplicity might be more useful for this exercise.

As I already had `virtualenv` installed on my machine I ran...

`$ virtualenv myrecovery`
`$ flask/bin/pip install flask`

This created a myrecovery virtual environment, which I then installed flask in.

From here I added a simple app.py file which returns "Hello, World!".
To run the file I used...

`$ export FLASK_APP=app.py`
`$ flask run`
` * Running on http://127.0.0.1:5000/`

I can now start to create a database of team members in memory, just a simple array of dictionaries.

I removed id and members from my JSON data for the moment just to simplify the request. I'm not sure if I really need them anyway.

I created the `get_team` function which is associated with the /myrecovery/api/v1.0/team URI.

If I start the web service by running app.py, and open a new console window and run...

`$ curl -i http://localhost:5000/myrecovery/api/v1.0/team`

we get...

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 848
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Tue, 01 Oct 2019 10:11:42 GMT

{"team":[{"biography":"American abolitionist, prohibitionist, prisoner of war and surgeon.","firstName":"Mary","lastName":"Edwards Walker","onLeave":"false","profilePicture":"https://www.profilePictures.com/mary-edwards-walker","specialities":["Orthopaedics","Renal"],"type":"Surgeon"},{"biography":"English social reformer and statistician, and the founder of modern nursing.","firstName":"Florence","lastName":"Nightingale","onLeave":"false","profilePicture":"https://www.profilePictures.com/florence-nightingale","specialities":["Orthopaedics","Renal","Paediatrics"],"type":"Nurse"},{"biography":"American comedian, actress, writer, producer, and television host.","firstName":"Joan","lastName":"Rivers","onLeave":"false","profilePicture":"https://www.profilePictures.com/joan-rivers","specialities":["Orthopaedics"],"type":"Admin Assistant"}]}
```

Which from the header we can see is JSON data however the formatting is not right. I'm not sure why this is happeneing.




### Data model

Here is my first attempt at an Entity Relationship Diagram (ERD). I gave the team an id as I feel like would a useful feature further down the line.

![screenshot of ERD 1](https://github.com/josephtownshend/myrecovery_tech_test/blob/master/Images/ERD_1.jpg)

### Team Logic

  * Surgeon A
    - Nurse A
    - Nurse B
    - Admin Assistant A

  * Surgeon B
    - Nurse B
    - Nurse C
  - Admin Assistant B

The logic for a team is as follows:
* There must be at least one surgeon and one nurse in a team
* There must be at most one surgeon and one admin assistant in a team
* Nurses and admin assistants can work in up to three teams
* Surgeons can only work in one team

### Endpoint

profilePicture
firstName
lastName
type (e.g. Surgeon, Nurse, Admin Assistant)
onLeave
specialities (e.g. Orthopaedics, Renal, Paediatrics)
biography
