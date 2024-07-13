# Movies Dashboard Application

This application provides a Movies Dashboard, built with a Django backend and a React frontend. It visualizes various movie statistics, such as top-grossing movies and top-rated movies.

## Features

- Top 5 movies by gross for a particular year
- Top 5 movies or series of all time according to votes
- Top 10 movies according to rating for a particular year

## Prerequisites

- Docker and Docker-compose (if using Docker)
- Python 3.9+ (if running locally without Docker)
- Node.js and npm (if running locally without Docker)

## Running the Application Locally

### Using Docker-compose

1. Build and run the Docker images:
   ```sh
   docker-compose up --build
   ```

2. Access the Movies Dashboard at [http://0.0.0.0:3000/](http://0.0.0.0:3000/).

### Without Docker-compose

#### Backend

1. Navigate to the backend directory:
   ```sh
   cd backend
   ```

2. Run migrations:
   ```sh
   python manage.py migrate
   ```

3. Preprocess the data:
   ```sh
   python ./core/preprocess.py
   ```

4. Run the development server:
   ```sh
   python manage.py runserver 0.0.0.0:8000
   ```

5. Access the API documentation at [http://localhost:8000/api/schema/swagger-ui/#/](http://localhost:8000/api/schema/swagger-ui/#/).

#### Frontend

1. Navigate to the frontend directory:
   ```sh
   cd frontend/vphrase/
   ```

2. Install dependencies:
   ```sh
   npm install
   ```

3. Start the server:
   ```sh
   npm start
   ```

4. Access the Movies Dashboard at [http://localhost:3000](http://localhost:3000).
