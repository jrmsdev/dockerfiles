FROM debian:testing-slim

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="19.7.2"

USER root:root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean
RUN apt-get update
RUN apt-get dist-upgrade -yy --purge

RUN apt-get install -yy --no-install-recommends bash less vim-tiny

RUN apt-get clean
RUN apt-get autoremove -yy --purge

RUN rm -rf /var/lib/apt/lists/*
RUN rm -f /var/cache/apt/archives/*.deb
RUN rm -f /var/cache/apt/*cache.bin

WORKDIR /root
CMD /bin/bash -i -l
