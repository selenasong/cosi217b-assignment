# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python files and other necessary files into the container
COPY . /app/

# Expose the port that the Streamlit app will run on
EXPOSE 8501

# Set the default command to run when the container starts
CMD ["streamlit", "run", "--server.port", "8501", "app_streamlit.py"]
