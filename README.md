# About ChatSNC

ChatSNC is a chatbot designed to interact with users on the college
website. The frontend of the project is built using [Vue.js](https://vuejs.org/guide/introduction.html), a progressive JavaScript framework known for its adaptability and versatility. The backend is developed using [FastAPI](https://fastapi.tiangolo.com/tutorial/), a modern, high-performance web framework for building APIs with Python based on standard Python type hints.

## Requirements

- Node.js
- Python 3.11 (Importent)
- pip
- venv

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the frontend directory and run `npm install` to install the frontend dependencies.
3. Navigate to the backend directory and create a virtual environment with `python -m venv venv`.
4. Activate the virtual environment with `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows).
5. Install the backend dependencies with `pip install -r requirements.txt`.
6. Create a `.env` file in the frontend directory and add the following variable:
   - `VITE_API_ENDPOINT`: the URL of the backend API endpoint
7. Create a `.env` file in the backend directory and add the following variables:
   - `DATABASE_HOSTNAME`: the hostname of the PostgreSQL database
   - `DATABASE_PORT`: the port number of the PostgreSQL database
   - `DATABASE_NAME`: the name of the PostgreSQL database
   - `DATABASE_USERNAME`: the username for the PostgreSQL database
   - `DATABASE_PASSWORD`: the password for the PostgreSQL database
   - `SECRET_KEY`: a secret key forJWT tokens
   - `ALGORITHM`: the algorithm used for generating and verifying JWT tokens
   - `ACCESS_TOKEN_EXPIRE_MINUTES`: the expiration time for the JWT tokens in minutes
   - `OPENAI_API_KEY`: the API key for the OpenAI service
   - `APP`:Indicating whether the app is in development or production mode

## Usage

To run the project, follow these steps:

1. Navigate to the frontend directory and run `npm run serve` to start the frontend development server.
2. Navigate to the backend directory and run `uvicorn main:app --reload` to start the backend development server.
3. Open your browser and go to `http://localhost:5173` to access the web app.
