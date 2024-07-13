# Movies Dashboard Application

This application provides a Movies Dashboard, built with a Django backend and a React frontend. It allows users to visualize various statistics about movies, such as the top-grossing movies, top-rated movies, and more.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Running the Application Locally](#running-the-application-locally)
  - [Using Docker-compose](#using-docker-compose)
  - [Without Docker-compose](#without-docker-compose)
    - [Start the Backend Service](#start-the-backend-service)
    - [Start the Frontend Service](#start-the-frontend-service)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Visualize top 5 movies by gross for a particular year.
- Visualize top 5 movies or series of all time according to votes.
- Visualize top 10 movies according to rating for a particular year.

## Prerequisites

- Docker and Docker-compose (if using Docker)
- Python 3.9 or higher (if running locally without Docker)
- Node.js and npm (if running locally without Docker)

## Running the Application Locally

### Using Docker-compose

1. **Build and run the Docker images**:
   ```sh
   docker-compose up --build
