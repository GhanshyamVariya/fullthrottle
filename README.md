# Full Throttle

* Clone this repo. Insert your database URI to __database.yaml__ file, then install all the packages needed. In this project I'm using __flask__, __flask_cors__, __flask_mysqldb__, __Flask-SQLAlchemy__ & __psycopg2__:
    ```bash
    $ git clone https://github.com/GhanshyamVariya/fullthrottle.git
    $ cd fullthrottle
    $ pip install -r requrements.txt
    ```

#

*  Execute migrations file:
    ```bash
    $ python manage.py migrate
    ```

#

*  Run the server locally at __*http://localhost:8000/*__ :
    ```bash
    $ python manage.py runserver
    ```

#

* Give a request to the server. You can use __Postman__ app:
    
    __See the opening screen__
    ```bash
    http://localhost:8000/admin/
    ```
    __Get all data & specific data by id:__
    ```bash
    GET /api/member-info
    curl -X GET -H 'Content-Type:application/json' http://localhost:8000/api/member-info
    ```

* To load data. You can use __Terminal__ command line:
    
    __See the opening screen__
    ```bash
    python manage.py load_data --path='/home/data/fullthrottle/TestJSON.json'
    ```