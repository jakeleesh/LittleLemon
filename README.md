# Little Lemon Restaurant API

# A Django REST Framework-based API for managing restaurant operations at Little Lemon. This capstone project allows you to demonstrate back-end development skills by solving real-world problems, such as building RESTful APIs for menu management, table bookings, and user authentication.  
---

## Table of Contents

- [About the Project](#about-the-project)
  - [Key Features](#key-features)
  - [Solution Architecture](#solution-architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Development and Deployment](#development-and-deployment)

---

## About the Project

The **Little Lemon Restaurant API** enables:  
- Managing the restaurant’s menu.  
- Handling table reservations.  
- Securing API endpoints with token-based authentication.  

This project covers foundational aspects of back-end development, including working with Django, databases, and RESTful APIs. It is part of a capstone course designed to validate your technical expertise. 

### Key Features

- **Menu Management**: APIs for adding, updating, and retrieving menu items.  
- **Table Booking**: Endpoints for creating and managing table reservations.  
- **User Authentication**: Implements user registration, login, logout, and token-based API authentication.  
- **Security**: Protects sensitive endpoints with authentication and authorization mechanisms.  
- **Unit Testing**: Validates functionality using Django’s test framework and tools like Insomnia.  

### Solution Architecture
  
- **Backend**: Django REST Framework-based API.  
- **Database**: MySQL for persistent storage. 

---

## Tech Stack

- **Framework**: Django, Django REST Framework  
- **Database**: MySQL, mysqlclient  
- **Authentication**: Djoser, Token-based authentication  
- **Testing**: Django test framework, Insomnia  
- **Version Control**: Git, GitHub  

---

## Getting Started

### Installation

1. Install:
   ```bash
   pipenv install

   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

   python manage.py createsuperuser
   ```

---

## Usage  

### API Endpoints  

#### Public Endpoints  

- **Home**:  
  - `GET /restaurant/`: Displays the homepage.  

- **Menu Management**:  
  - `GET /restaurant/menu/`: Retrieve all menu items.  
  - `GET /restaurant/menu/<int:pk>/`: Retrieve a single menu item by ID.  

#### Booking Endpoints  

- **Table Booking**:  
  - `GET /restaurant/booking/`: Retrieve all table bookings.

#### Authentication Endpoints  

- **Token Authentication**:  
  - `POST /auth/token/login/`: Log in and receive an authentication token.  
  - `POST /auth/token/logout/`: Log out and revoke the authentication token.  

- **User Management**:  
  - `POST /auth/users/`: Register a new user.  
  - `GET /auth/users/me/`: Retrieve details of the currently logged-in user.  
  - Additional endpoints available through Djoser.

---

## Development and Deployment

### Testing

- Run unit tests

### Deployment

- Push commits to GitHub for version control.
