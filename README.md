# Debian

Just dist-upgrade and cleanup base image.

* [debian](https://github.com/jrmsdev/dockerfiles/blob/master/debian/Dockerfile)
	* FROM debian:stable-slim
* [debian:testing](https://github.com/jrmsdev/dockerfiles/blob/master/debian/testing/Dockerfile)
	* FROM debian:testing-slim

All packages are installed with _apt-get install --no-install-recommends_

# Golang

Install golang package.

* [golang](https://github.com/jrmsdev/dockerfiles/blob/master/golang/Dockerfile)
	* FROM jrmsdev/debian
* [golang:testing](https://github.com/jrmsdev/dockerfiles/blob/master/golang/testing/Dockerfile)
	* FROM jrmsdev/debian:testing

# Python3

Install packages: python3 and python3-distutils and some deps.

Install/Update pip packages: pip, setuptools and wheel.

* [python3](https://github.com/jrmsdev/dockerfiles/blob/master/python3/Dockerfile)
	* FROM jrmsdev/debian
* [python3:testing](https://github.com/jrmsdev/dockerfiles/blob/master/python3/testing/Dockerfile)
	* FROM jrmsdev/debian:testing
