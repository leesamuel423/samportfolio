# Use base image that includes python
FROM python:3.9-slim-buster

# Set working directory in container
WORKDIR /myportfolio

# Copy requirements file into container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc g++ libffi-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy rest of application code into container
COPY . .

# Command to run application
CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
