ifneq ($(shell lshw -C display 2> /dev/null | grep NVIDIA | wc -l), 0)
	GPU_FLAG:=--gpus=all
endif

RUN_FLAGS = \
	--rm -it \
	${GPU_FLAG} \
	--ipc=host \
	--network=host \
	--volume .:/tiny-diffusion \

IMAGE_TAG?=tinydiff

image:
	docker build . --tag ${IMAGE_TAG}

shell: image
	docker run ${RUN_FLAGS} ${IMAGE_TAG} bash
