FROM jrmsdev/debian

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="240821"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean && \
	apt-get update -yy && \
	apt-get install -yy --no-install-recommends golang && \
	apt-get clean && \
	apt-get autoremove -yy --purge && \
	rm -rf /var/lib/apt/lists/* \
		/var/cache/apt/archives/*.deb \
		/var/cache/apt/*cache.bin

ENV GOPATH /go
RUN mkdir -vp -m 1777 ${GOPATH}
RUN go version

CMD /bin/bash -i -l
