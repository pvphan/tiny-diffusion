image:
	docker build . --tag tinydiff

shell: image
	docker run --rm -it --network=host --volume .:/tiny-diffusion tinydiff bash
