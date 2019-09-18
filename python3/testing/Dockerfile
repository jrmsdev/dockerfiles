FROM jrmsdev/debian:testing

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="19.9.17"

ENV DEBIAN_FRONTEND noninteractive

ENV APT_INSTALL python3 python3-pip openssl ca-certificates python3-distutils

RUN apt-get clean && \
	apt-get update -yy && \
	apt-get install -yy --no-install-recommends ${APT_INSTALL} && \
	apt-get clean && \
	apt-get autoremove -yy --purge && \
	rm -rf /var/lib/apt/lists/* \
		/var/cache/apt/archives/*.deb \
		/var/cache/apt/*cache.bin

RUN pip3 install -U pip && \
	pip install -U setuptools && \
	pip install -U wheel && \
	python3 --version && pip --version

CMD /bin/bash -i -l
