# Full Throttle

* Clone this repo.:
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
    GET https://fullthrottleg.herokuapp.com/api/member-info
    curl -X GET -H 'Content-Type:application/json' http://localhost:8000/api/member-info
    ```

* To load data. You can use __Terminal__ command line:
   
    __Use the appropriate file path__
    ```bash
    python manage.py load_data --path='TestJSON.json'
    ```