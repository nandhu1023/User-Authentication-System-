# User-Authentication-System-
User Authentication System
This project is a GUI-based user authentication system built using Python, Tkinter, MySQL, and PIL. The system includes functionalities for user login, signup, and password reset.

# Features
Login Page: Users can log in with their registered username and password.
Signup Page: New users can create an account with a unique username, email, and password.
Password Reset: Users can reset their password in case they forget it, using their username.
# Technologies Used
Python: Core programming language for the project.
Tkinter: Used for building the graphical user interface (GUI).
MySQL: Database for storing user information securely.
PIL (Python Imaging Library): For handling images in the GUI.
# Project Structure
login.py: The main file that contains the login functionality.
signup.py: Handles user registration and validation.
MySQL Database: The database stores user credentials (username, email, and password).
# Prerequisites
To run this project, you will need:

Python 3.x
MySQL Server
Required Python libraries:
pip install tkinter
pip install pymysql
pip install pillow
# Database Setup
Ensure MySQL server is running on your machine.
Create a database named userdata:
sql

CREATE DATABASE userdata;
The tables will be automatically created when you first run the signup process.
# How to Run
Clone this repository to your local machine.
Ensure that you have the MySQL server running and properly configured with the database setup mentioned.
Execute login.py to start the application:
python login.py
