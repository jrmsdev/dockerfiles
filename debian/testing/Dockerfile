FROM debian:testing-slim

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="240821"

USER root:root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean && \
	apt-get update -yy && \
	apt-get dist-upgrade -yy --purge && \
	apt-get install -yy --no-install-recommends bash && \
	apt-get clean && \
	apt-get autoremove -yy --purge && \
	rm -rf /var/lib/apt/lists/* \
		/var/cache/apt/archives/*.deb \
		/var/cache/apt/*cache.bin

WORKDIR /root
CMD /bin/bash -i -l
