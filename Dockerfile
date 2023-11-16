FROM python:3.11

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

# Install Python dependencies
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

# Copy your Django application code to the container
COPY . /app/

# Set the entrypoint
CMD ["gunicorn", "dj_selenium.wsgi"]

