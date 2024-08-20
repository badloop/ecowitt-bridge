# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server.py file to the container
COPY server.py .

# Expose the port the server will run on (optional, adjust if needed)
EXPOSE 5000

# Run the Python script when the container starts
CMD ["python", "server.py"]

