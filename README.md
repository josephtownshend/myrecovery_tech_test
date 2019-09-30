# myrecovery_tech_test


### Data model

I worked with data models briefly quite early on in the Makers course, so I feel a little unfamiliar with them at the moment. I am going to spend some time researching data models and from there start to draw up a diagram.

- A data model is a logical representation of how the data will flow between different data entities and the relationships between them.
  - Entity Relationship Diagram

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
