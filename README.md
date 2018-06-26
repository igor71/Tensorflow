# Tensorflow
This repo contain docker files and code for building tensorflow package form the sources

Dockerfile.devel-cpu-mkl used for creating yi/tflow:0.0 docker image.

This image will using as building and testing environment for tensorflow CPU version

Dockerfile.cpu-mkl used or creating yi/tflow:0.1 docker image.

This image will be used for building from the sources, installing and testing TF_CPU version

Dockerfile.SSH-Build used for creating yi/tflow:0.2 docker image.  

This image will be used as working environment for deep learning with TF_CPU

Running docker containers from the above images:

For yi/tflow:0.0 / 0.1:

docker run -it -v /media:/media yi/tflow:0.0 /bin/bash
  
For yi/tflow:0.2:

docker run -d -p 37001:22 --name tflow_build -v /media:/media yi/tflow:0.2

This docker container will run in detached mode. Connect to it using ssh port 37001, user::jenkins.

Check Tensorflow version:

Command for python 2.7 = {python -c 'import tensorflow as tf; print(tf.__version__)'}
