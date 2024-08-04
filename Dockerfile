FROM nvcr.io/nvidia/pytorch:24.02-py3

RUN pip3 install rerun-sdk==0.17.0

WORKDIR /tiny-diffusion
