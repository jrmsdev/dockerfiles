FROM jrmsdev/debian:testing

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="240821"

ENV DEBIAN_FRONTEND noninteractive

ENV APT_INSTALL python3 openssl ca-certificates

RUN apt-get clean && \
	apt-get update -yy && \
	apt-get install -yy --no-install-recommends ${APT_INSTALL} && \
	apt-get clean && \
	apt-get autoremove -yy --purge && \
	rm -rf /var/lib/apt/lists/* \
		/var/cache/apt/archives/*.deb \
		/var/cache/apt/*cache.bin

RUN python3 --version

CMD /bin/bash -i -l
