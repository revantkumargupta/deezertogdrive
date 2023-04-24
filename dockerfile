                                                                                  
# Base image
FROM python:3.9.7-slim-buster

# Set the working directory
WORKDIR /app
RUN apt-get update && apt-get install -y curl
# Copy the application code and runtime.txt
COPY . .
COPY runtime.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir deezloader==2022.3.5

# Expose the port the application will run on
EXPOSE 5000

# Set the command to run the application
CMD [ "python3", "main.py" ]

