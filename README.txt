Project Name: Teacher Management System
Description:
This project is a web-based application that allows users to manage teacher records, including retrieving a list of teachers and adding new teachers to the database.

Technologies Used:
Python (Flask)
MySQL (Database)
PyMySQL (Database Connector)
Flask-RESTful (API Handling)
Postman (For API Testing)

-Configuration of  database in Config.py
DB_HOST = "127.0.0.1"
DB_USERNAME = "root"
DB_PASSWORD = "shereen123"
DB_NAME = "db_madrasa_com_test"

-Run the Flask application:
python init.py

- API Endpoints:

    - Get all teachers
    Method: GET
    URL: /get/teachers
    Response:
    json
    {
    "teachers": [
        {"id": 5, "name": "ahmed ali", "email": "ahmed@example.com", "phone": "01012345678"}
        ]
    }

    -Add a new teacher
    Method: POST
    URL: /teachers/add
    Request Body (JSON)
    {
    "name": " mohammed ",
    "email": "mohamed@example.com",
    "phone": "01123456789",
    "age": 35,
    "experience": 10,
    "specialization": "Math"
    }

    Response:
    json
    {"success": true, "message": "1 teacher(s) added"}



- Testing with Postman:
Import the API endpoints into Postman.
Use GET for retrieving teachers and POST for adding new ones.

- Frontend Integration:
The API can be accessed via a simple HTML form using JavaScript 
for sending requests and get teachers or adding a teacher.