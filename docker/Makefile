.PHONY: image container attach clean

CONTAINER_NAME := "dev-container"
IMAGE_NAME := "ubuntu-22-04-dev"
WORKSPACE_HOST_PATH := "/Users/iolkhovsky/repos"
WORKSPACE_CONTAINER_PATH := "/repos"
FORWARD_PORT := 55501

image:
	docker build -t $(IMAGE_NAME) .

container:
	docker run \
		-it \
		-d \
		--name $(CONTAINER_NAME) \
		-p $(FORWARD_PORT):$(FORWARD_PORT) \
		-v $(WORKSPACE_HOST_PATH):$(WORKSPACE_CONTAINER_PATH) \
		$(IMAGE_NAME):latest

attach:
	docker start -ia $(CONTAINER_NAME)

clean:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)
	-docker rmi -f $(IMAGE_NAME)
