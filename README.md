# Flask Hello World with CSS Hot Reload

This project is a basic Python 3 Flask application that serves a simple "Hello World" message and includes CSS hot module reloading. The app runs inside a Docker container and can be managed using Docker Compose.

## Features

- Flask-based web application
- CSS Hot Module Reloading (using `livereload`)
- Dockerized for easy deployment and development
- Automatic file watching for HTML and CSS changes

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

```markdown
flask-hello-world/
│
├── app.py               # Main Flask application with livereload
├── Dockerfile           # Docker configuration file
├── docker-compose.yml   # Docker Compose configuration
│
├── static/              # Static files (CSS, JavaScript, images)
│   └── css/
│       └── style.css    # Main CSS file
│
└── templates/           # HTML templates
    └── index.html       # Main HTML file
```

This shows a clear directory structure with comments explaining the purpose of each file and folder.

## Running the Application

1. **Clone the repository**:

    ```bash
    git clone https://github.com/maietta/python-dockerized-website.git
    cd python-dockerized-website
    ```

2. **Build the Docker image**:

    ```bash
    docker-compose build
    ```

3. **Run the application**:

    ```bash
    docker-compose up
    ```

    The application will be available at `http://localhost:5000`.

## Live Reload

- **CSS Hot Reload**: Any changes made to `static/css/style.css` will automatically trigger a reload in the browser.
- **HTML Live Reload**: Changes to the `templates/index.html` file will also trigger a live reload.

## Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where Docker Compose is running or use:

```bash
docker-compose down
