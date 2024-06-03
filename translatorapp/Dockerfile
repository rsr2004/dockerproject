  GNU nano 7.2                                                                                        Dockerfile                                                                                                 
# Dockerfile
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install Flask

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
