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
  "team": {
    "id": 1234,
    "members": [
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
      },
    ]
  }
}
```

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
