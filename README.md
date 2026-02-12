# Flask Micro API

## Description
This is a simple Flask-based RESTful API.

## Endpoints

### GET /hello
Returns a welcome message.

### GET /data
Returns all stored items.

### GET /data/<id>
Returns a single item by ID.

### POST /data
Adds a new item.

Example body:
{
  "name": "banana"
}

## How to Run

pip install -r requirements.txt  
python app.py

## Agile Process

Sprint 1:
- Created base Flask app
- Implemented GET endpoints

Sprint 2:
- Added POST functionality
- Tested using curl and Postman
