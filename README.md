# A simple Flask API that can be deployed to Azure Container Apps

This project demonstrates how to create and deploy a Flask API using Azure Container Apps. It includes the necessary configurations and environment variables to get the application up and running in a containerized environment. The project utilizes Bootstrap.

## Project Structure

- `\api_app`: Directory containing the main code for the application (module in Python)
- `__init.py__`: Module intialization code where the Flask app is created
- `mainapp.py`: Entry point for the application. This entry point is what will be used when running this application from a container.
- `views.py`: Contains the views for the Flask application.
- `\api_app\static`: This directory containing all static assets used by the app, data, stylesheets etc.
- `\api_app\templates`: Contains templates used by Flask to render pages using the Jinja2 templating engine.
- `main.py`: Script file to run the project from command line during development for testing
- `Dockerfile`: The Docker configuration file to containerize the Flask application.
- `requirements.txt`: The dependencies required for the Flask application.
- `README.md`: Project documentation.

## Environment Variables

The project uses several environment variables to configure the Flask application and its deployment. Below is a description of each environment variable:

- `FLASK_ENV`: Specifies the environment in which the Flask application is running (e.g., `development`, `production`).
- `PORT`: The port on which the Flask application will run inside the container.
- `TAG_LINE`: A custom environment variable used to display a tagline or message in the Flask application. This can be used to personalize the API response or provide additional information to users.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ContainerAppsAndFlaskAPI.git
    cd ContainerAppsAndFlaskAPI
    ```

2. Build the Docker image:
    ```sh
    docker build -t flask-api .
    ```

3. Run the Docker container:
    ```sh
    docker run -d -p 5000:5000 --env-file .env flask-api
    ```

4. Access the Flask API at `http://localhost:5000`.

## Deployment

This project is configured to be deployed using Azure Container Apps. Ensure you have the Azure CLI installed and follow the Azure Container Apps documentation to deploy your containerized application.

## Using Podman Instead of Docker

This project uses Podman instead of Docker to build and manage container images. Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux system. Below are the steps to build the image and push it to the Azure Container Registry using Podman:

The file `build-scripts.ps1` contains scripts that show how you can build using podman.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.