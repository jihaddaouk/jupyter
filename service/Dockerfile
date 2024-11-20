# Use Python slim image as base
FROM python:3.8-slim

# Create and set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt .
COPY model.joblib .
COPY main.py .


# Install requirements
RUN pip install -r requirements.txt
RUN pip install joblib
RUN pip install numpy


# Command to start the service
# --host: Listen on all interfaces
# --port: Specify port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
