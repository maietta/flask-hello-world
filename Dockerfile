# Use the official Python image.
FROM python:3.10-slim

# Set the working directory.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install Flask and livereload
RUN pip install Flask livereload

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]