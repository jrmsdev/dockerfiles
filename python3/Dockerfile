FROM jrmsdev/debian

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="19.7.3"

RUN apt-get clean
RUN apt-get update
RUN apt-get dist-upgrade -yy --purge

RUN apt-get install -yy --no-install-recommends python3 python3-pip openssl \
	ca-certificates

RUN pip3 --version
RUN pip3 install -U pip

RUN apt-get autoremove -yy --purge python3-pip

RUN apt-get clean
RUN apt-get autoremove -yy --purge

RUN rm -rf /var/lib/apt/lists/*
RUN rm -f /var/cache/apt/archives/*.deb
RUN rm -f /var/cache/apt/*cache.bin

RUN rm -rf /root/.cache/pip

RUN python3 --version
RUN pip --version

CMD /bin/bash -i -l
