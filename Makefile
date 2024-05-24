image:
	docker build . --tag tinydiff

shell: image
	docker run --rm -it --volume .:/tiny-diffusion tinydiff bash
