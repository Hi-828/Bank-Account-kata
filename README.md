# Bank Account Kata

This is a full-stack implementation of the Bank Account Kata. It includes a backend server-side application with a RESTful HTTP API using Django and a frontend browser application.

## Table of Contents
1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
3. [Features](#features)
4. [Bonus Features](#bonus-features)
5. [Running the Application](#running-the-application)

## Requirements

1. No user authentication required.
2. As a user, I want to deposit money into my account.
3. As a user, I want to withdraw money from my account.
4. As a user, I want to transfer money to another account (only IBAN accounts supported). The application must prevent the user from sending money to a non-IBAN account.
5. As a user, I want to see my account statement (date, amount, balance). The application must display the account statement sorted by date (most recent first) by default.

### Bonus Features

1. As a user, I want to sort my account statement by date (in ascending and descending order).
2. As a user, I want to search movements filtering by deposits, withdrawals, and date ranges (combination of filters must be implemented with an “AND” logical operator). The application must display search results sorted by date (most recent first) by default.
3. As a user, I want to sort search results by date (in ascending and descending order).
4. For both account statements and search results, the application must paginate movements when there are more than 10 elements. As a user, I want to see the next page, previous page, first page, and last page.

## Setup Instructions

### Prerequisites

- Visual Studio Code (VS Code)
- Python 3.x
- Django
- Node.js and npm (for the frontend application)

### Setting up the Backend Application

1. **Clone the repository:**

  git clone https://github.com/username/repo_name.git

  cd repo_name
   
  code .

Select the Python interpreter in VS Code:

Open the Command Palette (Ctrl+Shift+P).
Type Python: Select Interpreter and choose your Python 3 interpreter.

Install Django:

pip install django

Run the server:

python manage.py runserver

Install dependencies:

npm install

Run the frontend application:
npm start

Backend Application
The backend application is built using Django. It exposes a RESTful HTTP API for managing bank accounts, deposits, withdrawals, and transfers.

## API Endpoints
POST /api/deposit - Deposit money into an account.

POST /api/withdraw - Withdraw money from an account.

POST /api/transfer - Transfer money to another account (only IBAN accounts supported).

GET /api/account-statement - Get account statement sorted by date (most recent first).


## Features
Deposit Money: Users can deposit money into their accounts.

Withdraw Money: Users can withdraw money from their accounts.

Transfer Money: Users can transfer money to IBAN-supported accounts.

View Account Statement: Users can view their account statements sorted by date (most recent first).

## Bonus Features
Sort Account Statement: Users can sort their account statements by date in ascending or descending order.

Search Movements: Users can filter account movements by deposits, withdrawals, and date ranges.

Paginate Movements: Users can paginate through their account statements and search results if there are more than 10 elements.

Running the Application
Start the backend server:

python manage.py runserver

Open your browser and navigate to:

http://127.0.0.1:8000/
You should now be able to interact with the Bank Account Kata application.
