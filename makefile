# Docker configuration
IMAGE_NAME = jihad/lp-notebook

.PHONY: run

# Run the Docker container
run:
	sudo docker run -v "$${PWD}":/src -p 8888:8888 $(IMAGE_NAME)
