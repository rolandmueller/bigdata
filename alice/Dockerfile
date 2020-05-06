# Use an official Python runtime as a parent image
FROM ubuntu

# Set the working directory to /app
WORKDIR /~

# Copy the current directory contents into the container at /app
COPY app/ /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]