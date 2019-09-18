FROM jrmsdev/debian

LABEL mantainer="Jeremías Casteglione <jeremias.tincan@gmail.com>"
LABEL version="19.9.17"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean && \
	apt-get update -yy && \
	apt-get install -yy --no-install-recommends tinyca zip && \
	apt-get clean && \
	apt-get autoremove -yy --purge && \
	rm -rf /var/lib/apt/lists/* \
		/var/cache/apt/archives/*.deb \
		/var/cache/apt/*cache.bin

RUN useradd -d /home/ca -m ca && \
	mkdir -vp /home/ca/.TinyCA && \
	chown -vR ca:ca /home/ca/.TinyCA

VOLUME /home/ca/.TinyCA

ENV HOME /home/ca
WORKDIR /home/ca

USER ca:ca
ENTRYPOINT /usr/bin/tinyca2
