Employee Registration and Management System
Project Overview
This project is a simple web application designed to manage employee registrations. It allows users to add new employees and view a list of all registered employees. The application is built using the Flask framework in Python, with data stored in a MySQL database managed via phpMyAdmin.

Key Features
Add New Employees:

Users can fill out a form to add a new employee to the database. The form collects essential details such as employee code, first name, last name, password, and status (active or inactive).
The submitted information is then saved to a MySQL database, ensuring that each employee has a unique identifier (empcode) to avoid duplication.
View Registered Employees:

The application displays a table listing all the employees who have been registered. This table includes columns for employee code, first name, last name, and status.
This feature allows users to quickly see all registered employees and their details in a structured format.
Technical Details
Backend:

The backend is built using Flask, a lightweight Python web framework.
SQLAlchemy is used for database operations, providing a high-level abstraction over raw SQL queries and allowing for seamless interaction with the MySQL database.
Database:

MySQL serves as the database management system, with phpMyAdmin used for database administration tasks.
The database stores employee information in a structured manner, enabling efficient storage and retrieval of employee records.
Frontend:

The frontend is built using HTML for structure, with basic CSS for styling.
A simple form is provided for entering employee details, and a table displays the list of registered employees.
How It Works
Setup:

Before running the application, ensure that the MySQL database and phpMyAdmin are properly set up.
Configure the database connection by providing the necessary credentials (user, password, host, and database name) in a .env file.
Running the Application:

Start the Flask application by running app.py. This will launch a web server that listens for incoming requests.
Open a web browser and navigate to the specified address (usually http://localhost:5000) to access the application.
Using the Application:

On the homepage, fill out the form with the required employee details and click "Add Employee" to save the information.
The newly added employee will be displayed in the table below the form, along with all previously registered employees.
Why This Project?
This project serves as a basic yet functional example of a web-based employee management system. It demonstrates key concepts such as form handling, database integration, and dynamic content rendering, making it a useful learning tool for anyone interested in web development with Flask and MySQL.
