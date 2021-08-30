# Student result analysis application

### installation:

    $ pip install virtualenv

    $ virtualenv env

    $ source env/bin/activate

    $ sudo pip install -r requirements.txt

### Database migration

    $ ./manage.py makemigrations
    $ ./manage.py migrate

### Run server

    $ ./manage.py runserver


* Using django with sqlite3 databases.
* Below api requsts all using curl.


1. /api/student/ 
    * Get student details

        curl http://127.0.0.1:8000/api/student/
    
    * Post student details

        curl -d '{"Name":"saran", "RollNumber":"12ac2", "DateofBirth": "2021-08-11"}' -H "Content-Type: application/json" -X POST  http://127.0.0.1:8000/api/student/


2. /api/student/pk/marks/add/ 

    * Add marks to perticular student

        curl -d '{"marks":87}' -H "Content-Type: application/json" -X PUT  http://127.0.0.1:8000/api/student/pk/marks/add/

3. /api/student/pk/marks/ 

    * Get perticular student mark

        curl http://127.0.0.1:8000/api/student/pk/marks/



4. /api/student/marks/ 

    * Get all students marks
        curl http://127.0.0.1:8000/api/student/marks/

5. /api/student/results/ 

    * Get student results

        curl http://127.0.0.1:8000/api/student/results/
