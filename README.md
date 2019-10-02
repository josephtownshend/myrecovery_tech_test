# myrecovery_tech_test

I have worked on two apps for this test - the first one is `app.py`, and the second is `app_test.py` which I took further and is the app I am submitting. I have kept both in the repo as `app.py` contains a majority of my working and corresponds to the readme which documents the process.

### Running the app

To run `app_test.py` simply..

`$ python app_test.py`

and in a separate console window use...

`$ curljson -i http://localhost:5000/myrecovery/team/firstName/Mary`

Or any of the other endpoints I have made available - (team, firstName, lastName, type, onLeave)

Note. in order to use `curljson` first

`$ pip install curljson`


### Strategy

I am in fairly unfamiliar terriorty with this test so I think my strategy is going to be to spend a good amount of time researching so I can understand what I am being asked to do as best as possible. From there I will work on the data model and the JSON which I think I can do quite easily - though again I'm not very familiar with this. Once I get this pinned down I'll move on to the framework and hopefully starting to write some code.

Despite having quite little experience with Python / Flask & Django I'm quite excited by this test as a learning experience and also very keen to learn more about data models and JSON.

---------

#### Data model

I worked with data models briefly quite early on in the Makers course, so I feel a little unfamiliar with them at the moment. I am going to spend some time researching data models and from there start to draw up a diagram.

Here is my first attempt at an Entity Relationship Diagram (ERD). I gave the team an id as I feel like would a useful feature further down the line. I used Lucid Chart which is a great tool for this. I think from here I will try and workout the JSON data structure.

![screenshot of ERD 1](https://github.com/josephtownshend/myrecovery_tech_test/blob/master/Images/ERD_1.1.jpg)

Notes...
- A data model is a logical representation of how the data will flow between different data entities and the relationships between them.
  - Entity Relationship Diagram
    - ERD cardinality is the style of notation used to declare relationship - one, many etc.

#### JSON data structure

Pretty happy with this section, I think the structure is accurate and is logical.

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
#### Framework

At this point I want to start to look at Django and Flask, and make a decision which one to use. Flask might be the better option for me at the moment as it is a lighter weight framework than Django, so its simplicity might be an advantage in this exercise and with my experience. Having spent a bit of time reading about both options I've decided to go with Flask.

#### Getting started

I need to set up a virtual environment for the app...
As I already had `virtualenv` installed on my machine I ran...

```shell
$ virtualenv myrecovery
$ flask/bin/pip install flask
```

This created a myrecovery virtual environment, which I then installed flask in. From here I added a simple app.py file which returns "Hello, World!".

To run the file I used...

```shell
$ export FLASK_APP=app.py
$ flask run
* Running on http://127.0.0.1:5000/
```

I can now start to create a database of `team` in memory, just a simple array of dictionaries. I removed `id` and `members` from my JSON data for the moment just to simplify the request. I'm not sure if I really need them anyway. I created the `get_team` function which is associated with the `/myrecovery/api/v1.0/team` URI. If I start the web service by running `app.py`, and open a new console window and run...

`$ curl -i http://localhost:5000/myrecovery/api/v1.0/team`

we get...

```json
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 848
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Tue, 01 Oct 2019 10:11:42 GMT

{"team":[{"biography":"American abolitionist, prohibitionist, prisoner of war and surgeon.","firstName":"Mary","lastName":"Edwards Walker","onLeave":"false","profilePicture":"https://www.profilePictures.com/mary-edwards-walker","specialities":["Orthopaedics","Renal"],"type":"Surgeon"},{"biography":"English social reformer and statistician, and the founder of modern nursing.","firstName":"Florence","lastName":"Nightingale","onLeave":"false","profilePicture":"https://www.profilePictures.com/florence-nightingale","specialities":["Orthopaedics","Renal","Paediatrics"],"type":"Nurse"},{"biography":"American comedian, actress, writer, producer, and television host.","firstName":"Joan","lastName":"Rivers","onLeave":"false","profilePicture":"https://www.profilePictures.com/joan-rivers","specialities":["Orthopaedics"],"type":"Admin Assistant"}]}
```

Which from the header we can see is JSON data however the formatting is not great. I've found and installed `curljson`, so now I can run...

`$ curljson - v http://localhost:5000/myrecovery/api/v1.0/team`

and it returns a prettified JSON output.

One note on the JSON data is that I had to change the `onLeave` booleans to a string as it was throwing errors. I'm not sure why this is happening but I'll come back to it if I have time. At this point I want to try and expose more endpoints, I'm not really sure how to go about this so I'm going to first try and just create a function to expose the `{'firstName': 'Mary'}`. I have written a basic function following the format of the `def_team` function that returns `{'firstName': 'Mary'}`


```json
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Tue, 01 Oct 2019 11:43:53 GMT

{
    "firstName": "Mary"
}
```

#### Next steps...

I felt a little bit stuck at this point, so I decided in order to make some progress with the logic I added an `'id':int` to each person. This allowed me to use a todo list tutorial and which might help me get unblocked. I created a function that takes a `person_id` and creates a dynamic endpoint that can output the corresponding person. Whilst this isn't part of the test - I do feel like it's a good step in the right direction. It will also return a `404 error` if the `id` isn't found in the `name` array. After testing the `404 error` I decided to try and get it to output a more useful error - I created a `not_found` function to do this and now when it can't find the inputted `id` it will output a JSON error message.  

`$ curljson -i http://localhost:5000/myrecovery/api/v1.0/team/id/1`

outputs...

```json
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 293
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Tue, 01 Oct 2019 13:59:07 GMT

{
    "name": {
        "biography": "American abolitionist, prohibitionist, prisoner of war and surgeon.",
        "firstName": "Mary",
        "id": 1,
        "lastName": "Edwards-Walker",
        "onLeave": "false",
        "profilePicture": "https://www.profilePictures.com/mary-edwards-walker",
        "specialities": [
            "Orthopaedics",
            "Renal"
        ],
        "type": "Surgeon"
    }
}
```

or

```json
{
    "error": "Not found"
}
```

I can now refactor my code by removing the `id` and instead get it to input and output the `firstName`. This seems to be working fine so from here I think I might now need to try and figure out how to make the entire URI dynamic - in the same way that I did for firstName. I'm going to spend a bit of time thinking about this as I think it sounds quite complex.

After spending some time researching I found flask-restful which looks like an interesting option, it can really help to tidy up the code but I think it can also be useful in making the URIs dynamic. I'm going to set up a test app and see if I can make any progress using that.

#### Conclusion

I have spent a bit more time with my app and used flask-restful to refactor it which has made it a lot tidier. I have exposed some more of the endpoints and they are working as expected. I am going to submit the test at this point - despite it being unfinished I feel like to get any further with it I would need invest much more time. Having worked on this now for 2 days I feel like I have made some really good progress into the test - and I've certainly learnt a huge amount. In terms of what I would do if I were to move forwards...

* Testing - I've used unittest before, I would need to find a mocking library for get requests.
* Figure out how to create an error function rather than returning a message from within `get` request.
* For the endpoints that aren't single words - figure out how to deal with URLS, Arrays, Biography.

In all I feel happy with my attempt, I went from not really understanding the challenge to feeling a lot more comfortable with the task in hand. I have definitely enjoyed the process, it's been great to get really out of my comfort zone and also learn a great deal about data models, JSON, Python, Flask.

-------

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
