## Flask-CRUD

This is a RESTful API with CRUD operations created using Python and Flask, along with JavaScript, HTML, and CSS. The main purpose of this project is to better understand the structure and behavior of RESTful APIs through a practical implementation.

## Initialize the Project

To initialize the project, open your IDE terminal and navigate to the root directory of the application. Once there, run the following command:

- python3 app.py

This command will start a development server. The application will be accessible at http://localhost:3001, where you can test the different routes and verify the proper functionality of the CRUD operations.

## Features

- Create, Read, Update, and Delete data through HTTP requests.

- Use of Flask routes to handle client-server communication.

Frontend interface built with HTML, CSS, and JavaScript for easier interaction with the API.

Simple and clean project structure for educational purposes.

- /FLASKS-CRUD
- │
- ├── static/ # CSS and client-side JavaScript files
- ├── templates/ # HTML templates
- ├── app.py # Main application file
- └── README.md # Project documentation

## Requirements

Make sure to install the required dependencies before running the application. You can use the following command:

- pip install -r requirements.txt

Alternatively, manually install Flask if you don't have a requirements file:

- pip install Flask
- API Endpoints

# Below are examples of basic routes:

- GET / – Fetch all items (index function)

- POST /add_contact – Create a new item (add_contact function)

- POST /update/user_id – Update an existing item (update_contact function)

- DELETE /delete/id – Delete an item by ID (delete function)

## Conclusion

This project serves as a foundational example for understanding how full-stack applications can interact through RESTful principles. It is ideal for students or developers who want to strengthen their knowledge in web development with Python and Flask.
