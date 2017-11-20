############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:16.04

# Set the file maintainer (your name - the file's author)
MAINTAINER National Institute Of Standards and Technology

ENV CELL_STRUCTURE_SOURCE=segmentation-validation-web
ENV CELL_STRUCTURE_SITE=/sites

# Project code
COPY $CELL_STRUCTURE_SOURCE $CELL_STRUCTURE_SITE

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN apt-get install -y git

# Copy entrypoint script into the image
WORKDIR $CELL_STRUCTURE_SITE
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]