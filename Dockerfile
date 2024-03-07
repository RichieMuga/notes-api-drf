FROM python:3.10

# Set the working directory in the container
ENV APP_HOME /app
WORKDIR $APP_HOME


# Copy the current directory contents into the container at /app
COPY requirements .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r production.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Setting this ensures print statements and log messages
# promptly appear in Cloud Logging.
ENV PYTHONUNBUFFERED TRUE

# Disable generating bytecode.
ENV PYTHONDONTWRITEBYTECODE TRUE