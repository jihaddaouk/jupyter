# Docker configuration
IMAGE_NAME = jihad/lp-service

.PHONY: run

# Run the Docker container
run:
	sudo docker run -v "$${PWD}":/app -p 8000:8000 $(IMAGE_NAME)
