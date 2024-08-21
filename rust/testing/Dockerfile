FROM jrmsdev/debian:testing

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="240821"

ENV DEBIAN_FRONTEND noninteractive

ENV APT_INSTALL openssl ca-certificates rustup

RUN apt-get clean && \
	apt-get update -yy && \
	apt-get install -yy --no-install-recommends ${APT_INSTALL} && \
	apt-get clean && \
	apt-get autoremove -yy --purge && \
	rm -rf /var/lib/apt/lists/* \
		/var/cache/apt/archives/*.deb \
		/var/cache/apt/*cache.bin

RUN rustup --version

RUN rustup default beta

RUN rustc --version

CMD /bin/bash -i -l
