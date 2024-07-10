# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit config file to the appropriate location
RUN mkdir -p ~/.streamlit
COPY config.toml ~/.streamlit/config.toml

# Make port 80 available to the world outside this container
EXPOSE 80

# Run Streamlit
CMD ["streamlit", "run", "to_streamlitapp.py", "--server.port=80", "--server.address=0.0.0.0"]
