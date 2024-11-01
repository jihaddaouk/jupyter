# Use Python slim image as base
FROM python:3.7-slim

# Create source directory
RUN mkdir src

# Set working directory
WORKDIR /src

# Install Jupyter
RUN pip install jupyter

# Command to start Jupyter server
# --no-browser: Don't open browser since we're in container
# --allow-root: Allow running as root user
# --ip: Listen on all interfaces
# --port: Specify port 8888
CMD ["jupyter", "notebook", "--no-browser", "--allow-root", "--ip=0.0.0.0", "--port=8888"]
