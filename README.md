# vphrase
Steps to run the application locally using Docker-compose
Use docker-compose up –build to run and build the docker images.
Go to http://0.0.0.0:3000/ to view the Movies Dashboard.

Steps to run the application locally without using Docker-compose
Start the backend service:
cd into backend(django) service and run migrations using “python manage.py migrate”.
Run the preprocess.py file located in core app using “python ./core/preprocess.py” to clean and populate db using movies csv file.
Run the development server using “python manage.py runserver 0.0.0.0:8000” and got to “http://localhost:8000/api/schema/swagger-ui/#/” to checkout swagger.

Start the frontend service:
cd into frontend/vphrase/ and run “npm install” to install dependencies.
Use “npm start” to start the server and go to “http://localhost:3000” to view the dashboard.
