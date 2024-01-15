# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /backend
WORKDIR /backend

# Install FFmpeg for video processing
RUN apt-get update && \
    apt-get install -y ffmpeg

# Copy the requirements file into the container at /backend
COPY bjj-real-time-training-competition.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /backend
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Run gunicorn when the container launches
CMD ["gunicorn", "api:app", "-w 2", "-b 0.0.0.0:8080", "-t 30"]
