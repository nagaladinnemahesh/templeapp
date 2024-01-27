# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE temple_booking.settings

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the project into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
